import cv2
import numpy as np

def detect_edges(image:np.ndarray, lower_threshold:int=100,upper_threshold:int=200)-> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= lower_threshold <= 255:
        raise ValueError("Lower threshold must be between 0 and 255.")
    if not 0 <= upper_threshold <= 255:
        raise ValueError("Upper threshold must be between 0 and 255.")
    edge = cv2.Canny(image,lower_threshold,upper_threshold)
    return edge

