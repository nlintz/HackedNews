import os
import os.path
from urlparse import urlsplit
from pymongo import MongoClient
import tornado.ioloop
import tornado.web
import scrape
import helpers
import json
import ui_methods

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "RobotsBeware",
    "login_url": "/login",
    "xsrf_cookies": True,
}


class MainHandler(tornado.web.RequestHandler): #handler for hackernews
	def get(self):
		titleLinkAssoc = scrape.scrapeHN()
		self.render("home.html",
		titleLinks = titleLinkAssoc
		)

class RedditHandler(tornado.web.RequestHandler): #handler for reddit
	def get(self):
		titleLinkAssoc = scrape.scrapeReddit()
		self.render("reddit.html",
		titleLinks = titleLinkAssoc
		)

		"""
		API changes slightly to accomadate more sites
		"""
class TechCrunch(tornado.web.RequestHandler):
	def get(self):
		titleLinkAssoc = scrape.scrape('http://www.techcrunch.com/', 'h2.headline > a')
		self.render("scraped.html",
		titleLinks = titleLinkAssoc,
		site = "Tech Crunch"
		)

class Metafilter(tornado.web.RequestHandler):
	def get(self):
		titleLinkAssoc = scrape.scrape('http://www.metafilter.com/', 'div.posttitle > a')
		formattedLinks = ['http://www.metafilter.com'+ v for k,v in titleLinkAssoc.items()] #metafilter hosts their own content so you need to add http://www.metafilter to each link
		titles = [k for k,v in titleLinkAssoc.items()]
		formattedLinkAssoc = dict(zip(titles, formattedLinks))
		self.render("scraped.html",
		titleLinks = formattedLinkAssoc,
		site = "MetaFilter"
		)

class SlashDot(tornado.web.RequestHandler):
	def get(self):
		titleLinkAssoc = scrape.scrape('http://www.slashdot.org/', 'h2 > span > a')
		self.render("scraped.html",
		titleLinks = titleLinkAssoc,
		site = "Slash Dot"
		)

class Digg(tornado.web.RequestHandler):
	def get(self):
		titleLinkAssoc = scrape.scrape('http://www.digg.com/', 'h2.story-title > a')
		self.render("scraped.html",
		titleLinks = titleLinkAssoc,
		site = "Digg"
		)
	
class Ham(tornado.web.RequestHandler):
	def get(self):
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017') #connect to DB
		parsed = urlsplit(mongo_url)
		db_name = parsed.path[1:]
		username = parsed.username
		password = parsed.password
		client = MongoClient(mongo_url)
		db = client.heroku_app14400075
		ham = db.Ham
		hamTitles = db.hamTitles
		response = {}
		for el in list(ham.find()): #pull the ham histogram and send it as a json response
			response[el["word"]] = el["count"]
		for count in list(hamTitles.find()):
			response["titleCount"] = count['count']
		
		self.write(
			json.dumps(
				response
				)
			)

	def post(self):
		title = self.get_argument("title")
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		parsed = urlsplit(mongo_url)
		db_name = parsed.path[1:]
		username = parsed.username
		password = parsed.password
		client = MongoClient(mongo_url)
		db = client.heroku_app14400075
		ham = db.Ham
		hamTitles = db.hamTitles
		query = helpers.formatQuery(title)
		for word in query: #add new words to ham histogram, increment the count as well
			ham.update({"word":word}, {"$inc": {"count":1} }, upsert=True)
		hamTitles.update({"titleCount":"count"}, {"$inc": {"count":1} }, upsert=True)
		
		"""
		Next class is the same as HAM but for the spam histogram
		"""
class Spam(tornado.web.RequestHandler):
	def get(self):
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		parsed = urlsplit(mongo_url)
		db_name = parsed.path[1:]
		username = parsed.username
		password = parsed.password
		client = MongoClient(mongo_url)
		db = client.heroku_app14400075
		spam = db.Spam
		spamTitles = db.SpamTitles
		response = {}
		for el in list(spam.find()):
			response[el["word"]] = el["count"]
		for count in list(spamTitles.find()):
			response["titleCount"] = count['count']
		self.write(
			json.dumps(
				response
				)
			)

	def post(self):
		title = self.get_argument("title")
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		parsed = urlsplit(mongo_url)
		db_name = parsed.path[1:]
		username = parsed.username
		password = parsed.password
		client = MongoClient(mongo_url)
		db = client.heroku_app14400075
		spam = db.Spam
		spamTitles = db.SpamTitles
		query = helpers.formatQuery(title)
		for word in query:
			spam.update({"word":word, "title":title}, {"$inc": {"count":1} }, upsert=True)
		spamTitles.update({"titleCount":"count"}, {"$inc": {"count":1} }, upsert=True)
		

class Filter(tornado.web.RequestHandler):
	def get(self):
		self.render("spam.html")


handlers = [
    (r"/", MainHandler),
    (r"/ham", Ham),
    (r"/spam", Spam),
    (r"/filter", Filter),
    (r"/reddit", RedditHandler),
    (r"/techcrunch", TechCrunch),
    (r"/metafilter", Metafilter),
    (r"/slashdot", SlashDot),
    (r"/digg", Digg),
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

