$(document).ready(function() {


	// make a square grid based on user input
	function makeGrid(n) {
		var grid = $('#container');
		for (var i = 1;i<=n; i++) {
			for (var j = 1; j <= n; j++){
				grid.append("<div class='square'></div>");
			}
			grid.append("<div class='new_row'></div>");
		}
	};

	// change color of each square on hover
	$(document).on('mouseenter','.square',function() {
        $(this).addClass('hover');
    });
	

	$('#button').click(function() {
		buttonClick();

	});


	function buttonClick() {
		var input = +window.prompt('enter a number for a square canvas (AxA)');
		$('.square').remove();
		$('.new_row').remove();
		makeGrid(input);
		console.log(input);
	}


	makeGrid(50);
			


});
