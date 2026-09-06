import cv2
import numpy as np
import pytest

from image_processor.thresholding import (threshold_image,binary_inverse_threshold,truncation_threshold,to_zero_threshold,adaptive_threshold,otsu_threshold,)

@pytest.fixture
def grayscale_image():
    return np.array([[0, 50, 100, 150],[50, 100, 150, 200],[100, 150, 200, 250],[150, 200, 250, 255],],dtype=np.uint8, )

def test_threshold_image(grayscale_image):
    result = threshold_image(grayscale_image, 127, 255)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8
    assert result[0, 0] == 0
    assert result[0, 3] == 255

def test_threshold_image_rejects_none():
    with pytest.raises(ValueError):
        threshold_image(None)

def test_threshold_image_rejects_invalid_threshold(grayscale_image):
    with pytest.raises(ValueError):
        threshold_image(grayscale_image, -1)
    with pytest.raises(ValueError):
        threshold_image(grayscale_image, 256)

def test_binary_inverse_threshold(grayscale_image):
    result = binary_inverse_threshold(grayscale_image, 127, 255)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8
    assert result[0, 0] == 255
    assert result[0, 3] == 0


def test_binary_inverse_threshold_rejects_none():
    with pytest.raises(ValueError):
        binary_inverse_threshold(None)

def test_truncation_threshold(grayscale_image):
    result = truncation_threshold(grayscale_image, 127)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8
    assert result[0, 0] == 0
    assert result[0, 3] == 127


def test_truncation_threshold_rejects_none():
    with pytest.raises(ValueError):
        truncation_threshold(None)

def test_to_zero_threshold(grayscale_image):
    result = to_zero_threshold(grayscale_image, 127)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8
    assert result[0, 0] == 0
    assert result[0, 3] == 150

def test_to_zero_threshold_rejects_none():
    with pytest.raises(ValueError):
        to_zero_threshold(None)

def test_adaptive_threshold(grayscale_image):
    result = adaptive_threshold(grayscale_image,max_val=255,block_size=3,constant=2,)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8

def test_adaptive_threshold_rejects_none():
    with pytest.raises(ValueError):
        adaptive_threshold(None)

def test_adaptive_threshold_rejects_invalid_block_size(grayscale_image):
    with pytest.raises(ValueError):
        adaptive_threshold(grayscale_image,block_size=2,)
    with pytest.raises(ValueError):
        adaptive_threshold(grayscale_image,block_size=1,)

def test_otsu_threshold(grayscale_image):
    result = otsu_threshold(grayscale_image)
    assert result.shape == grayscale_image.shape
    assert result.dtype == np.uint8

def test_otsu_threshold_rejects_none():
    with pytest.raises(ValueError):
        otsu_threshold(None)

def test_thresholding_rejects_color_image():
    color_image = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        threshold_image(color_image)
    with pytest.raises(ValueError):
        binary_inverse_threshold(color_image)
    with pytest.raises(ValueError):
        truncation_threshold(color_image)
    with pytest.raises(ValueError):
        to_zero_threshold(color_image)
    with pytest.raises(ValueError):
        adaptive_threshold(color_image)
    with pytest.raises(ValueError):
        otsu_threshold(color_image)