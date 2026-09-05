import unittest
import numpy as np

from image_processor.filtering import (blur_image,median_blur_image)


class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.image = np.zeros((400, 600, 3),dtype=np.uint8)

    def test_blur_image(self):
        blurred = blur_image(self.image,5)
        self.assertIsInstance(blurred,np.ndarray)
        self.assertEqual(blurred.shape,self.image.shape)

    def test_blur_none(self):
        with self.assertRaises(ValueError):
            blur_image(None,5)

    def test_blur_invalid_kernel(self):
        with self.assertRaises(ValueError):
            blur_image(self.image,4)

    def test_median_blur_image(self):
        blurred = median_blur_image(self.image,5)
        self.assertIsInstance(blurred,np.ndarray)
        self.assertEqual(blurred.shape,self.image.shape)

    def test_median_blur_none(self):
        with self.assertRaises(ValueError):
            median_blur_image(None,5)

    def test_median_blur_invalid_kernel(self):
        with self.assertRaises(ValueError):
            median_blur_image(self.image,4)


if __name__ == "__main__":
    unittest.main()