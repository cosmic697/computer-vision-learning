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

