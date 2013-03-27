$(document).ready(function() {
	colorHandler();
});

function colorHandler(){
	colorAjax();

}

function colorAjax(){
	$.get('/colorHandler', function(data) {
  		prob = $.parseJSON(data);
  		colorLabels(prob);
	});
}

function colorLabels(prob){
	$('.label').each(function( index) {

	});
}