import cv2
import numpy as np
import pytest

from image_processor.morphology import (create_structuring_element,erode_image,dilate_image,open_image,close_image,morphological_gradient,top_hat,black_hat,hit_or_miss,)

@pytest.fixture
def binary_image():
    image = np.zeros((7, 7), dtype=np.uint8)
    image[2:5, 2:5] = 255
    return image

@pytest.fixture
def kernel():
    """Create a 3x3 rectangular structuring element."""
    return create_structuring_element(cv2.MORPH_RECT, 3)

def test_create_structuring_element():
    kernel = create_structuring_element(cv2.MORPH_RECT,3)
    assert isinstance(kernel, np.ndarray)
    assert kernel.shape == (3, 3)
    assert kernel.dtype == np.uint8

def test_create_structuring_element_rejects_invalid_size():
    with pytest.raises(ValueError):
        create_structuring_element( cv2.MORPH_RECT, 2)
    with pytest.raises(ValueError):
        create_structuring_element(cv2.MORPH_RECT,0)

def test_create_structuring_element_rejects_invalid_type():
    with pytest.raises(TypeError):
        create_structuring_element(cv2.MORPH_RECT,3.5)

def test_erode_image(binary_image, kernel):
    result = erode_image( binary_image, kernel)
    assert result.shape == binary_image.shape
    assert result.dtype == np.uint8
    assert np.count_nonzero(result) <= np.count_nonzero(binary_image)

def test_erode_image_rejects_none(binary_image, kernel):
    with pytest.raises(ValueError):
        erode_image(None, kernel)
    with pytest.raises(ValueError):
        erode_image(binary_image, None)


def test_erode_image_rejects_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        erode_image(binary_image,kernel,1.5)
    with pytest.raises(ValueError):
        erode_image(binary_image,kernel,0 )

def test_dilate_image(binary_image, kernel):
    result = dilate_image( binary_image, kernel )
    assert result.shape == binary_image.shape
    assert result.dtype == np.uint8
    assert np.count_nonzero(result) >= np.count_nonzero(binary_image)

def test_dilate_image_rejects_none(binary_image, kernel):
    with pytest.raises(ValueError):
        dilate_image(None, kernel)
    with pytest.raises(ValueError):
        dilate_image(binary_image, None)


def test_dilate_image_rejects_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        dilate_image(binary_image,kernel,1.5)
    with pytest.raises(ValueError):
        dilate_image(binary_image,kernel,0 )

def test_open_image(binary_image, kernel):
    result = open_image(binary_image,kernel )
    assert result.shape == binary_image.shape
    assert result.dtype == np.uint8

def test_open_image_rejects_none(binary_image, kernel):
    with pytest.raises(ValueError):
        open_image(None, kernel)
    with pytest.raises(ValueError):
        open_image(binary_image, None)

def test_open_image_rejects_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        open_image(binary_image,kernel,1.5)
    with pytest.raises(ValueError):
        open_image(binary_image,kernel,0)

def test_close_image(binary_image, kernel):
    result = close_image(binary_image,kernel)
    assert result.shape == binary_image.shape
    assert result.dtype == np.uint8


def test_close_image_rejects_none(binary_image, kernel):
    with pytest.raises(ValueError):
        close_image(None, kernel)
    with pytest.raises(ValueError):
        close_image(binary_image, None)

def test_close_image_rejects_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        close_image(binary_image,kernel,1.5)
    with pytest.raises(ValueError):
        close_image(binary_image,kernel,0)

def test_morphological_gradient(binary_image, kernel):
    result = morphological_gradient(binary_image,kernel)
    assert isinstance(result, np.ndarray)
    assert result.shape == binary_image.shape

def test_morphological_gradient_none_image(kernel):
    with pytest.raises(ValueError):
        morphological_gradient(None, kernel)

def test_morphological_gradient_none_kernel(binary_image):
    with pytest.raises(ValueError):
        morphological_gradient(binary_image, None)

def test_morphological_gradient_invalid_kernel(binary_image):
    with pytest.raises(TypeError):
        morphological_gradient(binary_image,[[1, 1], [1, 1]])

def test_morphological_gradient_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        morphological_gradient(binary_image,kernel,iterations=1.5)

def test_morphological_gradient_zero_iterations(binary_image,kernel):
    with pytest.raises(ValueError):
        morphological_gradient(binary_image,kernel,iterations=0)

def test_top_hat(binary_image, kernel):
    result = top_hat(binary_image,kernel)
    assert isinstance(result, np.ndarray)
    assert result.shape == binary_image.shape

def test_top_hat_none_image(kernel):
    with pytest.raises(ValueError):
        top_hat(None, kernel)

def test_top_hat_none_kernel(binary_image):
    with pytest.raises(ValueError):
        top_hat(binary_image, None)

def test_top_hat_invalid_kernel(binary_image):
    with pytest.raises(TypeError):
        top_hat(binary_image,[[1, 1], [1, 1]])

def test_top_hat_invalid_iterations(binary_image,kernel):
    with pytest.raises(TypeError):
        top_hat(binary_image,kernel,iterations=1.5)

def test_top_hat_zero_iterations(binary_image,kernel):
    with pytest.raises(ValueError):
        top_hat(binary_image,kernel,iterations=0)

def test_black_hat(binary_image, kernel):
    result = black_hat( binary_image, kernel)
    assert isinstance(result, np.ndarray)
    assert result.shape == binary_image.shape

def test_black_hat_none_image(kernel):
    with pytest.raises(ValueError):
        black_hat(None, kernel)

def test_black_hat_none_kernel(binary_image):
    with pytest.raises(ValueError):
        black_hat(binary_image, None)

def test_black_hat_invalid_kernel(binary_image):
    with pytest.raises(TypeError):
        black_hat(binary_image,[[1, 1], [1, 1]])

def test_black_hat_invalid_iterations( binary_image, kernel):
    with pytest.raises(TypeError):
        black_hat(binary_image,kernel,iterations=1.5)

def test_black_hat_zero_iterations( binary_image, kernel):
    with pytest.raises(ValueError):
        black_hat(binary_image,kernel,iterations=0 )

@pytest.fixture
def hitmiss_image():
    image = np.zeros((7, 7), dtype=np.uint8)
    image[2:5, 2:5] = 255
    return image

@pytest.fixture
def hitmiss_kernel():
    return np.array([[0,  0, 0],[0,  1, 0],[0,  0, 0]], dtype=np.int8)

def test_hit_or_miss(hitmiss_image,hitmiss_kernel):
    result = hit_or_miss(hitmiss_image,hitmiss_kernel )
    assert isinstance(result, np.ndarray)
    assert result.shape == hitmiss_image.shape

def test_hit_or_miss_none_image(hitmiss_kernel):
    with pytest.raises(ValueError):
        hit_or_miss(None,hitmiss_kernel)

def test_hit_or_miss_none_kernel(hitmiss_image):
    with pytest.raises(ValueError):
        hit_or_miss(hitmiss_image,None)

def test_hit_or_miss_invalid_kernel_type(hitmiss_image):
    with pytest.raises(TypeError):
        hit_or_miss(hitmiss_image,[[0, 0, 0],[0, 1, 0],[0, 0, 0]])

def test_hit_or_miss_invalid_kernel_dimension(hitmiss_image):
    kernel = np.array([1, 1, 1])
    with pytest.raises(ValueError):
        hit_or_miss(hitmiss_image,kernel)

def test_hit_or_miss_invalid_kernel_values( hitmiss_image):
    kernel = np.array([[0, 0, 0],[0, 2, 0],[0, 0, 0]])
    with pytest.raises(ValueError):
        hit_or_miss(hitmiss_image,kernel)

def test_hit_or_miss_color_image(hitmiss_kernel):
    image = np.zeros((7, 7, 3),dtype=np.uint8)
    with pytest.raises(ValueError):
        hit_or_miss(image,hitmiss_kernel )

def test_hit_or_miss_invalid_dtype(hitmiss_kernel):
    image = np.zeros((7, 7),dtype=np.float32)
    with pytest.raises(ValueError):
        hit_or_miss(image,hitmiss_kernel)