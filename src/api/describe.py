import io

from flask import request, send_file

from src.helper import response, logic
from src.text_to_speech import text2speech


def post():
    request_body = request.json
    if 'image_base64' not in request_body:
        return response.make(True, 'image_base64 has to be specified.', code=400)
    image_base64 = request_body['image_base64']
    # do some magic for get a sentence from the image
    sentence = logic.describe(image_base64)
    if sentence:
        audio_binary = text2speech.synthesize_text(sentence)
        return send_file(
            io.BytesIO(audio_binary),
            attachment_filename='audio.mp3',
            mimetype='audio/mpeg'
        ), 200
    else:
        return response.make(False, message='nothing to say', code=204)
