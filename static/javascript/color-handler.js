$(document).ready(function() {
	colorHandler();
});

function colorHandler(){
	colorAjax();

}

function colorAjax(){
	$.get('/colorHandler', function(data) {
  		prob = $.parseJSON(data)
  		console.log(prob)
	});
}