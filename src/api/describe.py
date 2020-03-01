import base64
import io
import random

from flask import request, send_file

from src.eye_tales import max_length, encoder, decoder, image_features_extract_model, tokenizer
from src.helper import response, logic
from src.neural_image_caption_generation.inference_image_captioning import evaluate
from src.text_to_speech import text2speech


def post():
    try:
        # Get parameters
        request_body = request.json
        if 'image_base64' not in request_body or 'session_id' not in request_body or 'iteration' not in request_body:
            return response.make(True, 'image_base64, session_id and iteration has to be specified.', code=400)
        image_base64 = request_body['image_base64']
        session_id = request_body['session_id']
        iteration = request_body['iteration']
        # Save image
        image_path = 'data/{}.jpg'.format(random.choice(range(100)))
        image_encoded = base64.b64decode(image_base64)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_encoded)
        if iteration % 10 == 0:
            sentence = evaluate(image_path, max_length, encoder, decoder, image_features_extract_model, tokenizer)
            sentence = ' '.join(sentence[:-1]).capitalize()
        else:
            # Apply logic
            sentence = logic.describe(session_id, image_path)
        # Transcribe to speech if needed
        if sentence:
            audio_binary = text2speech.synthesize_text(sentence)
            return send_file(
                io.BytesIO(audio_binary),
                attachment_filename='audio.mp3',
                mimetype='audio/mpeg'
            ), 200
        else:
            return response.make(False, message='nothing to say', code=204)
    except Exception as e:
        print('error: unexpected error: {}'.format(e))
        return response.make(False, message='unexpected error', code=204)
