const player = document.getElementById('vid')
const button = document.querySelector('.button');

function callApi(sessionId, imageBase64) {
    var formData = {session_id: sessionId, image_base64: imageBase64};
    $.ajax({
        type: 'POST',
        url: 'http://localhost/describe',
        data: JSON.stringify(formData),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(data, textStatus, xhr) {
            console.log(xhr.status);
        },
        error: function() {
            // ignore
        },
        complete: function() {
            // ignore
        }
    });
}

function process(sessionId) {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
    imageBase64 = canvas.toDataURL();
    imageBase64 = imageBase64.split(',');
    imageBase64.shift();
    callApi(sessionId, imageBase64.join());
}

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
                process(sessionId);
            }, 1000);
        });
}

button.addEventListener('click', start);
button.addEventListener('touchend', start);
