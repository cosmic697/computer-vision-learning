import unittest
import numpy as np

from image_processor.thresholding import (threshold_image,)
class TestThresholding(unittest.TestCase):

    def setUp(self):
        self.gray_image = np.zeros((400, 600),dtype=np.uint8)

    def test_threshold_image(self):
        thresholded = threshold_image(self.gray_image,127,255)
        self.assertIsInstance(thresholded,np.ndarray)
        self.assertEqual(thresholded.shape,self.gray_image.shape)

    def test_threshold_none(self):
        with self.assertRaises(ValueError):
            threshold_image(None,127,255)

    def test_threshold_color_image(self):
        color_image = np.zeros((400, 600, 3),dtype=np.uint8)
        with self.assertRaises(ValueError):
            threshold_image(color_image,127,255)

    def test_invalid_threshold(self):
        with self.assertRaises(ValueError):
            threshold_image(self.gray_image,300,255)

    def test_invalid_max_value(self):
        with self.assertRaises(ValueError):
            threshold_image(self.gray_image,127,300)


if __name__ == "__main__":
    unittest.main()