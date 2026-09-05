from image_processor import (
    load_image,
    save_image,
    to_grayscale,
    resize_image,
    crop_image,
    rotate_image,
    blur_image,
    threshold_image,
    detect_edges,
    median_blur_image,
)


image = load_image("examples/input/test.jpg")

gray = to_grayscale(image)
save_image(gray, "examples/output/gray.jpg")

resized = resize_image(image, 300, 200)
save_image(resized, "examples/output/resized.jpg")

cropped = crop_image(image, 100, 50, 400, 250)
save_image(cropped, "examples/output/cropped.jpg")

rotated = rotate_image(image, 45)
save_image(rotated, "examples/output/rotated.jpg")

blurred = blur_image(image, 5)
save_image(blurred, "examples/output/blurred.jpg")

thresholded = threshold_image(gray)
save_image(thresholded, "examples/output/thresholded.jpg")

edges = detect_edges(gray)
save_image(edges, "examples/output/edges.jpg")

median_blurred = median_blur_image(image, 5)
save_image(median_blurred, "examples/output/median_blurred.jpg")

print("Image processing completed successfully.")