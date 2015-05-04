
window.onload = function() {

	
	var c = document.getElementById("myDrawing");
	var ctx = c.getContext("2d");
	var radius = 5;
	var y = 70;
	var flag = false;
/*	c.addEventListener("mousemove", mouseMoved);
	ctx.fillText("Put mouse here", 10, 10);
*/
	function drawHouse() {


		// draw the background
		ctx.beginPath();
		ctx.rect(0, 0, c.width, c.height/2 + 20);
		ctx.fillStyle = "#afeeee";
		ctx.fill();
		ctx.stroke();

		// draw the grass
		ctx.beginPath();
		ctx.rect(0, c.height/2 + 20, c.width, 130);
		ctx.fillStyle = "#6dc066";
		ctx.fill();
		ctx.stroke();
		
		// The front of the roof
		ctx.fillStyle = '#468499';
		
		ctx.beginPath();
		ctx.moveTo(85, 145);
		ctx.lineTo(140,100);
		//ctx.moveTo(140, 100);
		ctx.lineTo(190,150);
		//ctx.moveTo(190, 150);
		ctx.lineTo(85,145);
		ctx.closePath();
		//ctx.lineWidth = 3;
		
		ctx.stroke();
		ctx.fill();

		// The rest of the roof
		ctx.fillStyle = '#0099cc';
		ctx.beginPath();
		ctx.moveTo(140, 100);
		ctx.lineTo(200,83);
		//ctx.moveTo(200, 83);
		ctx.lineTo(245,115);
		//ctx.moveTo(245, 115);
		ctx.lineTo(190,150);
		//ctx.moveTo(190, 150);
		ctx.lineTo(140,100);
		ctx.closePath();
		//ctx.lineWidth = 3;
		
		ctx.stroke();
		ctx.fill();

		// the front of the house
		ctx.fillStyle = '#d7c797';
		ctx.beginPath();
		ctx.moveTo(105, 147);
		ctx.lineTo(170, 150);
		ctx.lineTo(170, 220);
		ctx.lineTo(105, 215);
		ctx.lineTo(105, 147);
		ctx.closePath();

		ctx.stroke();
		ctx.fill();

		// the rest of the house
		ctx.fillStyle = '#f2e2cd';
		ctx.beginPath();
		ctx.moveTo(170, 150);
		ctx.lineTo(190, 150);
		ctx.lineTo(234, 122);
		ctx.lineTo(234, 197);
		ctx.lineTo(170, 220);

		ctx.stroke();
		ctx.fill();

		// the chimney
		ctx.fillStyle = '#2e5678';
		ctx.beginPath();
		ctx.moveTo(175, 110);
		ctx.lineTo(175, 80);
		ctx.lineTo(186, 80);
		ctx.lineTo(185, 110);
		ctx.lineTo(175, 110);

		ctx.stroke();
		ctx.fill();
	}

	

	function drawSmoke() {
		
		
		//ctx.clearRect(160, 0, 40, 80);

		ctx.beginPath();
		ctx.arc(180, y, radius, 0, 2 * Math.PI, false);
		ctx.fillStyle = "#888888";
		ctx.fill();
		if (y < 0) {
			resetY();
		}
		
		animateSmoke();

	}

	function animateSmoke() {
		y -= 0.2;
		radius += 0.03;
	}

	function resetY() {
		ctx.clearRect(160, 0, 40, 80);
		ctx.beginPath();
		ctx.rect(160, 0, 40, 80);
		ctx.fillStyle = "#afeeee";
		ctx.strokeStyle = "#afeeee";
		ctx.fill();
		ctx.stroke();
		
		y = 70;
		radius = 5;
	}



	
		
	// this function determines the coordinates of the mouse relative to the canvas
/*	function mouseMoved(e) {
    ctx.clearRect(0, 0, c.width, 40);
    
    ctx.fillText(["From upper left:",
                      e.clientX - (c.offsetLeft - window.pageXOffset),
                      e.clientY - (c.offsetTop - window.pageYOffset)],
                     10,
                     10);
    
     ctx.fillText(["From upper right:",
                     c.width - (e.clientX - c.offsetLeft) - window.pageXOffset,
                     e.clientY - (c.offsetTop - window.pageYOffset)],
                     10,
                     30);
	}
*/


	// draw the house and animate
	drawHouse();
	setInterval(drawSmoke, 10);




	


 }