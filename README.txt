Hacked News
Nathan Lintz & Abe Kim
AI SPRING 2013

High Level Overview:
This project uses machine learning to determine if an article you are interested in reading is likely to interest you or not. We scrape a number of websites for their articles and have users upvote or downvote articles based on whether or not they like them. This data is stored and used to predict the likelihood that a user will like a given article they haven't read yet.

Modules:
	static:
	CSS:
		The css is pretty straightforward. Just a small modification to bootstrap default
	Javascript:
		We built our api on the requireJS interface to improve modularization and reusability
		-bayes.js = computes bayes and bayes with laplacian smoothing to determine if an article will be liked or not
		-color-handler = assigns colors to each label based on whether an article is good or not
		-main.js = bootstraps the application and initializes all bindings
		-percents.js = similar to the color handler but instead of coloring labels, puts percentages in the third column of our website so users know how likely it is that they will enjoy an article
		-postTitle.js = simple script used to prepopulate our DB
		-require-jquery.js = we use the requireJS API to ensure our code is clean. This build comes bundled with jquery :-)
		-voteAjax = handles ajax calls to the backend when the user upvotes or downvotes an article

	Templates:
		HTML for all of our views

	Python
		-dbReset.py = testing script so we can easily wipe and reinitialize our database
		-hackedNews.py = controller for our site. This stores the routes for ajax calls to the database and get requests for the views
		-helpers.py = a bunch of nice helpers to make our views neater
		-naiveBayes.py = server side implemetnation of bayes theorem in case the user disables javascript in their browser
		-scrape.py = handles all scraping for websites e.g. hackernews, reddit, metafilter etc...
		-ui_methods.py = frontend methods so we can call python in our html