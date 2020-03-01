import base64
import unittest
import requests

from playsound import playsound

from src.helper import logic


class DescribeTest(unittest.TestCase):

    def setUp(self):
        self.session_id = '123456789'
        self.image_path = 'examples/test_4.jpg'
        self.endpoint = 'http://34.89.52.65:81/describe'
        self.audio_path = 'data/output.mp3'
        with open(self.image_path, 'rb') as image_file:
            self.image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    def test_describe(self):
        result = logic.describe(self.session_id, self.image_path)
        self.assertIsNotNone(result)
        print(result)

    def test_cache(self):
        data = dict(iteration=10, session_id=self.session_id, image_base64=self.image_base64)
        response = requests.post(self.endpoint, json=data)
        if response.status_code == 200:
            with open(self.audio_path, 'wb') as out:
                out.write(response.content)
            playsound(self.audio_path)
