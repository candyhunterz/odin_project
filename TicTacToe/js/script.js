function allowDrop(ev) {
	
	ev.preventDefault();
}



function drag(ev) {
	ev.dataTransfer.setData("Text",ev.target.id);

}

var player1Turn = false;
var player2Turn = false;
var board = [0,0,0,0,0,0,0,0,0];
var row1, row2, row3, col1, col2, col3, leftDiag, rightDiag;
var sum = 0;
var monkeyScore = 0;
var dragonScore = 0;


function drop(ev) {
	ev.preventDefault();
	var data=ev.dataTransfer.getData("Text");
	var nodeCopy = document.getElementById(data).cloneNode(true);
	if (nodeCopy.id == 'drag1') {
		nodeCopy.id = "newId1";
		document.getElementById(ev.srcElement.id).style.backgroundColor="red";	
		player1Turn = true;
		sum += 1;
		//document.getElementById("drag1").setAttribute("draggable", "false");
		board[ev.target.id.charAt(1)] = 1;
		if (player2Turn == false) {
			document.getElementById("drag1").setAttribute("draggable", "false");
			player1Turn = false;
			document.getElementById("drag2").setAttribute("draggable", "true");
		}
	}

	if (nodeCopy.id == 'drag2'){
		nodeCopy.id = "newId2";
		document.getElementById(ev.srcElement.id).style.backgroundColor="blue";
		player2Turn = true;
		sum += 1;
		//document.getElementById("drag2").setAttribute("draggable", "false");
		board[ev.target.id.charAt(1)] = -1;
		if (player1Turn == false) {
			document.getElementById("drag2").setAttribute("draggable", "false");
			player2Turn = false;
			document.getElementById("drag1").setAttribute("draggable", "true");
		} 
	}
     /* We cannot use the same ID */
    ev.target.appendChild(nodeCopy);
    ev.target.setAttribute("ondragover", "false");
	document.getElementById(nodeCopy.id).setAttribute("draggable", "false");
	isWinner(board);
}

function isWinner(board) {
/*	for (var i=0; i<3; i++) {
		row1 += board[i];
		if (row1 == 3 || row1 == -3) {
			
			console.log(board);
		}
	}*/
	row1 = board[0]+board[1]+board[2];
	row2 = board[3]+board[4]+board[5];
	row3 = board[6]+board[7]+board[8];
	col1 = board[0]+board[3]+board[6];
	col2 = board[1]+board[4]+board[7];
	col3 = board[2]+board[5]+board[8];
	leftDiag = board[0]+board[4]+board[8];
	rightDiag = board[2]+board[4]+board[6];
	
	if (row1 == 3 || row2 == 3 || row3 == 3 || col1 == 3 || col2 == 3 || col3 == 3 || leftDiag == 3 || rightDiag == 3) {
		confirm("monkey wins!");
		monkeyScore += 1;
		document.getElementById("monkeyScore").innerHTML = "<h1>" + monkeyScore + "</h1>";
		
		document.getElementById("drag1").setAttribute("draggable", "false");
		document.getElementById("drag2").setAttribute("draggable", "false");
		nextGame();
	} else if (row1 == -3 || row2 == -3 || row3 == -3 || col1 == -3 || col2 == -3 || col3 == -3 || leftDiag == -3 || rightDiag == -3) {
		confirm("dragon wins!");
		dragonScore += 1;
		document.getElementById("dragonScore").innerHTML = "<h1>" + dragonScore + "</h1>";
		
		document.getElementById("drag1").setAttribute("draggable", "false");
		document.getElementById("drag2").setAttribute("draggable", "false");
		nextGame();
	} else if (sum == 9) {
		confirm("Tie!");
		document.getElementById("drag1").setAttribute("draggable", "false");
		document.getElementById("drag2").setAttribute("draggable", "false");
		nextGame();
	}
console.log(sum);
console.log(board);
}

function restart() {
	sum = 0;
	monkeyScore = 0;
	dragonScore = 0;
	document.getElementById("monkeyScore").innerHTML = "<h1>" + monkeyScore + "</h1>";
	document.getElementById("dragonScore").innerHTML = "<h1>" + dragonScore + "</h1>";
	document.getElementById("drag1").setAttribute("draggable", "true");
	document.getElementById("drag2").setAttribute("draggable", "true");
	for (var i=0; i<board.length; i++) {
		board[i] = 0;
		document.getElementById("d" + i).innerHTML = "";
		document.getElementById("d" + i).style.backgroundColor = "#ffffff";
		document.getElementById("d" + i).setAttribute("ondragover", "allowDrop(event)");
	}
}

function nextGame() {
	sum = 0;
	for (var i=0; i<board.length; i++) {
		board[i] = 0;
		document.getElementById("d" + i).innerHTML = "";
		document.getElementById("d" + i).style.backgroundColor = "#ffffff";
		document.getElementById("d" + i).setAttribute("ondragover", "allowDrop(event)");
	}
	document.getElementById("drag1").setAttribute("draggable", "true");
	document.getElementById("drag2").setAttribute("draggable", "true");
}	

