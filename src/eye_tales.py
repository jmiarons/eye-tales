import connexion

from flask_cors import CORS

from src.neural_image_caption_generation.inference_image_captioning import init

connexion_app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
flask_app = connexion_app.app
flask_app.config['JSON_AS_ASCII'] = False
connexion_app.add_api('openapi.yaml', arguments={'title': 'Eye Tales API'})
CORS(flask_app)

encoder, decoder, max_length, image_features_extract_model, tokenizer = init()


@flask_app.route('/')
def alive_check():
    return 'Welcome to Eye Tales API!', 200
