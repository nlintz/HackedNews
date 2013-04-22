$.fn.voteHandler = function() {
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