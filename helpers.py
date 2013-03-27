from pyquery import PyQuery as pq

def histogram(lst):
	hist = {}
	for word in lst:
		count = hist.setdefault(word, 0)
		hist[word] = count+1
	return hist

def makeTitleHist():
	hn = pq(url='https://news.ycombinator.com/')
	anchors = hn("td.title > a")
	articleText = map(lambda x: x.lower(), anchors.text().split(' '))

	articleTextHist = histogram(articleText)
	return articleTextHist

def getTitles():
	hn = pq(url='https://news.ycombinator.com/')
	anchors = hn("td.title > a")
	titles = [anchor.text for anchor in anchors]
	return titles

def main():
	print getTitles()

if __name__ == "__main__":
	main()