from image_processor.filtering import (gaussian_blur_image,median_blur_image,average_blur_image,bilateral_blur_image,custom_convolution,sharpen_image,unsharp_mask,reduce_noise,remove_salt_pepper_noise,)

from cli.helpers import get_image, save_result

import numpy as np

def gaussian_blur_command():
    """Apply Gaussian blur."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        result = gaussian_blur_image(image, kernel_size)
        print("\nGaussian blur applied successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel size must be an integer.")
    except Exception as error:
        print(f"\nFailed to apply Gaussian blur: {error}")

def median_blur_command():
    """Apply median blur."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        result = median_blur_image(image, kernel_size)
        print("\nMedian blur applied successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel size must be an integer.")
    except Exception as error:
        print(f"\nFailed to apply median blur: {error}")

def average_blur_command():
    """Apply average blur."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        result = average_blur_image(image, kernel_size)
        print("\nAverage blur applied successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel size must be an integer.")
    except Exception as error:
        print(f"\nFailed to apply average blur: {error}")

def bilateral_blur_command():
    """Apply bilateral filtering."""
    image = get_image()
    if image is None:
        return
    try:
        diameter = int(input("Enter diameter: "))
        sigma_color = float(input("Enter sigma color: "))
        sigma_space = float(input("Enter sigma space: "))
        result = bilateral_blur_image(
            image,
            diameter,
            sigma_color,
            sigma_space,
        )
        print("\nBilateral filter applied successfully.")
        save_result(result)
    except ValueError:
        print("\nInvalid input.")
    except Exception as error:
        print(f"\nFailed to apply bilateral filter: {error}")


def custom_convolution_command():
    """Apply a custom convolution kernel."""
    image = get_image()
    if image is None:
        return
    try:
        size = int(input("Enter kernel size (odd number): "))
        if size <= 0 or size % 2 == 0:
            print("\nKernel size must be a positive odd number.")
            return
        print("\nEnter kernel values row by row.")
        values = []
        for i in range(size):
            row = input(f"Row {i + 1}: ").split()
            if len(row) != size:
                print(f"\nEach row must contain exactly {size} values.")
                return
            values.append([float(value) for value in row])
        kernel = np.array(values, dtype=np.float32)
        result = custom_convolution(image, kernel)
        print("\nCustom convolution applied successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel values must be numbers.")
    except Exception as error:
        print(f"\nFailed to apply convolution: {error}")

def sharpening_command():
    """Sharpen an image."""
    image = get_image()
    if image is None:
        return
    try:
        result = sharpen_image(image)
        print("\nImage sharpened successfully.")
        save_result(result)
    except Exception as error:
        print(f"\nFailed to sharpen image: {error}")

def unsharp_mask_command():
    """Apply unsharp masking."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        amount = float(input("Enter sharpening amount: "))
        result = unsharp_mask(
            image,
            kernel_size,
            amount,
        )
        print("\nUnsharp mask applied successfully.")
        save_result(result)
    except ValueError:
        print("\nInvalid input.")
    except Exception as error:
        print(f"\nFailed to apply unsharp mask: {error}")

def noise_reduction_command():
    """Reduce image noise."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        result = reduce_noise(image, kernel_size)
        print("\nNoise reduction applied successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel size must be an integer.")
    except Exception as error:
        print(f"\nFailed to reduce noise: {error}")

def salt_pepper_removal_command():
    """Remove salt-and-pepper noise."""
    image = get_image()
    if image is None:
        return
    try:
        kernel_size = int(input("Enter kernel size: "))
        result = remove_salt_pepper_noise(image, kernel_size)
        print("\nSalt-and-pepper noise removed successfully.")
        save_result(result)
    except ValueError:
        print("\nKernel size must be an integer.")
    except Exception as error:
        print(f"\nFailed to remove salt-and-pepper noise: {error}")