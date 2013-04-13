require(["jquery", "jquery.vote-handler", "color-handler"], function($, voteHandler, colorHandler) {
    $().voteHandler(); //Binds vote buttons to ajax calls
    colorHandler.colorLabels(); //Sets up colors when pages loads
    $('.btn-up').bind("click", function() {
    	colorHandler.colorLabels();
    	alert('update')
	});
	$('.btn-down').bind("click", function() {
    	colorHandler.colorLabels();
	});
});