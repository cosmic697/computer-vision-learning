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


def binary_inverse_threshold(image:np.ndarray , threshold :int =127 , max_val:int =255)-> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= threshold <= 255:
        raise ValueError("Threshold must be between 0 and 255.")
    if not 0 <= max_val <= 255:
        raise ValueError("Maximum value must be between 0 and 255.")
    if len(image.shape) != 2:
        raise ValueError("Thresholding requires a grayscale image.")
    _,thresholded = cv2.threshold(image,threshold,max_val,cv2.THRESH_BINARY_INV)
    return thresholded

def truncation_threshold(image:np.ndarray , threshold :int =127)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= threshold <= 255:
        raise ValueError("Threshold must be between 0 and 255.")
    if len(image.shape) != 2:
        raise ValueError("Thresholding requires a grayscale image.")
    _,thresholded = cv2.threshold(image,threshold,255,cv2.THRESH_TRUNC)
    return thresholded

def to_zero_threshold(image:np.ndarray , threshold :int =127)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= threshold <= 255:
        raise ValueError("Threshold must be between 0 and 255.")
    if len(image.shape) != 2:
        raise ValueError("Thresholding requires a grayscale image.")
    _,thresholded = cv2.threshold(image,threshold,255,cv2.THRESH_TOZERO)
    return thresholded

def adaptive_threshold( image: np.ndarray, max_val: int = 255, adaptive_method: int = cv2.ADAPTIVE_THRESH_GAUSSIAN_C, threshold_type: int = cv2.THRESH_BINARY, block_size: int = 11, constant: int = 2) -> np.ndarray:
    if image is None:
          raise ValueError("Image cannot be None.")
    if not 0 <= max_val <= 255:
        raise ValueError("max value must be between 0 and 255.")
    if len(image.shape) != 2:
        raise ValueError("Thresholding requires a grayscale image.")
    if block_size<=1 or block_size%2==0:
        raise ValueError("block size must be an odd number greater than one.")
    result = cv2.adaptiveThreshold(image,max_val,adaptive_method,threshold_type,block_size,constant)
    return result

def otsu_threshold(image: np.ndarray,max_val: int = 255) -> np.ndarray:
    if image is None:
         raise ValueError("Image cannot be None.")
    if not 0 <= max_val <= 255:
         raise ValueError("max value must be between 0 and 255.")
    if len(image.shape) != 2:
         raise ValueError("Thresholding requires a grayscale image.")
    _, result = cv2.threshold(image,0,max_val,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return result


