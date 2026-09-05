import cv2
import numpy as np

def threshold_image(image:np.ndarray , threshold :int =127 , max_val:int =255)-> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= threshold <= 255:
        raise ValueError("Threshold must be between 0 and 255.")
    if not 0 <= max_val <= 255:
        raise ValueError("Maximum value must be between 0 and 255.")
    if len(image.shape) != 2:
        raise ValueError("Thresholding requires a grayscale image.")
    _,thresholded = cv2.threshold(image,threshold,max_val,cv2.THRESH_BINARY)
    return thresholded