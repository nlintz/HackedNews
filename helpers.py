from pyquery import PyQuery as pq
from pymongo import MongoClient

def histogram(lst): #simple histogram generator
	hist = {}
	for word in lst:
		count = hist.setdefault(word, 0)
		hist[word] = count+1
	return hist

def makeTitleHist(): #makes a histogram of lowercase words in an article title
	hn = pq(url='https://news.ycombinator.com/')
	anchors = hn("td.title > a")
	articleText = map(lambda x: x.lower(), anchors.text().split(' '))

	articleTextHist = histogram(articleText)
	return articleTextHist

def getTitles(): #scrapes hacker news for article titles
	hn = pq(url='https://news.ycombinator.com/')
	anchors = hn("td.title > a")
	titles = [anchor.text for anchor in anchors]
	return titles

def formatQuery(articleName): #makes sure that the words that will be put into the dict are all lower case
	query = articleName.split(' ')
	query_lower = [q.lower() for q in query]
	return query_lower

def main():
	print getTitles()


if __name__ == "__main__":
	main()