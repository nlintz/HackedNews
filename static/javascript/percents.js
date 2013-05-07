define(["jquery", "bayes"], function($, bayes) {
	// gets all percents from the database and puts it into the right column
	function assignPercents(ham, spam){
		$('.likelihood-spam').each(function( index ) {
			title = $(this).data('title');
			title = title.toLowerCase();
			splitTitle = title.split(" ");
			var probTitle = bayes.bayes(splitTitle, ham, spam);
			percentTitle = String(probTitle*100);
			percentTitleSigDigits = percentTitle.substring(0,4)+"%";
			$(this).text(percentTitleSigDigits);
		});
	}
	return{
		assignPercents:assignPercents
	}
})