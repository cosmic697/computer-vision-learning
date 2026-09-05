import unittest
import cv2
import numpy as np
import os
from image_processor import (
    load_image,
    save_image,
    to_grayscale,
    resize_image,
    crop_image,
    rotate_image,
    blur_image,
    threshold_image,
    detect_edges,
)

INPUT_IMAGE = "examples/input/test.jpg"
TEST_OUTPUT = "examples/output/test_output.jpg"

class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        self.image = load_image(INPUT_IMAGE)

    def tearDown(self):
        if os.path.exists(TEST_OUTPUT):
            os.remove(TEST_OUTPUT)

    def test_load_image(self):
        image = load_image("examples/input/test.jpg")
        self.assertIsNotNone(image)
        self.assertIsInstance(image, np.ndarray)

    def test_save_image(self):
        save_image(self.image, TEST_OUTPUT)
        self.assertTrue(os.path.exists(TEST_OUTPUT))

        saved_image = cv2.imread(TEST_OUTPUT)
        self.assertIsNotNone(saved_image)
        self.assertEqual(saved_image.shape, self.image.shape)

    def test_save_none_image(self):
        with self.assertRaises(ValueError):
            save_image(None,TEST_OUTPUT)

    def test_to_grayscale(self):
        gray = to_grayscale(self.image)
        self.assertEqual(len(gray.shape), 2)
        self.assertEqual(gray.shape, self.image.shape[:2])

    def test_grayscale_none(self):
        with self.assertRaises(ValueError):
            to_grayscale(None)

    def test_resize_image(self):
        resized = resize_image(self.image, 300, 200)
        self.assertEqual(resized.shape, (200, 300, 3))

    def test_resize_none(self):
        with self.assertRaises(ValueError):
            resize_image(None, 300, 200)

    def test_resize_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            resize_image(self.image, 0, 200)

        with self.assertRaises(ValueError):
            resize_image(self.image, 300, 0)

        with self.assertRaises(ValueError):
            resize_image(self.image, -100, 200)

    def test_crop_image(self):
        cropped = crop_image(self.image, 100, 50, 400, 250)
        self.assertEqual(cropped.shape, (200, 300, 3))

    def test_crop_none(self):
        with self.assertRaises(ValueError):
            crop_image(None, 100, 50, 400, 250)

    
    def test_rotate_image(self):
        rotated = rotate_image(self.image, 45)
        self.assertEqual(rotated.shape, self.image.shape)

    def test_rotate_none(self):
        with self.assertRaises(ValueError):
            rotate_image(None, 45)

    def test_rotate_invalid_angle(self):
        with self.assertRaises(TypeError):
            rotate_image(self.image, "45")

    def test_blur_image(self):
        blurred = blur_image(self.image, 5)
        self.assertEqual(blurred.shape, self.image.shape)

    def test_blur_none(self):
        with self.assertRaises(ValueError):
            blur_image(None, 5)

    def test_blur_invalid_kernel(self):
        with self.assertRaises(ValueError):
            blur_image(self.image, 0)
        with self.assertRaises(ValueError):
            blur_image(self.image, 4)
        with self.assertRaises(ValueError):
            blur_image(self.image, -3)
        with self.assertRaises(TypeError):
            blur_image(self.image, "5")

    def test_threshold_image(self):
        gray = to_grayscale(self.image)
        thresholded = threshold_image(gray)
        self.assertEqual(thresholded.shape, gray.shape)

        unique_values = np.unique(thresholded)
        for value in unique_values:
            self.assertIn(value, [0, 255])

    def test_threshold_color_image(self):
        with self.assertRaises(ValueError):
            threshold_image(self.image)

    def test_threshold_none(self):
         with self.assertRaises(ValueError):
            threshold_image(None)

    def test_threshold_invalid_values(self):
        gray = to_grayscale(self.image)

        with self.assertRaises(ValueError):
            threshold_image(gray, -1)

        with self.assertRaises(ValueError):
            threshold_image(gray, 256)

        with self.assertRaises(ValueError):
            threshold_image(gray, 127, 256)

    def test_detect_edges(self):
        gray = to_grayscale(self.image)
        edges = detect_edges(gray)
        self.assertEqual(edges.shape, gray.shape)

    def test_detect_edges_none(self):
        with self.assertRaises(ValueError):
            detect_edges(None)

    def test_detect_edges_invalid_thresholds(self):
        gray = to_grayscale(self.image)

        with self.assertRaises(ValueError):
            detect_edges(gray, -1, 200)

        with self.assertRaises(ValueError):
            detect_edges(gray, 100, 256)

if __name__ == "__main__":
    unittest.main()