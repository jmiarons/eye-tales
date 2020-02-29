from flask import request

from src.helper import response
from src.text_to_speech import text2speech


def post():
    request_body = request.json
    if 'image_base64' not in request_body:
        return response.make(error=True, message='image_base64 has to be specified.')
    image_base64 = request_body['image_base64']
    # do some magic for get a sentence from the image
    sentence = 'Test'
    audio_binary = text2speech.synthesize_text(sentence)
    return 'ok', 200
