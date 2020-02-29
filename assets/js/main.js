function process() {
const player = document.getElementById('vid');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const constraints = {video: true,};
context.drawImage(player, 0, 0, canvas.width, canvas.height);
navigator.mediaDevices.getUserMedia(constraints)
	.then((stream) => {
		player.srcObject = stream;
	});
console.log(canvas.toDataURL());
}

function start() {
	canvas.style.visibility="hidden";
	window.setInterval(function() {
		process();
	}, 1000);
}
