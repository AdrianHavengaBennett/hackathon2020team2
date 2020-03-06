$ ( document ).on ( "click", "#image", function () {
	
	var content_div = $(this).data('content_number');
	
	$('.content_'+content_div).toggleClass('d-none')
	
	
});