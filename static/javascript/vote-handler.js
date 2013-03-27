$(document).ready(function() {
	voteHandler();
	voteAjax("bull shit is going down", "down");
});

function voteHandler(){
	$('.icon-thumbs-up').click(function() {
	upVotedArticle = $(this).siblings("a").text();
  	voteAjax(upVotedArticle, "up");
	});

	$('.icon-thumbs-down').click(function() {
	downVotedArticle = $(this).siblings("a").text();
  	voteAjax(downVotedArticle, "down");
	});

}

function voteAjax(articleName, voteType){
	$.post("/", { articleName: articleName, voteType: voteType } );
}