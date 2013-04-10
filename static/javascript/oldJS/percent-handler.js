function assignPercents(likelihoods){
	$('.likelihood-spam').each(function( index ) {
		title = $(this).data('title');
		probTitle = prob[title];
		percentTitle = String(probTitle*100);
		percentTitleSigDigits = percentTitle.substring(0,4)+"%";
		$(this).text(percentTitleSigDigits);
	});
}