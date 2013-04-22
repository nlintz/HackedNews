require(["jquery", "jquery.vote-handler", "color-handler", "postTitle"], function($, voteHandler, colorHandler, postTitle) {
	// postTitle.postAllTitles();
    $().voteHandler(); //Binds vote buttons to ajax calls
    colorHandler.colorLabels(); //Sets up colors when pages loads
    $('.btn-up').bind("click", function() {
		colorHandler.colorLabels();
	});
	$('.btn-down').bind("click", function() {
		colorHandler.colorLabels();
	});
	$('a').bind("click", function() {
		colorHandler.colorLabels();
	});
});