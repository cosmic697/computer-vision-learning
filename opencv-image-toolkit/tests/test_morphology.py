import cv2
import numpy as np
import pytest

from image_processor.morphology import (create_structuring_element,erode_image,dilate_image,open_image,close_image,)

@pytest.fixture
def binary_image():
    """Create a small binary image for testing."""
    return np.array([[0, 0, 0, 0, 0],[0, 255, 255, 255, 0],[0, 255, 255, 255, 0],[0, 255, 255, 255, 0],[0, 0, 0, 0, 0],], dtype=np.uint8,)

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