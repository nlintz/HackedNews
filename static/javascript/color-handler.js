define(["jquery","percents","bayes"], function($, percents,bayes) {
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
		var ham = getHam();
		var spam = getSpam();
		$('.label').each(function( index ) {
			title = $(this).data('title');
			title = title.toLowerCase();
			splitTitle = title.split(" ");
			var probTitle = bayes.bayes(splitTitle, ham, spam);
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
				$(this).toggleClass("label-info", false);
				$(this).toggleClass("label-important", false);
				$(this).text('Unsure');
			}
		})
		percents.assignPercents(ham, spam)

	}

	return {
		colorLabels:colorLabels,
	}
});