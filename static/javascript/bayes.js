//Bayesian computation, first without laplacian smoothing, second with laplacian smoothing
define([], function() {
	function bayes(titleArray, ham, spam){
		hamSize = 0;
		spamSize = 0;
		for (key in ham){
			hamSize += ham[key];
		}
		for (key in spam){
			spamSize += spam[key];
		}
		P_spam = spamSize/(spamSize + hamSize); //The probability that an article is spam is the total amount of spam/dictionary size
		P_ham = hamSize/(spamSize + hamSize) //Above logic is the same

		P_title_spam = 1;
		P_title_ham = 1;
		//Compute the conditionally independent likelihood of an article being ham or spam by mulitplying the frequency of each word  in the dict 
		for (index in titleArray){
			var word = titleArray[index];
			var spamProb = spam[word] || 0;
			var hamProb	= ham[word] || 0; 
			P_title_spam *= (spamProb/spamSize)
			P_title_ham *= (hamProb/hamSize)
		}
		var P_spam_title = (P_title_spam * P_spam)/(P_title_spam * P_spam + P_title_ham * P_ham);
		if(isNaN(P_spam_title)){
			return .5;
		}
		return P_spam_title
	}

	function laplacianBayes(titleArray, ham, spam){
		k = 1; //laplacian coefficient = 1
		hamSize = 0; //total number of word occurences
		hamCount = 0; //total number of unique words
		spamSize = 0; 
		spamCount = 0; 
		hamTitleCount = ham['titleCount'];//total number of articles
		spamTitleCount = spam['titleCount'];//total number of articles
		for (key in ham){
			hamSize += key == 'titleCount' ? 0 : ham[key];
			hamCount += key == 'titleCount' ? 0 : 1;
		}
		for (key in spam){
			spamSize += key == 'titleCount' ? 0 : spam[key];
			spamCount += key == 'titleCount' ? 0 : 1;
		}
		P_spam = (spamTitleCount+k)/(spamTitleCount + hamTitleCount + k*2); // probability of spam is the total amount of spam articles/total number of articles
		P_ham = (hamTitleCount+k)/(spamTitleCount + hamTitleCount + k*2); //k*2 classes (spam, ham)

		P_title_spam = 1;
		P_title_ham = 1;
		for (index in titleArray){
			var word = titleArray[index];
			var spamProb = spam[word] || 0;
			var hamProb	= ham[word] || 0; 
			P_title_spam *= ((spamProb+k)/(spamSize+k*spamCount))
			P_title_ham *= ((hamProb+k)/(hamSize+k*hamCount))
		}

		var P_spam_title = (P_title_spam * P_spam)/(P_title_spam * P_spam + P_title_ham * P_ham);
		return P_spam_title
	}
	return{
		bayes:laplacianBayes
	}
});