import unittest
import os
import cv2
import numpy as np

from image_processor.io import (
    load_image,
    save_image,
    display_image,
)


INPUT_IMAGE = "examples/input/test.jpg"
TEST_OUTPUT = "examples/output/test_io_output.jpg"


class TestIO(unittest.TestCase):

    def setUp(self):
        self.image = load_image(INPUT_IMAGE)

    def tearDown(self):
        if os.path.exists(TEST_OUTPUT):
            os.remove(TEST_OUTPUT)

    def test_load_image(self):
        image = load_image(INPUT_IMAGE)

        self.assertIsNotNone(image)
        self.assertIsInstance(image, np.ndarray)

    def test_load_invalid_image(self):
        with self.assertRaises(FileNotFoundError):
            load_image("examples/input/nonexistent.jpg")

    def test_save_image(self):
        save_image(self.image, TEST_OUTPUT)

        self.assertTrue(os.path.exists(TEST_OUTPUT))

        saved_image = cv2.imread(TEST_OUTPUT)

        self.assertIsNotNone(saved_image)
        self.assertEqual(saved_image.shape, self.image.shape)

    def test_save_none_image(self):
        with self.assertRaises(ValueError):
            save_image(None, TEST_OUTPUT)

    
if __name__ == "__main__":
    unittest.main()
