define(["jquery","voteAjax"], function($,voteAjax) {
	// test script written to populate the db
	function postAllTitles(){
		$('.label').each(function( index ) {
			title = $(this).data('title');
			voteAjax.voteAjax(title, "up");
			voteAjax.voteAjax(title, "down");
		});
	}
	return {
		postAllTitles:postAllTitles
	};

});