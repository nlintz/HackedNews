$(document).ready(function() {
	colorHandler();
});

function colorHandler(){
	colorAjax();

}

function colorAjax(){
	$.getJSON('/colorHandler', function(data) {
		// console.log('colorAjax')
  		prob = data
  		console.log(prob);
  		colorLabels(prob);
	});
}

function colorLabels(prob){
	$('.label').each(function( index ) {
		title = $(this).data('title');
		probTitle = prob[title]
		if (probTitle < .5){
			$(this).toggleClass("label-info", true);
			$(this).toggleClass("label-important", false);
			$(this).text('Ham');
		}
		else {
			$(this).toggleClass("label-info", false);
			$(this).toggleClass("label-important", true);
			$(this).text('Spam');
		}
	});
}