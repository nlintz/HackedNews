$.fn.voteHandler = function() {
	var voteHandler = function(){
	$('.btn-up').bind("click", function() {
	upVotedArticle = $(this).data('title');
  	voteAjax(upVotedArticle, "up");
		});

	$('.btn-down').click(function() {
	downVotedArticle = $(this).data('title');
  	voteAjax(downVotedArticle, "down");
		});
	}

	function voteAjax(articleName, voteType){
		if(voteType=="up"){
			$.post("/Ham", { title: articleName } );
		}
		if(voteType=="down"){
			alert('downvote')
		}
	
	}

    return voteHandler();
};