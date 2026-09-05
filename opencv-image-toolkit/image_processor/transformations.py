import cv2
import numpy as np

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

def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

def flip_horizontal(image:np.ndarray)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    flipped = cv2.flip(image , 1)
    return flipped

def flip_vertical(image:np.ndarray)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    flipped = cv2.flip(image , 0)
    return flipped

def flip_both(image:np.ndarray)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    flipped = cv2.flip(image , -1)
    return flipped

def translate_image(image:np.ndarray,tx :int ,ty:int)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(tx, (int, float)):
        raise TypeError("tx must be a number.")
    if not isinstance(ty, (int, float)):
        raise TypeError("ty must be a number.")
    height , width = image.shape[:2]
    matrix = np.float32(([1,0,tx],[0,1,ty]))
    translated = cv2.warpAffine(image , matrix , (width,height))
    return translated

def scale_image(image:np.ndarray,tx :float ,ty:float)->np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(tx, (int, float)):
        raise TypeError("tx must be a number.")
    if not isinstance(ty, (int, float)):
        raise TypeError("ty must be a number.")
    if(tx<=0 or ty<=0):
        raise ValueError("Scale factors must be positive.")
    height , width = image.shape[:2]
    new_height = int(height * ty)
    new_width = int(width * ty)
    scaled= cv2.resize(image ,(new_width,new_height))
    return scaled

def shear_image(image: np.ndarray,shear_x: float = 0.0,shear_y: float = 0.0) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not isinstance(shear_x, (int, float)):
        raise TypeError("shear_x must be a number.")
    if not isinstance(shear_y, (int, float)):
        raise TypeError("shear_y must be a number.")
    height, width = image.shape[:2]
    matrix = np.float32([[1, shear_x, 0],[shear_y, 1, 0]])
    sheared = cv2.warpAffine(image,matrix,(width, height))
    return sheared

def affine_transform(image: np.ndarray,source_points: np.ndarray,destination_points: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if source_points is None or destination_points is None:
        raise ValueError("Source and destination points cannot be None.")
    if source_points.shape != (3, 2):
        raise ValueError("source_points must contain exactly 3 points.")
    if destination_points.shape != (3, 2):
        raise ValueError("destination_points must contain exactly 3 points.")
    height, width = image.shape[:2]
    matrix = cv2.getAffineTransform(np.float32(source_points),np.float32(destination_points))
    transformed = cv2.warpAffine(image,matrix,(width, height))
    return transformed

def perspective_transform(image: np.ndarray,source_points: np.ndarray,destination_points: np.ndarray) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if source_points is None or destination_points is None:
        raise ValueError("Source and destination points cannot be None.")
    if source_points.shape != (4, 2):
        raise ValueError("source_points must contain exactly 4 points.")
    if destination_points.shape != (4, 2):
        raise ValueError("destination_points must contain exactly 4 points.")
    height, width = image.shape[:2]
    matrix = cv2.getPerspectiveTransform(np.float32(source_points),np.float32(destination_points))
    transformed = cv2.warpPerspective(image,matrix,(width, height))
    return transformed
   
def add_padding(image: np.ndarray,top: int,bottom: int,left: int,right: int,border_type: int = cv2.BORDER_CONSTANT,value: int = 0) -> np.ndarray:
    if image is None:
        raise ValueError("Image cannot be None.")
    if not all(isinstance(value_, int)for value_ in [top, bottom, left, right]):
        raise TypeError("Padding values must be integers.")
    if top < 0 or bottom < 0 or left < 0 or right < 0:
        raise ValueError("Padding values cannot be negative.")
    padded = cv2.copyMakeBorder(image , top, bottom , left , right , border_type,value=value)
    return padded
