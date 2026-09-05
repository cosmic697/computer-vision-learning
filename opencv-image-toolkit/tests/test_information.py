import unittest
import numpy as np

from image_processor.information import (
    get_dimensions,
    get_width,
    get_height,
    get_channels,
    get_dtype,
)


class TestInformation(unittest.TestCase):

    def setUp(self):
        self.color_image = np.zeros((347, 576, 3), dtype=np.uint8)
        self.gray_image = np.zeros((347, 576), dtype=np.uint8)

    def test_get_dimensions(self):
        dimensions = get_dimensions(self.color_image)

        self.assertEqual(dimensions, (347, 576, 3))

    def test_get_dimensions_none(self):
        with self.assertRaises(ValueError):
            get_dimensions(None)

    def test_get_width(self):
        width = get_width(self.color_image)

        self.assertEqual(width, 576)

    def test_get_width_none(self):
        with self.assertRaises(ValueError):
            get_width(None)

    def test_get_height(self):
        height = get_height(self.color_image)

        self.assertEqual(height, 347)

    def test_get_height_none(self):
        with self.assertRaises(ValueError):
            get_height(None)

    def test_get_channels_color(self):
        channels = get_channels(self.color_image)

        self.assertEqual(channels, 3)

    def test_get_channels_grayscale(self):
        channels = get_channels(self.gray_image)

        self.assertEqual(channels, 1)

    def test_get_channels_none(self):
        with self.assertRaises(ValueError):
            get_channels(None)

    def test_get_dtype(self):
        dtype = get_dtype(self.color_image)

        self.assertEqual(dtype, np.uint8)

    def test_get_dtype_none(self):
        with self.assertRaises(ValueError):
            get_dtype(None)


if __name__ == "__main__":
    unittest.main()
