import cv2
import numpy as np

def create_structuring_element(shape:int=cv2.MORPH_RECT,kernel_size:int=3)->np.ndarray:
    if not isinstance(kernel_size,int):
        raise TypeError("kernel_size must ba integer.")
    if kernel_size<=0 or kernel_size%2==0:
        raise ValueError("Kernel size must a positive odd number.")
    if shape not in(cv2.MORPH_RECT,cv2.MORPH_ELLIPSE,cv2.MORPH_CROSS):
        raise ValueError("unsupported structuring element shape.")
    kernel = cv2.getStructuringElement(shape,(kernel_size,kernel_size))
    return kernel

def erode_image(image:np.ndarray,kernel:np.ndarray,iterations:int=1)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel is None:
        raise ValueError("Kernel cannot be none.")
    if not isinstance(kernel,np.ndarray):
        raise TypeError("kernel must be a Numpy array.")
    if not isinstance(iterations,int):
        raise TypeError("iterations must be a integer value.")
    if iterations<=0:
        raise ValueError("interations must be positive.")
    result = cv2.erode(image,kernel,iterations=iterations)
    return result

def dilate_image(image:np.ndarray,kernel:np.ndarray,iterations:int=1)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel is None:
        raise ValueError("Kernel cannot be none.")
    if not isinstance(kernel,np.ndarray):
        raise TypeError("kernel must be a Numpy array.")
    if not isinstance(iterations,int):
        raise TypeError("iterations must be a integer value.")
    if iterations<=0:
        raise ValueError("interations must be positive.")
    result = cv2.dilate(image,kernel,iterations=iterations)
    return result

def open_image(image:np.ndarray,kernel:np.ndarray,iterations:int=1)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel is None:
        raise ValueError("Kernel cannot be none.")
    if not isinstance(kernel,np.ndarray):
        raise TypeError("kernel must be a Numpy array.")
    if not isinstance(iterations,int):
        raise TypeError("iterations must be a integer value.")
    if iterations<=0:
        raise ValueError("interations must be positive.")
    result = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel,iterations=iterations)
    return result

def close_image(image:np.ndarray,kernel:np.ndarray,iterations:int=1)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel is None:
        raise ValueError("Kernel cannot be none.")
    if not isinstance(kernel,np.ndarray):
        raise TypeError("kernel must be a Numpy array.")
    if not isinstance(iterations,int):
        raise TypeError("iterations must be a integer value.")
    if iterations<=0:
        raise ValueError("interations must be positive.")
    result = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel,iterations=iterations)
    return result

