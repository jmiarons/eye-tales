navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
if(navigator.getUserMedia) {
	navigator.getUserMedia({video: true}, handleVideo, videoError);
}
function handleVideo (stream) {
	document.querySelector('#vid').src = window.URL.createobjectURL(stream);
}
function videoError(e) {
	alert("There has some problem");
}
