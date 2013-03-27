$(document).ready(function() {
	voteHandler();
	console.log('dom ready')

});

function voteHandler(){
	$('.btn-up').click(function() {
	upVotedArticle = $(this).closest("a").text();
	console.log($(this))
  	voteAjax(upVotedArticle, "up");
	});

	$('.btn-down').click(function() {
	downVotedArticle = $(this).parent().siblings("a").text();
  	voteAjax(downVotedArticle, "down");
	});

}

function voteAjax(articleName, voteType){
	$.post("/", { articleName: articleName, voteType: voteType } );
}