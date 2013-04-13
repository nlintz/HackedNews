$.fn.colorHandler = function() {
	function getHam(){
		$.ajax({
        url: '/ham',
        type: 'get',
        dataType: 'json',
        async: false,
        success: function(data) {
            result = data;
        }
     });
     return result;

	}
	function getSpam(){
		$.ajax({
        url: '/spam',
        type: 'get',
        dataType: 'json',
        async: false,
        success: function(data) {
            result = data;
        }
     });
     return result;
 	}

	var colorLabels = function(){
		ham = getHam();
		spam = getSpam();
		$('.label').each(function( index ) {
			title = $(this).data('title');
			title = title.toLowerCase();
			splitTitle = title.split(" ");
			var probTitle = bayes(splitTitle,ham,spam);
			if (probTitle < .5){
				$(this).toggleClass("label-info", true);
				$(this).toggleClass("label-important", false);
				$(this).text('Ham');
				}
			else if (probTitle > .5){
				$(this).toggleClass("label-info", false);
				$(this).toggleClass("label-important", true);
				$(this).text('Spam');
				}
			else{
				$(this).text('Unsure');
			}
		})
	}

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
		return P_spam_title
	}
	colorLabels()
}