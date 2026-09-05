import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError ("fail to load the image.")
    return image

def save_image(image: np.ndarray, path: str) -> None:
    if image is None:
        raise ValueError("Image cannot be None.")
    success = cv2.imwrite(path, image)
    if not success:
        raise ValueError("Failed to save the image.")

def display_image(image: np.ndarray, window_name: str = "Image") -> None:
    if image is None:
        raise ValueError("Image cannot be None.")
    cv2.imshow(window_name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

