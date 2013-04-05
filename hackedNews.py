import os
import os.path
import sys
import pymongo
import dbConfig
sys.path.append( "PickleMonger" )
from PickleMonger.PickleMonger import PickleMonger
import tornado.ioloop
import tornado.web
import scrape
import naiveBayes
import helpers
import json
import ui_methods

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
    	print os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
    	db_name = "bayesDict"
    	connection = pymongo.Connection(mongo_url)
    	ham = connection.Ham
    	test = connection.Spam

    	dbConfig.dbSetup()
    	titleLinkAssoc = scrape.scrapeHN()
        self.render("home.html",
        titleLinks = titleLinkAssoc,
        voteHandler = "/static/javascript/vote-handler.js" )
    
    def post(self):
		PM = PickleMonger('bayesDict.dat')

		args = [self.get_arguments("articleName"),self.get_arguments("voteType")]
		articleName = args[0][0]
		voteType = str(args[1][0])
		query = helpers.formatQuery(articleName)
		ham = PM.read_allInstances('ham')
		spam = PM.read_allInstances('spam')
		if voteType == "up":
			for word in query:
				ham.wordCountDict.setdefault(word, 0)
				ham.wordCountDict[word] = ham.wordCountDict[word] + 1

		if voteType == "down":
			for word in query:
				spam.wordCountDict.setdefault(word, 0)
				spam.wordCountDict[word] = spam.wordCountDict[word] + 1

		PM.updateObject(ham)
		PM.updateObject(spam)

		print "spam liklihood: " + str(naiveBayes.naiveBayes(spam.wordCountDict, ham.wordCountDict, query))

class Ham(tornado.web.RequestHandler):
	def get(self):
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		db_name = "bayesDict"
		connection = pymongo.Connection(mongo_url)
		ham = connection.Ham
		response = {}
		for el in list(ham.find()):
			response[el["word"]] = el["count"]
		self.write(
			json.dumps(
				response
				)
			)

	def post(self):
		title = self.get_arguments("title")
		mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
		db_name = "bayesDict"
		connection = pymongo.Connection(mongo_url)
		ham = connection.Ham
		query = helpers.formatQuery(title)
		for word in query:
			ham.update({"word":word}, {"$inc": {"count":1} }, upsert=True)
		
		# ham.update({user_id:1}, {$set:{text:"Lorem ipsum", updated:new Date()}, $inc:{count:1}}, true, false)

class PosteriorHandler(tornado.web.RequestHandler):
	def get(self):
		PM = PickleMonger('bayesDict.dat')
		ham = PM.read_allInstances('ham').wordCountDict
		spam = PM.read_allInstances('spam').wordCountDict
		
		titleProbDict = {}
		titles = helpers.getTitles()
		for title in titles:
			key = ''.join(title.split())
			query = helpers.formatQuery(title)
			titleProbDict[key] = str(naiveBayes.naiveBayes(spam, ham, query))

		self.write(
			json.dumps(
				titleProbDict
				)
			)



handlers = [
    (r"/", MainHandler),
    (r"/posterior", PosteriorHandler),
    (r"/Ham", Ham),
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

