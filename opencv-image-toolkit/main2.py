import cv2
import numpy as np

from image_processor.morphology import hit_or_miss


# Create binary image
image = np.zeros((100, 100), dtype=np.uint8)

# White L-shaped pattern
image[40, 40:43] = 255
image[40:43, 40] = 255

# Create a white 3x3 block
image[40:43, 40:43] = 255


# Look for this exact pattern:
#
#   0  0  0
#   0  1  0
#   0  0  0
#
# 1  = foreground
# -1 = background
# 0  = don't care
kernel = np.array([
    [ 1,  1,  0],
    [ 1, -1, -1],
    [ 0, -1, -1]
], dtype=np.int8)


result = hit_or_miss(image, kernel)


cv2.imwrite(
    "examples/output/hit_or_miss_input.jpg",
    image
)

cv2.imwrite(
    "examples/output/hit_or_miss.jpg",
    result
)


print("Input shape:", image.shape)
print("Result shape:", result.shape)
print("Result dtype:", result.dtype)
print("Non-zero pixels:", np.count_nonzero(result))