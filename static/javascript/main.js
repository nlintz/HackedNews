require(["jquery", "jquery.vote-handler", "jquery.color-handler"], function($, voteHandler, colorHandler) {
    $().voteHandler();
    $().colorHandler();

    $('.btn-up').bind("click", function() {
    	$().colorHandler();
	});
	$('.btn-down').bind("click", function() {
    	$().colorHandler();
	});
});