import unittest

from src.helper import logic


class DescribeTest(unittest.TestCase):

    def setUp(self):
        self.session_id = '123456789'
        self.image_path = 'examples/test_4.jpg'

    def test_describe(self):
        result = logic.describe(self.session_id, self.image_path)
        self.assertIsNotNone(result)
        print(result)
