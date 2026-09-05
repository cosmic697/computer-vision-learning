# OpenCV Image Toolkit

A beginner-friendly Python project for learning **Computer Vision and Image Processing using OpenCV**.

The goal of this project is not just to use OpenCV functions, but to understand how common computer vision operations work, how they are implemented, and how they can be combined into useful image-processing pipelines.

---

## 🎯 Goals

This project is part of my Computer Vision learning journey.

The main goals are:

- Learn OpenCV through implementation
- Understand image-processing concepts
- Practice NumPy with real computer vision data
- Learn how images are represented and manipulated
- Build reusable image-processing functions
- Write tests for computer vision operations
- Gradually build more advanced computer vision systems

---

# 📚 Feature Roadmap

The toolkit will be developed category by category.

The goal is to complete each category before moving to the next one.

---

## 1. Image I/O & Information

### Image I/O

- [x] Load image
- [x] Save image
- [x] Display image

### Image Information

- [x] Get image dimensions
- [x] Get width
- [x] Get height
- [x] Get number of channels
- [x] Get image data type
- [x] Get pixel value
- [x] Get image statistics
- [x] Check whether image is grayscale
- [x] Check whether image is color
- [x] Support different image formats

---

## 2. Basic Image Transformations

- [x] Convert image to grayscale
- [x] Resize image
- [x] Crop image
- [x] Rotate image
- [x] Flip image horizontally
- [x] Flip image vertically
- [x] Flip both
- [x] Translate image
- [x] Scale image
- [x] Shear image
- [x] Affine transformation
- [x] Perspective transformation
- [x] Add image padding/borders

---

## 3. Image Filtering

- [x] Gaussian blur
- [x] Median blur
- [ ] Average / box blur
- [ ] Bilateral filtering
- [ ] Custom convolution
- [ ] Sharpening
- [ ] Unsharp masking
- [ ] Noise reduction
- [ ] Salt-and-pepper noise removal

---

## 4. Thresholding

- [x] Binary thresholding
- [ ] Binary inverse thresholding
- [ ] Truncation thresholding
- [ ] To-zero thresholding
- [ ] Adaptive thresholding
- [ ] Otsu thresholding
- [ ] Automatic threshold selection

---

## 5. Morphological Operations

- [ ] Erosion
- [ ] Dilation
- [ ] Opening
- [ ] Closing
- [ ] Morphological gradient
- [ ] Top-hat transformation
- [ ] Black-hat transformation
- [ ] Structuring elements

---

## 6. Edge Detection

- [x] Canny edge detection
- [ ] Sobel X
- [ ] Sobel Y
- [ ] Sobel gradient magnitude
- [ ] Scharr operator
- [ ] Laplacian
- [ ] Gradient magnitude
- [ ] Gradient direction

---

## 7. Contours

- [ ] Find contours
- [ ] Draw contours
- [ ] Contour area
- [ ] Contour perimeter
- [ ] Bounding rectangle
- [ ] Rotated bounding rectangle
- [ ] Minimum enclosing circle
- [ ] Convex hull
- [ ] Convexity defects
- [ ] Polygon approximation
- [ ] Contour hierarchy
- [ ] Basic shape detection

---

## 8. Color Processing

- [ ] BGR to RGB
- [ ] BGR to HSV
- [ ] BGR to LAB
- [ ] BGR to YCrCb
- [ ] Color masking
- [ ] Color range detection
- [ ] Histogram calculation
- [ ] Histogram equalization
- [ ] CLAHE
- [ ] Brightness adjustment
- [ ] Contrast adjustment
- [ ] Saturation adjustment

---

## 9. Feature Detection & Description

- [ ] Harris corner detection
- [ ] Shi-Tomasi corner detection
- [ ] FAST
- [ ] ORB
- [ ] SIFT
- [ ] Feature descriptors
- [ ] Feature matching
- [ ] Brute-force matching
- [ ] FLANN matching
- [ ] Feature visualization

---

## 10. Image Segmentation

- [ ] Binary segmentation
- [ ] Color segmentation
- [ ] Region-based segmentation
- [ ] Connected components
- [ ] Watershed
- [ ] GrabCut
- [ ] K-means image segmentation

---

## 11. Geometric Computer Vision

- [ ] Camera calibration
- [ ] Camera matrix
- [ ] Distortion coefficients
- [ ] Image distortion
- [ ] Image undistortion
- [ ] Homography
- [ ] Perspective geometry
- [ ] Epipolar geometry
- [ ] Fundamental matrix
- [ ] Essential matrix
- [ ] Stereo vision
- [ ] Depth estimation
- [ ] Triangulation

---

## 12. Motion & Video Processing

- [ ] Read video
- [ ] Write video
- [ ] Process video frame-by-frame
- [ ] Background subtraction
- [ ] Motion detection
- [ ] Optical flow
- [ ] Lucas-Kanade optical flow
- [ ] Dense optical flow
- [ ] Object tracking
- [ ] Centroid tracking
- [ ] KCF tracking
- [ ] CSRT tracking

---

## 13. Object Detection

- [ ] Template matching
- [ ] Haar cascade detection
- [ ] HOG + SVM
- [ ] Bounding boxes
- [ ] Confidence scores
- [ ] Non-maximum suppression
- [ ] YOLO integration

---

## 14. Image Registration & Stitching

- [ ] Image registration
- [ ] Feature-based alignment
- [ ] Homography-based alignment
- [ ] Image stitching
- [ ] Panorama generation
- [ ] Image blending
- [ ] OpenCV Stitcher
- [ ] Manual panorama pipeline

---

## 15. Image Restoration

- [ ] Noise models
- [ ] Image denoising
- [ ] Inpainting
- [ ] Motion blur concepts
- [ ] Deblurring concepts

---

## 16. Image Analysis & Comparison

- [ ] Image histograms
- [ ] Image moments
- [ ] Mean
- [ ] Variance
- [ ] Minimum / maximum pixel values
- [ ] MSE
- [ ] PSNR
- [ ] SSIM
- [ ] Image comparison

---

## 17. Utilities & Pipelines

- [ ] Batch image processing
- [ ] Folder processing
- [ ] Automatic output directories
- [ ] Image format conversion
- [ ] Image metadata
- [ ] Processing pipelines
- [ ] Configuration support
- [ ] Logging
- [ ] Error handling
- [ ] Input validation
- [ ] Progress reporting

---

## 18. Command Line Interface

Eventually the toolkit will provide a CLI for running image-processing operations without modifying Python code.

Planned features:

- [ ] Command-line image processing
- [ ] Input/output arguments
- [ ] Operation selection
- [ ] Processing pipelines
- [ ] Batch processing
- [ ] CLI help system

---

# 🧪 Testing

Each category will have its own test file.

Current structure:

```text
tests/
├── __init__.py
├── test_io.py
├── test_information.py
├── test_transformations.py
├── test_filtering.py
├── test_thresholding.py
└── test_edges.py


# 🚧 Current Status

### Category 1 — Image I/O & Information
### Category 2 — Image Transformation

**COMPLETED ✅**

All planned features for this category have been implemented and tested.

### Test Status

```text
All tests passing ✅