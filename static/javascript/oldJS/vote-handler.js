define({
	color: "black"
	});

// $(document).ready(function() {
// 	voteHandler();

// });

function voteHandler(){
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
	$.post("/", { articleName: articleName, voteType: voteType } );
}