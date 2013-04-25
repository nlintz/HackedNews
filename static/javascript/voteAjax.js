define(["jquery"], function($) {
  function voteAjax(articleName, voteType){
    // if upvote, make an ajax post to the ham url with the article name, otherwise do the same except for the downvote url
    if(voteType=="up"){
      $.post("/ham", { title: articleName } );
    }
    if(voteType=="down"){
      $.post("/spam", { title: articleName } );
    }
  }
  return {
    voteAjax:voteAjax
  }
});
