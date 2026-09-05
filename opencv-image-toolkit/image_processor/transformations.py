import cv2
import numpy as np

def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    resized = cv2.resize(image, (width, height))
    return resized

def crop_image(image:np.ndarray, x1:int, y1:int, x2:int, y2:int) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    cropped = image[y1:y2, x1:x2]
    return cropped

def rotate_image(image: np.ndarray, angle: float) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(angle, (int, float)):
        raise TypeError("Angle must be a number.")
    height , width = image.shape[:2]
    center = (width//2 ,height//2)
    matrix = cv2.getRotationMatrix2D(center,angle,1.0)
    rotated = cv2.warpAffine(image , matrix , (width,height))
    return rotated

def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray


