$.fn.voteHandler = function() {
	//Jquery addon implementation of rthe voteAjax. Used if the user doesn't want to implement the require js api
	var voteHandler = function(){

	$('a').bind("click", function() {
		upVotedArticle = $(this).data('title');
		voteAjax(upVotedArticle, "up");
		});

	$('.btn-up').bind("click", function() {
	upVotedArticle = $(this).data('title');
	voteAjax(upVotedArticle, "up");
		});

	$('.btn-down').click(function() {
	downVotedArticle = $(this).data('title');
	voteAjax(downVotedArticle, "down");
		});
	};

	function voteAjax(articleName, voteType){
		if(voteType=="up"){
			$.post("/ham", { title: articleName } );
		}
		if(voteType=="down"){
			$.post("/spam", { title: articleName } );
		}
	
	}

    return voteHandler();
};