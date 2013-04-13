$.fn.bayes = function() {
	$.get('/ham', function(data) {
  	ham = data
  	$.get('/spam', function(data) {
  	spam = data
  	return b(ham,spam)
		});
	});
	var b = function(ham,spam){
		return [ham,spam];
	};
}