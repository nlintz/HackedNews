$(document).ready(function() {
	hamHandler();
});

function getHamHandler(){
	colorAjax();

}

function postHamHandler(){

}

function hamHandler(){
	$.getJSON('/Ham', function(data) {
  		prob = data
  		console.log(prob);
  		colorLabels(prob);
  		assignPercents(prob);
	});
}