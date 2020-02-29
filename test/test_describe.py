import unittest

from src.helper import logic


class DescribeTest(unittest.TestCase):

    def setUp(self):
        self.image_path = 'examples/test_1.jpg'

    def test_describe(self):
        result = logic.describe(self.image_path)
        self.assertIsNotNone(result)
