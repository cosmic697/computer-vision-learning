import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError ("fail to load the image.")
    return image

def save_image(image: np.ndarray, file: str) -> None:
    if image is None:
        raise ValueError("Image cannot be None.")
    success = cv2.imwrite(file, image)
    if not success:
        raise ValueError("Failed to save the image.")
       
def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

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

def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    #more the kernel size the smoother the image the more the content lost
    #kernel size should be odd so that we have a correct center pixel
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.GaussianBlur(image,(kernel_size, kernel_size),0)
    return blurred

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

def detect_edges(image:np.ndarray, lower_threshold:int=100,upper_threshold:int=200)-> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not 0 <= lower_threshold <= 255:
        raise ValueError("Lower threshold must be between 0 and 255.")
    if not 0 <= upper_threshold <= 255:
        raise ValueError("Upper threshold must be between 0 and 255.")
    edge = cv2.Canny(image,lower_threshold,upper_threshold)
    return edge

def median_blur_image(image :np.ndarray,kernel_size :int )->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")
    blurred = cv2.medianBlur(image, kernel_size)
    return blurred

    

    





     
     

    
