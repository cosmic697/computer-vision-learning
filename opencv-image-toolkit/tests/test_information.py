import unittest
import numpy as np

from image_processor.information import (get_dimensions,get_width,get_height,get_channels,get_dtype,get_pixel,get_statistics,is_grayscale,is_color,)


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

    def test_get_pixel_color(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        image[20, 10] = [10, 20, 30]
        pixel = get_pixel(image, 10, 20)
        np.testing.assert_array_equal(pixel, [10, 20, 30])

    def test_get_pixel_grayscale(self):
        image = np.zeros((100, 100), dtype=np.uint8)
        image[20, 10] = 127
        pixel = get_pixel(image, 10, 20)
        self.assertEqual(pixel, 127)

    def test_get_pixel_none(self):
        with self.assertRaises(ValueError):
            get_pixel(None, 10, 20)

    def test_get_pixel_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            get_pixel(self.color_image, -1, 20)

        with self.assertRaises(ValueError):
            get_pixel(self.color_image, 10, 500)

    def test_get_pixel_invalid_coordinate_type(self):
        with self.assertRaises(TypeError):
            get_pixel(self.color_image, "10", 20)

    def test_get_statistics(self):
        image = np.array(
            [ [0, 50], [100, 150]],dtype=np.uint8)
        statistics = get_statistics(image)
        self.assertEqual(statistics["min"], 0)
        self.assertEqual(statistics["max"], 150)
        self.assertEqual(statistics["mean"], 75)
        self.assertAlmostEqual(statistics["std"],np.std(image))

    def test_get_statistics_none(self):
        with self.assertRaises(ValueError):
            get_statistics(None)

    def test_is_grayscale(self):
        self.assertTrue(is_grayscale(self.gray_image))
        self.assertFalse(is_grayscale(self.color_image))

    def test_is_grayscale_none(self):
        with self.assertRaises(ValueError):
            is_grayscale(None)

    def test_is_color(self):
        self.assertTrue(is_color(self.color_image))
        self.assertFalse(is_color(self.gray_image))

    def test_is_color_none(self):
        with self.assertRaises(ValueError):
            is_color(None)
    


if __name__ == "__main__":
    unittest.main()
