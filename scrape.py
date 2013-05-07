from pyquery import PyQuery as pq
from helpers import *

def scrapeHN(): #scrapes hacker news for their articles and urls to said articles
	hn = pq(url='http://news.ycombinator.com/')
	anchors = hn("td.title > a")
	titleLinkAssoc = {}
	for anchor in anchors:
		if anchor.text == "More":
			continue
		titleLinkAssoc[anchor.text] = anchor.attrib['href']

	links = [anchor.attrib['href'] for anchor in anchors]
	filteredLinks = filter(lambda x: 'http' in x, links)
	titles = [anchor.text for anchor in anchors]

	return titleLinkAssoc

def scrapeReddit(): #same as above for reddit
	reddit = pq(url='http://www.reddit.com/')
	anchors = reddit("p.title > a")
	titleLinkAssoc = {}
	for anchor in anchors:
		if anchor.text == "More":
			continue
		titleLinkAssoc[anchor.text] = anchor.attrib['href']

	links = [anchor.attrib['href'] for anchor in anchors]
	filteredLinks = filter(lambda x: 'http' in x, links)
	titles = [anchor.text for anchor in anchors]
	return titleLinkAssoc

def scrape(url, hook): #same as above but modularized for any website
	"""
	url = website url
	hook = parent selector of link
	"""
	scrape = pq(url)
	anchors = scrape(hook)
	titleLinkAssoc = {}
	for anchor in anchors:
		if anchor.text == "More":
			continue
		titleLinkAssoc[anchor.text] = anchor.attrib['href']

	links = [anchor.attrib['href'] for anchor in anchors]
	filteredLinks = filter(lambda x: 'http' in x, links)
	titles = [anchor.text for anchor in anchors]
	return titleLinkAssoc

	
def main():
	# print scrape('http://www.digg.com/', 'h2.headline > a')
	print scrapeReddit()

if __name__ == "__main__":
	main()
