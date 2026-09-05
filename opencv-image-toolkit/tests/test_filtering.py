import unittest
import numpy as np

from image_processor.filtering import (gaussian_blur_image,median_blur_image,average_blur_image,bilateral_blur_image,custom_convolution,sharpen_image,unsharp_mask,reduce_noise,remove_salt_pepper_noise,)

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.image = np.zeros((400, 600, 3),dtype=np.uint8)

    def test_blur_image(self):
        blurred = gaussian_blur_image(self.image,5)
        self.assertIsInstance(blurred,np.ndarray)
        self.assertEqual(blurred.shape,self.image.shape)

    def test_blur_none(self):
        with self.assertRaises(ValueError):
            gaussian_blur_image(None,5)

    def test_blur_invalid_kernel(self):
        with self.assertRaises(ValueError):
            gaussian_blur_image(self.image,4)

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

    def test_average_blur(self):
        result = average_blur_image(self.image,5)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_average_blur_none(self):
        with self.assertRaises(ValueError):
            average_blur_image(None, 5)

    def test_average_blur_invalid_type(self):
        with self.assertRaises(TypeError):
            average_blur_image(self.image,"5")

    def test_average_blur_even_kernel(self):
        with self.assertRaises(ValueError):
            average_blur_image(self.image,4)

    def test_bilateral_blur(self):
        result = bilateral_blur_image(self.image,9,75,75)

        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_bilateral_blur_none(self):
        with self.assertRaises(ValueError):
            bilateral_blur_image(None,9,75,75)

    def test_bilateral_invalid_diameter(self):
        with self.assertRaises((TypeError, ValueError)):
            bilateral_blur_image(self.image, "9", 75, 75)

    def test_bilateral_invalid_sigma_color(self):
        with self.assertRaises((TypeError, ValueError)):
            bilateral_blur_image(self.image, 9, "75", 75)

    def test_bilateral_invalid_sigma_space(self):
        with self.assertRaises((TypeError, ValueError)):
            bilateral_blur_image(self.image, 9, 75, "75")

    def test_bilateral_invalid_diameter_value(self):
        with self.assertRaises(ValueError):
            bilateral_blur_image(self.image,0,75,75)

    def test_bilateral_invalid_sigma_color_value(self):
        with self.assertRaises(ValueError):
            bilateral_blur_image(self.image,9,0,75)

    def test_bilateral_invalid_sigma_space_value(self):
        with self.assertRaises(ValueError):
            bilateral_blur_image(self.image,9,75,0)

    def test_sharpen_image(self):
        result = sharpen_image(self.image)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_sharpen_none(self):
        with self.assertRaises(ValueError):
            sharpen_image(None)

    def test_custom_convolution(self):
        kernel = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]], dtype=np.float32)
        result = custom_convolution(self.image,kernel)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_custom_convolution_none_image(self):
        kernel = np.ones((3, 3),dtype=np.float32)
        with self.assertRaises(ValueError):
            custom_convolution(None,kernel)

    def test_custom_convolution_none_kernel(self):
        with self.assertRaises(ValueError):
            custom_convolution(self.image,None)

    def test_custom_convolution_invalid_kernel_type(self):
        with self.assertRaises(TypeError):
            custom_convolution(self.image,[[1, 2], [3, 4]])

    def test_custom_convolution_invalid_kernel_dimension(self):
        kernel = np.ones((3, 3, 3),dtype=np.float32)

        with self.assertRaises(ValueError):
            custom_convolution(self.image,kernel)

    def test_custom_convolution_even_kernel(self):
        kernel = np.ones((4, 4),dtype=np.float32)
        with self.assertRaises(ValueError):
            custom_convolution(self.image,kernel)

    def test_unsharp_mask(self):
        result = unsharp_mask(self.image,5,1.0)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_unsharp_mask_none(self):
        with self.assertRaises(ValueError):
            unsharp_mask(None,5,1.0)

    def test_unsharp_invalid_kernel_type(self):
        with self.assertRaises(TypeError):
            unsharp_mask(self.image,"5",1.0)

    def test_unsharp_invalid_amount_type(self):
        with self.assertRaises(TypeError):
            unsharp_mask(self.image,5,"1.0")

    def test_unsharp_even_kernel(self):
        with self.assertRaises(ValueError):
            unsharp_mask(self.image,4,1.0)

    def test_unsharp_negative_amount(self):
        with self.assertRaises(ValueError):
            unsharp_mask(self.image,5,-1.0)

    def test_reduce_noise(self):
        result = reduce_noise(self.image,5)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_reduce_noise_none(self):
        with self.assertRaises(ValueError):
            reduce_noise(None,5)

    def test_reduce_noise_invalid_type(self):
        with self.assertRaises(TypeError):
            reduce_noise(self.image,"5")

    def test_reduce_noise_even_kernel(self):
        with self.assertRaises(ValueError):
            reduce_noise(self.image,4)

    def test_remove_salt_pepper_noise(self):
        result = remove_salt_pepper_noise(self.image,5)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

    def test_remove_salt_pepper_none(self):
        with self.assertRaises(ValueError):
            remove_salt_pepper_noise(None,5)

    def test_remove_salt_pepper_invalid_type(self):
        with self.assertRaises(TypeError):
            remove_salt_pepper_noise(self.image,"5")

    def test_remove_salt_pepper_even_kernel(self):
        with self.assertRaises(ValueError):
            remove_salt_pepper_noise(self.image,4)


if __name__ == "__main__":
    unittest.main()