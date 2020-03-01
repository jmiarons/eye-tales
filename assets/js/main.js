window.onload = init;
var context;    // Audio context
var buf;        // Audio buffer

// Global variables
const player = document.getElementById('vid')
const button = document.querySelector('.button');
var iteration = 1;

// Ajax
function callApi(iteration, sessionId, imageBase64) {
    var formData = {iteration: iteration, session_id: sessionId, image_base64: imageBase64};
    $.ajax({
        type: 'POST',
        url: 'http://34.89.52.65/describe',
        data: JSON.stringify(formData),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(data, textStatus, xhr) {
            if (xhr.status === 200) {
                playByteArray(data);
            } else {
                console.log('nothing to say', xhr.status);
            }
        },
        error: function() {
            // ignore
            console.log('error');
        },
        complete: function(xhr, textStatus) {
            // ignore
        }
    });
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
            }, 1000);
        });
}

// Audio init
function init() {
    if (!window.AudioContext) {
        if (!window.webkitAudioContext) {
            alert("Your browser does not support any AudioContext and cannot play back this audio.");
            return;
        }
        window.AudioContext = window.webkitAudioContext;
    }
    context = new AudioContext();
}

// Play Byte Array
function playByteArray(byteArray) {
    var arrayBuffer = new ArrayBuffer(byteArray.length);
    var bufferView = new Uint8Array(arrayBuffer);
    for (i = 0; i < byteArray.length; i++) {
        bufferView[i] = byteArray[i];
    }
    context.decodeAudioData(arrayBuffer, function(buffer) {
        buf = buffer;
        play();
    });
}

// Play the loaded file
function play() {
    // Create a source node from the buffer
    var source = context.createBufferSource();
    source.buffer = buf;
    // Connect to the final output node (the speakers)
    source.connect(context.destination);
    // Play immediately
    source.start(0);
}

button.addEventListener('click', start);
button.addEventListener('touchend', start);
