from pyquery import PyQuery as pq
from helpers import *

def scrapeHN():
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

def scrapeReddit():
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

def scrape(url, hook):
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
	print scrape('http://www.digg.com/', 'h2.headline > a')

if __name__ == "__main__":
	main()
