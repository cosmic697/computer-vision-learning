import unittest
import numpy as np
import cv2

from image_processor.transformations import (to_grayscale,resize_image,crop_image,rotate_image,flip_horizontal,flip_vertical,flip_both,translate_image,scale_image,shear_image,add_padding,perspective_transform,affine_transform)


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

    def test_flip_horizontal(self):
        image = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.uint8)
        expected = np.array([[3, 2, 1],[6, 5, 4]], dtype=np.uint8)
        result = flip_horizontal(image)
        np.testing.assert_array_equal(result, expected)

    def test_flip_horizontal_none(self):
        with self.assertRaises(ValueError):
            flip_horizontal(None)

    def test_flip_vertical(self):
        image = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.uint8)
        expected = np.array([[4, 5, 6],[1, 2, 3]], dtype=np.uint8)
        result = flip_vertical(image)
        np.testing.assert_array_equal(result, expected)

    def test_flip_vertical_none(self):
        with self.assertRaises(ValueError):
            flip_vertical(None)

    def test_flip_both(self):
        image = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.uint8)
        expected = np.array([[6, 5, 4],[3, 2, 1]], dtype=np.uint8)
        result = flip_both(image)
        np.testing.assert_array_equal(result, expected)

    def test_flip_both_none(self):
        with self.assertRaises(ValueError):
            flip_both(None)

    def test_translate_image(self):
        image = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]], dtype=np.uint8)
        result = translate_image(image, 1, 1)
        expected = np.array([[0, 0, 0],[0, 1, 2],[0, 4, 5]], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected)

    def test_translate_none(self):
        with self.assertRaises(ValueError):
            translate_image(None, 1, 1)

    def test_translate_invalid_x(self):
        with self.assertRaises(TypeError):
            translate_image(self.image, "10", 10)

    def test_translate_invalid_y(self):
        with self.assertRaises(TypeError):
            translate_image(self.image, 10, "10")

    def test_scale_image(self):
        result = scale_image(self.image, 0.5, 0.5)
        self.assertEqual(result.shape, (200, 300, 3))

    def test_scale_image_up(self):
        result = scale_image(self.image, 2, 2)
        self.assertEqual(result.shape, (800, 1200, 3))

    def test_scale_none(self):
        with self.assertRaises(ValueError):
            scale_image(None, 2, 2)

    def test_scale_invalid_x(self):
        with self.assertRaises(TypeError):
            scale_image(self.image, "2", 2)

    def test_scale_invalid_y(self):
        with self.assertRaises(TypeError):
            scale_image(self.image, 2, "2")

    def test_scale_zero(self):
        with self.assertRaises(ValueError):
            scale_image(self.image, 0, 2)

    def test_scale_negative(self):
        with self.assertRaises(ValueError):
            scale_image(self.image, -1, 2)

    def test_shear_image(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        result = shear_image(image, 0.2, 0)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, image.shape)


    def test_shear_image_vertical(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        result = shear_image(image, 0, 0.2)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, image.shape)


    def test_shear_none(self):
        with self.assertRaises(ValueError):
            shear_image(None, 0.2, 0)

    def test_shear_invalid_x(self):
        with self.assertRaises(TypeError):
            shear_image(self.image, "0.2", 0)

    def test_shear_invalid_y(self):
        with self.assertRaises(TypeError):
            shear_image(self.image, 0.2, "0")

    def test_affine_transform(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[10, 90]])
        result = affine_transform(image,source_points,destination_points)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, image.shape)

    def test_affine_none(self):
        source_points = np.float32([[0, 0],[99, 0],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[10, 90]])
        with self.assertRaises(ValueError):
            affine_transform(None,source_points,destination_points)

    def test_affine_invalid_source_points(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0]])
        destination_points = np.float32([[10, 10],[90, 10],[10, 90]])
        with self.assertRaises(ValueError):
            affine_transform(image,source_points,destination_points)

    def test_affine_invalid_destination_points(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10]])
        with self.assertRaises(ValueError):
            affine_transform(image,source_points,destination_points)

    def test_perspective_transform(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0],[99, 99],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[90, 90],[10, 90]])
        result = perspective_transform(image,source_points,destination_points)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, image.shape)

    def test_perspective_none(self):
        source_points = np.float32([[0, 0],[99, 0],[99, 99],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[90, 90],[10, 90]])
        with self.assertRaises(ValueError):
            perspective_transform(None,source_points,destination_points)

    def test_perspective_invalid_source_points(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0],[99, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[90, 90],[10, 90]])
        with self.assertRaises(ValueError):
            perspective_transform(image,source_points,destination_points)

    def test_perspective_invalid_destination_points(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        source_points = np.float32([[0, 0],[99, 0],[99, 99],[0, 99]])
        destination_points = np.float32([[10, 10],[90, 10],[90, 90]])
        with self.assertRaises(ValueError):
            perspective_transform(image,source_points,destination_points)

    def test_add_padding(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        result = add_padding(image,top=10,bottom=20,left=5,right=15)
        self.assertEqual(result.shape, (130, 120, 3))

    def test_add_padding_none(self):
        with self.assertRaises(ValueError):
            add_padding(None,10,10,10,10)

    def test_add_padding_negative(self):
        with self.assertRaises(ValueError):
            add_padding(self.image,-10,10,10,10)

    def test_add_padding_invalid_type(self):
        with self.assertRaises(TypeError):
            add_padding(self.image,"10",10,10,10)

    def test_add_padding_constant_value(self):
        image = np.zeros((10, 10, 3), dtype=np.uint8)
        result = add_padding(image,5,5,5,5,border_type=cv2.BORDER_CONSTANT,value=255)
        self.assertEqual(result.shape, (20, 20, 3))

if __name__ == "__main__":
    unittest.main()