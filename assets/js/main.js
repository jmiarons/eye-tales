var context;
window.addEventListener('load', init, false);

// Global variables
const player = document.getElementById('vid')
const button = document.querySelector('.button');
const audio = document.getElementById('myAudioElement') || new Audio();
var iteration = 1;

// Ajax
function callApi(iteration, sessionId, imageBase64) {
    var formData = {iteration: iteration, session_id: sessionId, image_base64: imageBase64};
    var request = new XMLHttpRequest();
    request.open('POST', 'https://api.eyetales.asuarez.dev/describe', true);
    request.responseType = 'arraybuffer';
    // Decode asynchronously
    request.onload = function() {
        if (request.status == 200) {
            // console.log('something to say')
            context.decodeAudioData(request.response, function(buffer) {
              buf = buffer;
                var source = context.createBufferSource();  // creates a sound source
                source.buffer = buffer;                     // tell the source which sound to play
                source.connect(context.destination);        // connect the source to the context's destination (the speakers)
                source.start(0);                            // play the source now
                                                            // note: on older systems, may have to use deprecated noteOn(time);
            }, function() {
                console.log('error decoding audio');
            });
        } else if (request.status == 204) {
            // console.log('nothing to say');
        } else {
            console.log('error')
        }
    }
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.send(JSON.stringify(formData));
}

// Iterate per image
function process(iteration, sessionId) {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
    imageBase64 = canvas.toDataURL();
    imageBase64 = imageBase64.split(',');
    imageBase64.shift();
    callApi(iteration, sessionId, imageBase64.join());
}

// Main function
function start() {
    button.classList.add('button--loading');
    button.disabled = true;
    button.querySelector('span').innerHTML = 'Loading...';
    const constraints = {video: true,};
    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            player.srcObject = stream;
            button.classList.add('button--hide');
            const sessionId = (Math.floor(Math.random() * (10000 - 1 + 1)) + 1).toString();
            setInterval(function() {
                process(iteration, sessionId);
                ++iteration;
            }, 3000);
        });
}

// Audio init
function init() {
    try {
        // Fix up for prefixing
        window.AudioContext = window.AudioContext||window.webkitAudioContext;
        context = new AudioContext();
    }
    catch(e) {
        alert('Web Audio API is not supported in this browser');
    }
}

button.addEventListener('click', start);
button.addEventListener('touchend', start);
