const player = document.getElementById('vid')
const button = document.querySelector('.button');

function process() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
    console.log(canvas.toDataURL());
    // call the api
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
            setInterval(function() {
                process();
            }, 1000);
        });
}

button.addEventListener('click', start);
button.addEventListener('touchend', start);
