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
		P_spam = spamSize/(spamSize + hamSize);
		P_ham = hamSize/(spamSize + hamSize)

		P_title_spam = 1;
		P_title_ham = 1;
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
	return{
		bayes:bayes
	}
});