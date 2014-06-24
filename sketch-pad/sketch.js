$(document).ready(function() {



	function makeGrid(n) {
		var grid = $('#container');
		for (var i = 1;i<=n; i++) {
			for (var j = 1; j <= n; j++){
				grid.append("<div class='square'></div>");
			}
			grid.append("<div class='new_row'></div>");
		}
	};

	$('.square').hover(function() {
	$(this).addClass('hover');
	
	});

	

	
	

	makeGrid(4);
			


});
