import cv2
import numpy as np

def get_dimensions(image: np.ndarray) -> tuple:
    if image is None:
        raise ValueError("Image cannot be None.")
    return image.shape

def get_width(image: np.ndarray) -> int:
    if image is None:
        raise ValueError("Image cannot be None.")
    return image.shape[1]

def get_height(image: np.ndarray) -> int:
    if image is None:
        raise ValueError("Image cannot be None.")
    return image.shape[0]

def get_channels(image: np.ndarray) -> int:
    #channels means the individual color layer in each image--- not given for grayscale image 
    if image is None:
        raise ValueError("Image cannot be None.")
    if len(image.shape) == 2:
        return 1
    return image.shape[2]

def get_dtype(image: np.ndarray) -> np.dtype:
    if image is None:
        raise ValueError("Image cannot be None.")
    return image.dtype

def get_pixel(image: np.ndarray, x:int , y:int)->tuple:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x and y must be integers.")
    height, width = image.shape[:2]
    if x < 0 or x >= width:
        raise ValueError("x coordinate is outside the image.")
    if y < 0 or y >= height:
        raise ValueError("y coordinate is outside the image.")
    return image[y, x]

def get_statistics(image: np.ndarray) -> dict:
    if image is None:
        raise ValueError("Image cannot be None.")
    statistics = {
        "min": np.min(image),
        "max": np.max(image),
        "mean": np.mean(image),
        "std": np.std(image),
    }
    return statistics

def is_grayscale(image: np.ndarray) -> bool:
    if image is None:
        raise ValueError("Image cannot be None.")
    return len(image.shape) == 2

def is_color(image: np.ndarray) -> bool:
    if image is None:
        raise ValueError("Image cannot be None.")
    return len(image.shape) == 3

