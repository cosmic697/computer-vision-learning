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

def morphological_gradient(image:np.ndarray,kernel:np.ndarray,iterations:int=1)->np.ndarray:
    '''Gradient = Dilation - Erosion'''
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
    result = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel,iterations=iterations)
    return result

def top_hat(image: np.ndarray,kernel: np.ndarray,iterations: int = 1) -> np.ndarray:
    '''TopHat = Original - Opening'''
    '''Opening = Erosion → Dilation'''
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
    result = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel,iterations=iterations)
    return result

def black_hat(image: np.ndarray,kernel: np.ndarray,iterations: int = 1) -> np.ndarray:
    '''BlackHat = Closing - Original'''
    '''Closing = Dilation → Erosion'''
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
    result = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel,iterations=iterations)
    return result

def hit_or_miss(image: np.ndarray,kernel: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel is None:
        raise ValueError("Kernel cannot be None.")
    if not isinstance(kernel, np.ndarray):
        raise TypeError("Kernel must be a NumPy array.")
    if kernel.ndim != 2:
        raise ValueError("Kernel must be a 2D array.")
    if not np.all(np.isin(kernel, [-1, 0, 1])):
        raise ValueError("Kernel values must be -1, 0, or 1.")
    if len(image.shape) != 2:
        raise ValueError("Hit-or-miss requires a single-channel binary image.")
    if image.dtype != np.uint8:
        raise ValueError("Hit-or-miss requires an 8-bit binary image.")
    result = cv2.morphologyEx( image, cv2.MORPH_HITMISS, kernel)
    return result
