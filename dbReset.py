import os
from pymongo import MongoClient

def wipeDB(): #Used for DB testing
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017') #create a connection
	client = MongoClient(mongo_url)
	db = client.heroku_app14400075
	ham = db.Ham
	hamTitles = db.hamTitles
	spam = db.Spam
	spamTitles = db.SpamTitles
	"""
	Kill DB
	"""
	ham.remove()
	hamTitles.remove()
	spam.remove()
	spamTitles.remove()

def wipeHam(): #same thing as above except for the Ham dict
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
	client = MongoClient(mongo_url)
	db = client.heroku_app14400075
	ham = db.Spam
	ham.remove()

def wipeSpam(): #same thing as above except for the spam dict
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
	client = MongoClient(mongo_url)
	db = client.heroku_app14400075
	spam = db.Spam
	spam.remove()

def main():
	wipeDB()

if __name__ == "__main__":
	main()