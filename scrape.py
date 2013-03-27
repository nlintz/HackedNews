from pyquery import PyQuery as pq
from helpers import *

def scrapeHN():
	hn = pq(url='https://news.ycombinator.com/')
	anchors = hn("td.title > a")
	titleLinkAssoc = {}
	for anchor in anchors:
		titleLinkAssoc[anchor.text] = anchor.attrib['href']

	links = [anchor.attrib['href'] for anchor in anchors]
	filteredLinks = filter(lambda x: 'http' in x, links)
	titles = [anchor.text for anchor in anchors]

	return titleLinkAssoc



	
def main():
	print scrapeHN()

if __name__ == "__main__":
	main()
