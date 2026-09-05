import cv2
import numpy as np

def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    #more the kernel size the smoother the image the more the content lost
    #kernel size should be odd so that we have a correct center pixel
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.GaussianBlur(image,(kernel_size, kernel_size),0)
    return blurred

def median_blur_image(image :np.ndarray,kernel_size :int )->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.medianBlur(image, kernel_size)
    return blurred

