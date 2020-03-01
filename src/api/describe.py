import base64
import io
import random

from flask import request, send_file

from src.helper import response, logic
from src.neural_image_caption_generation import inference_image_captioning
from src.text_to_speech import text2speech


# Initialize image captioning model
encoder, decoder, max_length, image_features_extractor, tokenizer = inference_image_captioning.init()


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
            sentence = inference_image_captioning.evaluate(
                image_path, max_length, encoder, decoder, image_features_extractor, tokenizer
            )
            sentence = ' '.join(sentence[:-1]).capitalize()
        else:
            # Apply logic
            sentence = logic.describe(session_id, image_path)
        # Transcribe to speech if needed
        if sentence:
            print('{}: {}'.format(iteration, sentence))
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
