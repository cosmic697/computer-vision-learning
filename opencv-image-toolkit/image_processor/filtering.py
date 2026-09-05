import cv2
import numpy as np

def gaussian_blur_image(image: np.ndarray,kernel_size: int) -> np.ndarray:
    # Larger kernel → stronger smoothing
    # Kernel size must be odd so there is a center pixel.
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.GaussianBlur(image,(kernel_size, kernel_size),0)
    return blurred

def median_blur_image(image:np.ndarray,kernel_size:int)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.medianBlur(image,kernel_size)
    return blurred

def average_blur_image(image:np.ndarray,kernel_size:int)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.blur(image,(kernel_size,kernel_size))
    return blurred

def bilateral_blur_image(image:np.ndarray,diameter:int,sigma_color:float,sigma_space:float)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(diameter, int):
        raise ValueError("Diameter must be an integer.")
    if not isinstance(sigma_color,(int,float)):
        raise ValueError("sigma_color must be a number.")
    if not isinstance(sigma_space,(int,float)):
        raise ValueError("sigma_space must be a number.")
    if diameter <= 0:
        raise ValueError("diameter must be positive.")
    if sigma_color <=0:
        raise ValueError("sigma_color must be a positive.")
    if sigma_space <=0:
        raise ValueError("sigma_space must be positive.")
    blurred = cv2.bilateralFilter(image,diameter,sigma_color,sigma_space)
    return blurred

def custom_convolution(image: np.ndarray,kernel: np.ndarray)->np.ndarray:
    if image is None:
        raise ValueError("image cannot be None.")
    if kernel is None:
        raise ValueError("kernel cannot be None.")
    if not isinstance(kernel, np.ndarray):
        raise TypeError("Kernel must be a NumPy array.")
    if kernel.ndim != 2:
        raise ValueError("kernel must be a 2D array.")
    if kernel.shape[0]%2==0 or kernel.shape[1]%2==0:
        raise ValueError("kernel dimensions must be odd.")
    result = cv2.filter2D(image , -1, kernel)
    return result

def sharpen_image(image : np.ndarray)->np.ndarray:
    if image is None:
        raise ValueError("image cannot be None.")
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float32)
    sharpened = cv2.filter2D(image , -1 , kernel)
    return sharpened

def unsharp_mask(image : np.ndarray , kernel_size:int =5, amount:float =1.0)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size,int):
        raise TypeError("Kernel size must be an integer.")
    if not isinstance(amount ,(int , float)):
        raise TypeError("Amount must be a number.")
    if kernel_size<=0 or kernel_size%2==0:
        raise ValueError("Kernel size must be a positive odd number.")
    if amount<0:
        raise ValueError("Amount cannot be negative")
    blurred = cv2.GaussianBlur(image , (kernel_size ,kernel_size),0)
    image_float = image.astype(np.float32)
    blurred_float = blurred.astype(np.float32)
    mask = image_float - blurred_float
    sharpened = image_float + amount*mask
    sharpened = np.clip(sharpened,0,255).astype(np.uint8)
    return sharpened

def reduce_noise(image:np.ndarray,kernel_size:int =5)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size,int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size<=0 or kernel_size%2==0:
        raise ValueError("kernel size must be a positive odd number")
    reduced = cv2.GaussianBlur(image , (kernel_size,kernel_size),0)
    return reduced

def remove_salt_pepper_noise(image:np.ndarray,kernel_size:int=5)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(kernel_size,int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size<=0 or kernel_size%2==0:
        raise ValueError("Kernel size must be a positive odd number.")
    denoised = cv2.medianBlur(image , kernel_size)
    return denoised




    






