define(["jquery","voteAjax"], function($,voteAjax) {
	function postAllTitles(){
		$('.label').each(function( index ) {
			title = $(this).data('title');
			voteAjax.voteAjax(title, "up");
			voteAjax.voteAjax(title, "down");
			console.log(title+" was added to db");
		})

	}
	return {
		postAllTitles:postAllTitles
	}

})