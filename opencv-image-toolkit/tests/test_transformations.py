import unittest
import numpy as np

from image_processor.transformations import (
    to_grayscale,
    resize_image,
    crop_image,
    rotate_image,
)


class TestTransformations(unittest.TestCase):

    def setUp(self):
        self.image = np.zeros((400, 600, 3),dtype=np.uint8)

    def test_to_grayscale(self):
        gray = to_grayscale(self.image)
        self.assertIsInstance(gray, np.ndarray)
        self.assertEqual(gray.shape, (400, 600))

    def test_to_grayscale_none(self):
        with self.assertRaises(ValueError):
            to_grayscale(None)

    def test_resize_image(self):
        resized = resize_image(self.image,300,200)
        self.assertEqual(resized.shape,(200, 300, 3))

    def test_resize_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            resize_image(self.image,0,200)

    def test_resize_none(self):
        with self.assertRaises(ValueError):
            resize_image(None,300,200)

    def test_crop_image(self):
        cropped = crop_image(self.image,100,50,400,250)
        self.assertEqual(cropped.shape,(200, 300, 3))

    def test_crop_none(self):
        with self.assertRaises(ValueError):
            crop_image(None, 0,0,100,100)

    def test_rotate_image(self):
        rotated = rotate_image(self.image,90)
        self.assertIsInstance(rotated,np.ndarray)
        self.assertEqual(rotated.shape, self.image.shape)

    def test_rotate_none(self):
        with self.assertRaises(ValueError):
            rotate_image(None, 90)

    def test_rotate_invalid_angle(self):
        with self.assertRaises(TypeError):
            rotate_image(self.image,"90")

if __name__ == "__main__":
    unittest.main()