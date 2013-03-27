from pyquery import PyQuery as pq
from helpers import *

def naiveBayes(spam, ham, query):
	"""
	spam = dict of spam words
	ham = dict of ham words
	query = list of words
	"""
	spamSize = sum(spam.values())
	hamSize = sum(ham.values())
	P_article_spam = 1
	P_article_not_spam = 1
	for word in query:
		P_article_spam = P_article_spam*(spam.get(word, 0)/float(spamSize))
		P_article_not_spam = P_article_not_spam*(ham.get(word, 0)/float(hamSize))

	P_spam = float(spamSize)/(spamSize+hamSize)
	P_not_spam = 1 - P_spam

	P_article_spam += .001
	P_article_not_spam += .001
	P_article = P_article_spam * P_spam + P_article_not_spam * P_not_spam
	# print P_not_spam
	P_spam_article = float(P_article_spam*P_spam)/P_article
	return P_spam_article


def main():
	# spam = histogram('i like cheese i like freeze'.split(' '))
	# ham = histogram('i like sneeze'.split(' '))
	spam = {u'outdoor': 1, u'revamped': 1, u'just': 1, u'show': 2, u'text': 1, u'celebrities': 1, u'symbols': 1, u'thanks': 1, u'filters': 1, u'startups': 1, u'cyprus': 1, u'before': 1, u'perfect': 1, u'(yc': 1, u'flask': 1, u'ships': 1, u'3': 1, u'better': 1, u'to': 5, u'theme': 1, u'helps': 1, u'under': 1, u'wireless:': 1, u'chess': 1, u'do': 3, u'postgres': 1, u'python': 1, u'between': 1, u'"completed"': 1, u'maxstagram': 1, u'facebook': 1, u'hands': 1, u'world': 3, u'nasty': 1, u'password': 1, u'day': 1, u'school': 1, u'success': 1, u'level': 1, u'companies': 1, u'race': 1, u'side': 1, u'mandatory': 1, u'instagram': 1, u'kindleberry': 1, u'senate': 1, u'a': 8, u'mirror': 1, u'close': 1, u'index': 1, u'for': 1, u'space': 1, u'integration': 1, u'launch': 1, u'fans': 1, u'369': 1, u'bleeding': 1, u'swartz': 1, u'issue': 1, u'bought': 1, u'scientific': 1, u'javascript': 2, u'poll:': 1, u'statistics': 1, u'armenia': 1, u'super': 1, u'by': 1, u'change': 1, u'improve': 1, u'accident': 1, u'getting': 1, u'demystified': 1, u'of': 2, u'could': 1, u'losses': 1, u'experience': 1, u'keep': 1, u'chrome': 1, u'became': 1, u'corrupting': 1, u'first': 1, u'for...?': 1, u'fundraising': 1, u'retailer': 1, u'negative': 1, u'you\xe2\x80\x99re': 1, u'learning': 2, u'force': 1, u'tools': 1, u'your': 1, u'portable': 1, u'use': 1, u'start-up,': 1, u'from': 1, u'deal': 1, u'rivals': 1, u'introduction': 1, u'data': 1, u'aaron': 1, u'next': 1, u'their': 1, u'too': 1, u'mothball': 1, u'500': 1, u'more': 1, u'w13)': 1, u'flat': 1, u'knows': 1, u'gay': 1, u'that': 1, u'prizeo': 1, u'with': 1, u'charity': 1, u'case': 1, u'logos': 1, u'tank': 1, u'inside': 1, u'database': 1, u'cracker': 1, u'hackstation': 1, u'project': 2, u'ui': 1, u'country': 1, u'fleet': 1, u'my': 3, u'nabokov': 1, u'sublime': 1, u'and': 5, u'shark': 1, u'tap': 1, u'almost': 1, u'minutes': 1, u'is': 3, u'ram': 1, u'an': 3, u'say': 1, u'at': 1, u'in': 4, u'need': 1, u'devtools': 1, u'counting': 1, u'bank,': 1, u'make': 1, u'-': 2, u'machine': 1, u'how': 2, u'take': 1, u'online': 1, u'you': 2, u'hn:': 2, u'mega-tutorial': 1, u'nginx?': 1, u'advice': 1, u'firetruck': 1, u'mario': 1, u'fast-growing': 1, u'visa': 1, u'massachusetts': 1, u'gal,': 1, u'weekend': 1, u'why': 1, u'ghost': 1, u'\xe2\x80\x93': 2, u'meditate?': 1, u'i': 3, u'oracle': 1, u'the': 10}
	ham = spam
	query = 'revamped'.split(' ')
	print naiveBayes(spam, ham, query)

if __name__ == "__main__":
	main()