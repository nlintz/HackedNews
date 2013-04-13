import os
from pymongo import MongoClient

def wipeDB():
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
	db_name = "bayesDict"
	client = MongoClient(mongo_url)
	db = client.db_name
	ham = db.Ham
	spam = db.Spam
	ham.remove()
	spam.remove()

def wipeHam():
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
	db_name = "bayesDict"
	client = MongoClient(mongo_url)
	db = client.db_name
	ham = db.Spam
	ham.remove()

def wipeSpam():
	mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
	db_name = "bayesDict"
	client = MongoClient(mongo_url)
	db = client.db_name
	spam = db.Spam
	spam.remove()

def main():
	wipeDB()

if __name__ == "__main__":
	main()