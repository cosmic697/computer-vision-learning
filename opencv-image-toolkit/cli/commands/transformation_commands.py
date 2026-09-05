from image_processor.transformations import (resize_image,crop_image,rotate_image,to_grayscale,flip_horizontal,flip_vertical,flip_both,translate_image,scale_image,shear_image,affine_transform,perspective_transform,add_padding,)

from cli.helpers import get_image, save_result

import numpy as np
import cv2

def resize_command():
    """Resize an image."""
    image = get_image()
    if image is None:
        return
    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        result = resize_image(image, width, height)
        print("\nImage resized successfully.")
        save_result(result)
    except ValueError:
        print("\nWidth and height must be integers.")
    except Exception as error:
        print(f"\nFailed to resize image: {error}")

def crop_command():
    """Crop an image."""
    image = get_image()
    if image is None:
        return
    try:
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        result = crop_image(image, x1, y1, x2, y2)
        print("\nImage cropped successfully.")
        save_result(result)
    except ValueError:
        print("\nCoordinates must be integers.")
    except Exception as error:
        print(f"\nFailed to crop image: {error}")

def rotate_command():
    """Rotate an image."""
    image = get_image()
    if image is None:
        return
    try:
        angle = float(input("Enter rotation angle: "))
        result = rotate_image(image, angle)
        print("\nImage rotated successfully.")
        save_result(result)
    except ValueError:
        print("\nAngle must be a number.")
    except Exception as error:
        print(f"\nFailed to rotate image: {error}")

def grayscale_command():
    """Convert an image to grayscale."""
    image = get_image()
    if image is None:
        return
    try:
        result = to_grayscale(image)
        print("\nImage converted to grayscale.")
        save_result(result)
    except Exception as error:
        print(f"\nFailed to convert image: {error}")

def horizontal_flip_command():
    """Flip an image horizontally."""
    image = get_image()
    if image is None:
        return
    try:
        result = flip_horizontal(image)
        print("\nImage flipped horizontally.")
        save_result(result)
    except Exception as error:
        print(f"\nFailed to flip image: {error}")

def vertical_flip_command():
    """Flip an image vertically."""
    image = get_image()
    if image is None:
        return
    try:
        result = flip_vertical(image)
        print("\nImage flipped vertically.")
        save_result(result)
    except Exception as error:
        print(f"\nFailed to flip image: {error}")

def both_flip_command():
    """Flip an image horizontally and vertically."""
    image = get_image()
    if image is None:
        return
    try:
        result = flip_both(image)
        print("\nImage flipped on both axes.")
        save_result(result)
    except Exception as error:
        print(f"\nFailed to flip image: {error}")

def translation_command():
    """Translate an image."""
    image = get_image()
    if image is None:
        return
    try:
        tx = float(input("Enter x translation: "))
        ty = float(input("Enter y translation: "))
        result = translate_image(image, tx, ty)
        print("\nImage translated successfully.")
        save_result(result)
    except ValueError:
        print("\nTranslation values must be numbers.")
    except Exception as error:
        print(f"\nFailed to translate image: {error}")

def scaling_command():
    """Scale an image."""
    image = get_image()
    if image is None:
        return
    try:
        tx = float(input("Enter horizontal scale: "))
        ty = float(input("Enter vertical scale: "))
        result = scale_image(image, tx, ty)
        print("\nImage scaled successfully.")
        save_result(result)
    except ValueError:
        print("\nScale factors must be numbers.")

    except Exception as error:
        print(f"\nFailed to scale image: {error}")

def shearing_command():
    """Shear an image."""
    image = get_image()
    if image is None:
        return
    try:
        shear_x = float(input("Enter horizontal shear: "))
        shear_y = float(input("Enter vertical shear: "))
        result = shear_image(image, shear_x, shear_y)
        print("\nImage sheared successfully.")
        save_result(result)
    except ValueError:
        print("\nShear values must be numbers.")
    except Exception as error:
        print(f"\nFailed to shear image: {error}")

def affine_command():
    """Apply an affine transformation."""
    image = get_image()
    if image is None:
        return
    try:
        print("\nEnter 3 source points.")
        source_points = []
        for i in range(3):
            x = float(input(f"Source point {i + 1} x: "))
            y = float(input(f"Source point {i + 1} y: "))
            source_points.append([x, y])
        print("\nEnter 3 destination points.")
        destination_points = []
        for i in range(3):
            x = float(input(f"Destination point {i + 1} x: "))
            y = float(input(f"Destination point {i + 1} y: "))
            destination_points.append([x, y])
        source_points = np.array(source_points, dtype=np.float32)
        destination_points = np.array(destination_points, dtype=np.float32)
        result = affine_transform(
            image,
            source_points,
            destination_points,
        )
        print("\nAffine transformation applied successfully.")
        save_result(result)
    except ValueError:
        print("\nPoint coordinates must be numbers.")
    except Exception as error:
        print(f"\nFailed to apply affine transformation: {error}")

def perspective_command():
    """Apply a perspective transformation."""
    image = get_image()
    if image is None:
        return
    try:
        print("\nEnter 4 source points.")
        source_points = []
        for i in range(4):
            x = float(input(f"Source point {i + 1} x: "))
            y = float(input(f"Source point {i + 1} y: "))
            source_points.append([x, y])
        print("\nEnter 4 destination points.")
        destination_points = []
        for i in range(4):
            x = float(input(f"Destination point {i + 1} x: "))
            y = float(input(f"Destination point {i + 1} y: "))
            destination_points.append([x, y])
        source_points = np.array(source_points, dtype=np.float32)
        destination_points = np.array(destination_points, dtype=np.float32)
        result = perspective_transform(
            image,
            source_points,
            destination_points,
        )
        print("\nPerspective transformation applied successfully.")
        save_result(result)
    except ValueError:
        print("\nPoint coordinates must be numbers.")
    except Exception as error:
        print(f"\nFailed to apply perspective transformation: {error}")

def padding_command():
    """Add padding around an image."""
    image = get_image()
    if image is None:
        return
    try:
        top = int(input("Enter top padding: "))
        bottom = int(input("Enter bottom padding: "))
        left = int(input("Enter left padding: "))
        right = int(input("Enter right padding: "))
        result = add_padding(
            image,
            top,
            bottom,
            left,
            right,
        )
        print("\nPadding added successfully.")
        save_result(result)
    except ValueError:
        print("\nPadding values must be integers.")
    except Exception as error:
        print(f"\nFailed to add padding: {error}")