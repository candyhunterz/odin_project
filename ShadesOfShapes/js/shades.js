$(document).ready(function() {

	// init game constants
	var board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	var row1, row2, row3, row4, row5, col1, col2, col3, col4, col5, leftDiag, rightDiag;

	//function to randomize the colors of the cell
	function randomize() {
		for (var i=0; i<board.length; i++) {
			var num = Math.floor(Math.random()*3)
			var color='';
			board[i] = 0;
			if (num == 0) {
				color = 'red';
			}
			else if (num == 1) {
				color = 'blue';	
			}
			else if (num == 2) {
				color = 'yellow';
			}
			$("#d"+i).css({backgroundColor: color});
		}
		$("#choice td").css({backgroundColor: color});
	}

	// initialize game state
	function setColor() {
		
		randomize();
	}
	//function to return the color of selection box
	function getChoiceColor() {
		$("#choice td").css("background-color")

	}


	// function to get the color of a clicked cell
	$("td").click(function() {
		var color = $(this).css("background-color");
		var choiceColor = $("#choice td").css("background-color")
		if (color === choiceColor) {
			$(this).css({backgroundColor: '#FFFFFF'})
		}
		console.log(color);
	})

	
	$("#restart").click(function() {
		setColor();

	})

	$("#timed").click(function() {
		setColor();
		for (var i=0; i<board.length; i++) {
			$("#d" + i).animate({
				opacity: 0}, 5000, function() {

				});

			
		}

	})



setColor();

});

