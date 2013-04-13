require(["jquery", "jquery.vote-handler", "jquery.color-handler","postTitle"], function($, voteHandler, colorHandler, postTitle) {
	postTitle.postAllTitles();
    $().voteHandler(); //Binds vote buttons to ajax calls
    $().colorHandler(); //Sets up colors when pages loads
    $('.btn-up').bind("click", function() {
    	$().colorHandler();
	});
	$('.btn-down').bind("click", function() {
    	$().colorHandler();
	});
});