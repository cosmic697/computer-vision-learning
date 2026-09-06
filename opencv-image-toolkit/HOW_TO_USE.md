# How to Use OpenCV Image Toolkit

This guide explains how to use the OpenCV Image Toolkit through its command-line interface (CLI).

---

## Table of Contents

1. [Requirements](#1-requirements)
2. [Starting the Application](#2-starting-the-application)
3. [Main Menu](#3-main-menu)
4. [Image I/O](#4-image-io)
5. [Image Information](#5-image-information)
6. [Transformations](#6-transformations)
7. [Filtering](#7-filtering)
8. [Thresholding](#8-thresholding)
9. [Morphological Operations](#9-morphological-operations)
10. [Edge Detection](#10-edge-detection)
11. [Typical Workflow](#11-typical-workflow)
12. [Input Guidelines](#12-input-guidelines)
13. [Common Errors](#13-common-errors)
14. [Exiting the Application](#14-exiting-the-application)
15. [Current Feature Categories](#15-current-feature-categories)
16. [Future Improvements](#16-future-improvements)

---

# 1. Requirements

Before using the application, make sure you have:

* Python 3 installed
* OpenCV installed
* NumPy installed

The required Python packages are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

If you are using a virtual environment, activate it before running the application.

---

# 2. Starting the Application

Open a terminal in the project root:

```text
opencv-image-toolkit/
```

Run:

```bash
python3 main.py
```

The application will display the main menu.

---

# 3. Main Menu

The main menu provides access to all currently implemented feature categories:

```text
==================================================
              OpenCV Image Toolkit
==================================================

1. Image I/O
2. Image Information
3. Transformations
4. Filtering
5. Thresholding
6. Morphological Operations
7. Edge Detection
8. Exit
```

Select an option by entering its corresponding number.

For example:

```text
Choose an option: 3
```

opens the Transformations menu.

---

# 4. Image I/O

The Image I/O menu contains operations for loading, saving, and displaying images.

```text
1. Load Image
2. Save Image
3. Display Image
4. Back
```

## 4.1 Load Image

Select:

```text
1. Load Image
```

Enter the path to the image.

Example:

```text
Enter image path: examples/input/test.jpg
```

The application will load the image and display basic information such as its shape and data type.

Example:

```text
Image loaded successfully.

Shape: (720, 1280, 3)
Data type: uint8
```

The loaded image becomes the current image and can then be processed using other operations.

---

## 4.2 Save Image

Select:

```text
2. Save Image
```

The application asks for the output path.

Example:

```text
Enter output path: examples/output/result.jpg
```

The currently loaded and processed image will be saved at the specified location.

---

## 4.3 Display Image

Select:

```text
3. Display Image
```

The currently loaded image will open in an OpenCV window.

Press:

```text
ESC
```

to close the image window.

---

# 5. Image Information

The Image Information menu provides information about the currently loaded image.

```text
1. Dimensions
2. Width
3. Height
4. Channels
5. Data Type
6. Pixel Value
7. Statistics
8. Check Grayscale
9. Check Color
10. Back
```

---

## 5.1 Dimensions

Returns the complete shape of the image.

Example:

```text
Dimensions: (720, 1280, 3)
```

For a color image:

```text
(height, width, channels)
```

For a grayscale image:

```text
(height, width)
```

---

## 5.2 Width

Returns the image width in pixels.

Example:

```text
Width: 1280
```

---

## 5.3 Height

Returns the image height in pixels.

Example:

```text
Height: 720
```

---

## 5.4 Channels

Returns the number of image channels.

Examples:

```text
Channels: 3
```

for a color image, or:

```text
Channels: 1
```

for a grayscale image.

---

## 5.5 Data Type

Displays the NumPy data type used to represent the image.

A common image type is:

```text
Data type: uint8
```

---

## 5.6 Pixel Value

Returns the pixel value at a specific coordinate.

The CLI asks for:

```text
x coordinate
y coordinate
```

Example:

```text
Enter x coordinate: 100
Enter y coordinate: 200
```

Example output:

```text
Pixel value at (100, 200): [120 85 40]
```

For color images, the returned value represents the channel values at that pixel.

> Note: Image coordinates are zero-based.

---

## 5.7 Statistics

Displays basic image statistics:

```text
Image Statistics:

min: ...
max: ...
mean: ...
std: ...
```

The statistics include:

* Minimum pixel value
* Maximum pixel value
* Mean pixel value
* Standard deviation

---

## 5.8 Check Grayscale

Checks whether the currently loaded image is represented as a grayscale image.

Example:

```text
Grayscale image: True
```

---

## 5.9 Check Color

Checks whether the currently loaded image is represented as a color image.

Example:

```text
Color image: True
```

---

# 6. Transformations

The Transformations menu contains geometric and basic image transformations.

```text
1. Resize
2. Crop
3. Rotate
4. Grayscale
5. Horizontal Flip
6. Vertical Flip
7. Flip Both
8. Translate
9. Scale
10. Shear
11. Affine Transform
12. Perspective Transform
13. Add Padding
14. Back
```

---

## 6.1 Resize

Changes the image dimensions.

The application asks for:

```text
new width
new height
```

Example:

```text
Enter new width: 800
Enter new height: 600
```

---

## 6.2 Crop

Extracts a rectangular region from an image.

The application asks for:

```text
x1
y1
x2
y2
```

Example:

```text
Enter x1: 100
Enter y1: 100
Enter x2: 500
Enter y2: 400
```

The selected region becomes the resulting image.

---

## 6.3 Rotate

Rotates the image around its center.

Example:

```text
Enter rotation angle: 90
```

Positive and negative angles can be used.

---

## 6.4 Grayscale

Converts a color image into a grayscale image.

Select:

```text
4. Grayscale
```

The resulting image contains a single grayscale channel.

This operation is particularly useful before operations such as:

* Thresholding
* Edge Detection
* Morphological Processing

---

## 6.5 Horizontal Flip

Flips the image horizontally.

This mirrors the image from left to right.

---

## 6.6 Vertical Flip

Flips the image vertically.

This mirrors the image from top to bottom.

---

## 6.7 Flip Both

Flips the image along both axes.

---

## 6.8 Translate

Moves the image horizontally and/or vertically.

The application asks for:

```text
x translation
y translation
```

Example:

```text
Enter x translation: 50
Enter y translation: 25
```

---

## 6.9 Scale

Changes the size of the image using horizontal and vertical scale factors.

Example:

```text
Enter horizontal scale: 1.5
Enter vertical scale: 1.5
```

A value greater than `1` enlarges the image.

A value between `0` and `1` reduces the image.

---

## 6.10 Shear

Applies a shear transformation.

The application asks for:

```text
horizontal shear
vertical shear
```

Example:

```text
Enter horizontal shear: 0.2
Enter vertical shear: 0
```

---

## 6.11 Affine Transform

Applies an affine transformation using three source points and three destination points.

The application asks for:

```text
3 source points
3 destination points
```

Each point contains:

```text
x
y
```

Example:

```text
Source point 1 x: 0
Source point 1 y: 0

Source point 2 x: 500
Source point 2 y: 0

Source point 3 x: 0
Source point 3 y: 500
```

The same process is then repeated for the destination points.

---

## 6.12 Perspective Transform

Applies a perspective transformation using four source points and four destination points.

This is useful for operations such as:

* Perspective correction
* Document rectification
* Transforming quadrilateral regions

The application asks for four source points and four destination points.

---

## 6.13 Add Padding

Adds borders around an image.

The application asks for:

```text
top
bottom
left
right
```

Example:

```text
Enter top padding: 20
Enter bottom padding: 20
Enter left padding: 10
Enter right padding: 10
```

---

# 7. Filtering

The Filtering menu contains smoothing, sharpening, convolution, and noise-reduction operations.

```text
1. Gaussian Blur
2. Median Blur
3. Average Blur
4. Bilateral Filter
5. Custom Convolution
6. Sharpening
7. Unsharp Mask
8. Noise Reduction
9. Remove Salt-and-Pepper Noise
10. Back
```

---

## 7.1 Gaussian Blur

Applies Gaussian smoothing.

The application asks for an odd kernel size.

Example:

```text
Enter kernel size: 5
```

Valid examples include:

```text
3
5
7
9
```

---

## 7.2 Median Blur

Applies median filtering.

It is particularly useful for reducing certain types of noise.

Example:

```text
Enter kernel size: 5
```

---

## 7.3 Average Blur

Applies an averaging filter over a local neighborhood.

Example:

```text
Enter kernel size: 3
```

---

## 7.4 Bilateral Filter

Applies bilateral filtering while attempting to preserve edges.

The application asks for:

```text
diameter
sigma color
sigma space
```

Example:

```text
Enter diameter: 9
Enter sigma color: 75
Enter sigma space: 75
```

---

## 7.5 Custom Convolution

Allows the user to enter a custom convolution kernel.

First enter the kernel size.

Example:

```text
Enter kernel size (odd number): 3
```

Then enter each row of the kernel.

Example:

```text
Row 1: 0 -1 0
Row 2: -1 5 -1
Row 3: 0 -1 0
```

The kernel must have odd dimensions.

---

## 7.6 Sharpening

Applies a predefined sharpening kernel.

No additional parameters are required.

---

## 7.7 Unsharp Mask

Applies unsharp masking for image sharpening.

The application asks for:

```text
kernel size
sharpening amount
```

Example:

```text
Enter kernel size: 5
Enter sharpening amount: 1.0
```

---

## 7.8 Noise Reduction

Applies Gaussian smoothing to reduce image noise.

Example:

```text
Enter kernel size: 5
```

---

## 7.9 Remove Salt-and-Pepper Noise

Uses median filtering to reduce salt-and-pepper noise.

Example:

```text
Enter kernel size: 5
```

---

# 8. Thresholding

The Thresholding menu provides several techniques for converting or segmenting grayscale images based on pixel intensity.

```text
1. Binary Threshold
2. Binary Inverse Threshold
3. Truncation Threshold
4. To Zero Threshold
5. Adaptive Threshold
6. Otsu Threshold
7. Back
```

Most thresholding operations require a grayscale image.

If the input image is a color image, convert it to grayscale first:

```text
Transformations
→ Grayscale
```

---

## 8.1 Binary Threshold

Binary thresholding converts a grayscale image into a binary image based on a threshold value.

The application asks for:

```text
threshold
maximum value
```

Example:

```text
Enter threshold (0-255): 127
Enter maximum value (0-255): 255
```

Pixels above the threshold are assigned the maximum value, while the remaining pixels are assigned zero.

---

## 8.2 Binary Inverse Threshold

Binary inverse thresholding performs the opposite operation of binary thresholding.

Pixels above the threshold are assigned zero, while pixels at or below the threshold are assigned the maximum value.

Example:

```text
Enter threshold (0-255): 127
Enter maximum value (0-255): 255
```

This can be useful when the foreground and background need to be inverted.

---

## 8.3 Truncation Threshold

Truncation thresholding limits pixel values above the specified threshold.

Pixels greater than the threshold are replaced by the threshold value.

Example:

```text
Enter threshold (0-255): 127
```

This preserves lower intensity values while limiting higher intensity values.

---

## 8.4 To Zero Threshold

To Zero thresholding sets pixels below the threshold to zero.

Pixels greater than or equal to the threshold retain their original values.

Example:

```text
Enter threshold (0-255): 127
```

This can be useful for removing low-intensity regions while preserving brighter regions.

---

## 8.5 Adaptive Threshold

Adaptive thresholding calculates the threshold value locally instead of using one global threshold for the entire image.

The application asks for:

```text
maximum value
block size
constant
```

The block size must be a positive odd number greater than one.

Example:

```text
Enter maximum value (0-255): 255
Enter block size: 11
Enter constant: 2
```

Adaptive thresholding is useful when the image contains uneven or changing illumination.

---

## 8.6 Otsu Threshold

Otsu thresholding automatically determines a suitable global threshold from the image histogram.

The application asks for:

```text
maximum value
```

Example:

```text
Enter maximum value (0-255): 255
```

Otsu thresholding is particularly useful when the image contains two dominant intensity regions.

---

## Important

Thresholding operations require a grayscale image.

Recommended workflow:

```text
Image I/O
→ Load Image
→ Transformations
→ Grayscale
→ Thresholding
```

The resulting thresholded image can then be saved using:

```text
Image I/O
→ Save Image
```

---

# 9. Morphological Operations

The Morphological Operations menu provides operations that process the shape and structure of objects in an image.

```text
1. Erosion
2. Dilation
3. Opening
4. Closing
5. Back
```

Morphological operations use a **structuring element**, also called a kernel.

The application allows the user to select the structuring-element shape:

```text
1. Rectangle
2. Ellipse
3. Cross
```

The kernel size must be a positive odd number.

Example:

```text
Enter kernel size: 3
```

---

## 9.1 Erosion

Erosion reduces the boundaries of foreground objects.

It can be used to:

* Remove small foreground regions
* Separate connected objects
* Reduce the size of foreground objects

The application asks for:

```text
structuring element shape
kernel size
iterations
```

Example:

```text
Choose structuring element shape:
1. Rectangle
2. Ellipse
3. Cross

Choose shape: 1

Enter kernel size: 3
Enter iterations: 1
```

Increasing the number of iterations applies erosion repeatedly.

---

## 9.2 Dilation

Dilation expands the boundaries of foreground objects.

It can be used to:

* Increase the size of foreground objects
* Fill small gaps
* Connect nearby regions

The application asks for:

```text
structuring element shape
kernel size
iterations
```

Example:

```text
Choose structuring element shape:
1. Rectangle
2. Ellipse
3. Cross

Choose shape: 1

Enter kernel size: 3
Enter iterations: 1
```

---

## 9.3 Opening

Opening consists of erosion followed by dilation.

It is useful for:

* Removing small foreground noise
* Separating objects
* Smoothing object boundaries

The application asks for:

```text
structuring element shape
kernel size
iterations
```

Example:

```text
Choose structuring element shape:
1. Rectangle
2. Ellipse
3. Cross

Choose shape: 2

Enter kernel size: 5
Enter iterations: 1
```

---

## 9.4 Closing

Closing consists of dilation followed by erosion.

It is useful for:

* Filling small gaps
* Closing small holes
* Connecting nearby foreground regions

The application asks for:

```text
structuring element shape
kernel size
iterations
```

Example:

```text
Choose structuring element shape:
1. Rectangle
2. Ellipse
3. Cross

Choose shape: 1

Enter kernel size: 3
Enter iterations: 1
```

---

## Morphological Processing Workflow

A typical workflow is:

```text
Load Image
     ↓
Grayscale
     ↓
Threshold
     ↓
Morphological Operation
     ↓
Save Result
```

For example:

```text
Image I/O
→ Load Image

Transformations
→ Grayscale

Thresholding
→ Binary Threshold

Morphological Operations
→ Opening

Image I/O
→ Save Image
```

---

# 10. Edge Detection

The Edge Detection menu currently provides Canny edge detection.

```text
1. Canny Edge Detection
2. Back
```

---

## 10.1 Canny Edge Detection

Canny edge detection identifies strong changes in image intensity and produces an edge map.

The application asks for:

```text
lower threshold
upper threshold
```

Example:

```text
Enter lower threshold (0-255): 100
Enter upper threshold (0-255): 200
```

The result is a binary edge image.

### Recommended Workflow

For many images, convert the image to grayscale before edge detection:

```text
Transformations
→ Grayscale
```

Then:

```text
Edge Detection
→ Canny Edge Detection
```

---

# 11. Typical Workflow

A basic workflow for the toolkit is:

```text
Start application
       ↓
Load Image
       ↓
Choose a processing operation
       ↓
Enter required parameters
       ↓
Continue processing if required
       ↓
Save Result
```

The current image remains available while the application is running, allowing multiple operations to be performed sequentially.

For example, an image can be:

```text
Load
→ Grayscale
→ Gaussian Blur
→ Threshold
→ Morphological Opening
→ Save
```

---

## Basic Blur Workflow

For example, to blur an image:

```text
1. Start the application

2. Image I/O
   → Load Image

3. Filtering
   → Gaussian Blur

4. Enter kernel size

5. Image I/O
   → Save Image
```

---

## Grayscale + Threshold Workflow

For thresholding:

```text
Load Image
     ↓
Transformations
     ↓
Grayscale
     ↓
Thresholding
     ↓
Binary Threshold
     ↓
Save Result
```

---

## Grayscale + Edge Detection Workflow

For Canny edge detection:

```text
Load Image
     ↓
Transformations
     ↓
Grayscale
     ↓
Edge Detection
     ↓
Canny Edge Detection
     ↓
Save Result
```

---

## Morphological Workflow

For morphological processing:

```text
Load Image
     ↓
Grayscale
     ↓
Threshold
     ↓
Morphological Operation
     ↓
Save Result
```

For example:

```text
Load Image
→ Grayscale
→ Binary Threshold
→ Morphological Opening
→ Save Result
```

---

# 12. Input Guidelines

Follow these guidelines when entering parameters.

## Kernel Sizes

Filtering and morphological operations generally require positive odd kernel sizes.

Valid:

```text
3
5
7
9
```

Invalid:

```text
0
2
4
-3
```

---

## Threshold Values

Threshold values must be between:

```text
0 and 255
```

---

## Maximum Values

Maximum threshold values must also be between:

```text
0 and 255
```

---

## Scale Factors

Scale factors must be positive.

Examples:

```text
1.5
0.5
2.0
```

---

## Coordinates

Coordinates should be entered as integer pixel positions where required.

Image coordinates are zero-based.

---

## Morphological Iterations

Morphological iterations must be positive integers.

Examples:

```text
1
2
3
```

---

# 13. Common Errors

## Image Cannot Be Loaded

If an image path is incorrect, the application will report that the image could not be loaded.

Check that:

* The file exists.
* The path is correct.
* The image format is supported.

Example:

```text
examples/input/test.jpg
```

---

## No Image Is Loaded

Processing operations require a currently loaded image.

If no image is loaded, the application will display a message asking you to load an image first.

Use:

```text
Image I/O
→ Load Image
```

before performing image-processing operations.

---

## Thresholding Requires Grayscale

Thresholding operations require a grayscale image.

If thresholding reports that a grayscale image is required, convert the image first:

```text
Transformations
→ Grayscale
```

---

## Invalid Kernel Size

If an operation requires an odd kernel size, use values such as:

```text
3
5
7
```

instead of:

```text
2
4
6
```

---

## Invalid Threshold

Threshold values must be within:

```text
0-255
```

---

## Invalid Morphological Iterations

Morphological iterations must be positive integers.

For example:

```text
1
2
3
```

are valid, while:

```text
0
-1
1.5
```

are invalid.

---

## Image Window Does Not Close

When displaying an image, focus the OpenCV image window and press:

```text
ESC
```

to close it.

---

# 14. Exiting the Application

To exit the application, return to the main menu and select:

```text
8. Exit
```

The application will display:

```text
Goodbye!
```

and terminate.

---

# 15. Current Feature Categories

The current CLI provides:

| Category | Features |
|---|---|
| Image I/O | Load, Save, Display |
| Image Information | Dimensions, Width, Height, Channels, Data Type, Pixel Value, Statistics, Grayscale Check, Color Check |
| Transformations | Resize, Crop, Rotate, Grayscale, Flips, Translation, Scaling, Shearing, Affine, Perspective, Padding |
| Filtering | Gaussian, Median, Average, Bilateral, Custom Convolution, Sharpening, Unsharp Mask, Noise Reduction, Salt-and-Pepper Removal |
| Thresholding | Binary, Binary Inverse, Truncation, To Zero, Adaptive, Otsu |
| Morphological Operations | Structuring Elements, Erosion, Dilation, Opening, Closing |
| Edge Detection | Canny Edge Detection |

---

# 16. Future Improvements

The CLI architecture is under active development.

Planned improvements may include:

* Additional morphological operations
* Additional edge detection algorithms
* Additional filtering techniques
* Additional thresholding techniques
* Chained image-processing workflows
* Improved parameter validation
* Improved error handling
* More advanced CLI workflows
* Better documentation and examples
* Additional image-processing capabilities

The documentation will evolve alongside the project.
