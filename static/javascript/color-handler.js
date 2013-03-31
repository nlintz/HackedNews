$(document).ready(function() {
	colorHandler();
});

function colorHandler(){
	colorAjax();

}

function colorAjax(){
	$.getJSON('/posterior', function(data) {
  		prob = data
  		console.log(prob);
  		colorLabels(prob);
  		assignPercents(prob);
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