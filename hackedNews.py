import os
import os.path
from urlparse import urlsplit
import sys
from pymongo import MongoClient
import tornado.ioloop
import tornado.web
import scrape
import naiveBayes
import helpers
import json
import ui_methods

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "RobotsBeware",
    "login_url": "/login",
    "xsrf_cookies": True,
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	titleLinkAssoc = scrape.scrapeHN()
        self.render("home.html",
        titleLinks = titleLinkAssoc
        )
    
class Ham(tornado.web.RequestHandler):
	def get(self):
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		parsed = urlsplit(mongo_url)
		db_name = parsed.path[1:]
		client = MongoClient(mongo_url)
		db = client.db_name
		ham = db.Ham
		response = {}
		for el in list(ham.find()):
			response[el["word"]] = el["count"]
		self.write(
			json.dumps(
				response
				)
			)

	def post(self):
		title = self.get_argument("title")
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		db_name = "bayesDict"
		client = MongoClient(mongo_url)
		db = client.db_name
		ham = db.Ham
		query = helpers.formatQuery(title)
		for word in query:
			ham.update({"word":word}, {"$inc": {"count":1} }, upsert=True)
		
class Spam(tornado.web.RequestHandler):
	def get(self):
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		db_name = "bayesDict"
		client = MongoClient(mongo_url)
		db = client.db_name
		spam = db.Spam
		response = {}
		for el in list(spam.find()):
			response[el["word"]] = el["count"]
		self.write(
			json.dumps(
				response
				)
			)

	def post(self):
		title = self.get_argument("title")
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		db_name = "bayesDict"
		client = MongoClient(mongo_url)
		db = client.db_name
		spam = db.Spam
		query = helpers.formatQuery(title)
		for word in query:
			spam.update({"word":word}, {"$inc": {"count":1} }, upsert=True)
		

class Filter(tornado.web.RequestHandler):
	def get(self):
		self.render("spam.html")


handlers = [
    (r"/", MainHandler),
    (r"/ham", Ham),
    (r"/spam", Spam),
    (r"/filter", Filter),
]

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"), 
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        ui_methods=ui_methods,
)               

application = tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    application.listen(os.environ.get("PORT", 5000))
    tornado.ioloop.IOLoop.instance().start()

