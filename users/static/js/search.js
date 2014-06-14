var Search = (function($){

	var doActions = function(){
		$("#search-user").parent().on("keyup","#search-user",function(){
			console.log("vish");

			var data = {};
			data.nameUser = $("#search-user").val();

			$.ajax({
			  url: "/usuarios/busca/",
			  contentType: "application/json",
			  data : JSON.stringify(data),
			  type : "POST",
			  success : function(ret){
			  	console.log(ret);
			  }
			});
			});
	};

	var init = function(){
		doActions();
	};

	return{
		init : init
	}
})(jQuery);

$(document).ready(function(){
	Search.init();
});