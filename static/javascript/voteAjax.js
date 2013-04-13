define(["jquery"], function($) {
  function voteAjax(articleName, voteType){
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
