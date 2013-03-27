$(document).ready(function() {
	voteHandler();

});

function voteHandler(){
	$('.btn-up').bind("click", function() {
	upVotedArticle = $(this).data('title');
  	voteAjax(upVotedArticle, "up");
  	colorHandler();
	});

	$('.btn-down').click(function() {
	downVotedArticle = $(this).data('title');
  	voteAjax(downVotedArticle, "down");
  	colorHandler();
	});

}

function voteAjax(articleName, voteType){
	$.post("/", { articleName: articleName, voteType: voteType } );
}