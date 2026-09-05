# How to Use OpenCV Image Toolkit

This guide explains how to use the OpenCV Image Toolkit through its command-line interface (CLI).

---

## Table of Contents

1.  [Requirements](#1-requirements)
2.  [Starting the Application](#2-starting-the-application)
3.  [Main Menu](#3-main-menu)
4.  [Image I/O](#4-image-io)
5.  [Image Information](#5-image-information)
6.  [Transformations](#6-transformations)
7.  [Filtering](#7-filtering)
8.  [Thresholding](#8-thresholding)
9.  [Edge Detection](#9-edge-detection)
10. [Typical Workflow](#10-typical-workflow)
11. [Input Guidelines](#11-input-guidelines)
12. [Common Errors](#12-common-errors)
13. [Exiting the Application](#13-exiting-the-application)

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

The main menu provides access to all currently implemented features:

```text
==================================================
              OpenCV Image Toolkit
==================================================

1. Image I/O
2. Image Information
3. Transformations
4. Filtering
5. Thresholding
6. Edge Detection
7. Exit
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
Enter image path: examples/input/image.jpg
```

The application will load the image and display basic information such as its shape and data type.

### Example

```text
Image loaded successfully.
Shape: (720, 1280, 3)
Data type: uint8
```

---

## 4.2 Save Image

Select:

```text
2. Save Image
```

Enter the path of the image you want to save.

Example:

```text
Enter image path: examples/input/image.jpg
Enter output path: examples/output/result.jpg
```

The processed image will be saved at the specified location.

---

## 4.3 Display Image

Select:

```text
3. Display Image
```

Enter the image path.

The image will open in an OpenCV window.

Press:

```text
ESC
```

to close the image window.

---

# 5. Image Information

The Image Information menu provides information about an image.

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

Checks whether the image is represented as a grayscale image.

Example:

```text
Grayscale image: True
```

---

## 5.9 Check Color

Checks whether the image is represented as a color image.

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

The Thresholding menu currently provides binary thresholding.

```text
1. Binary Threshold
2. Back
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

### Important

Thresholding requires a **grayscale image**.

If the input image is a color image, convert it to grayscale first:

```text
Transformations
→ Grayscale
```

---

# 9. Edge Detection

The Edge Detection menu currently provides Canny edge detection.

```text
1. Canny Edge Detection
2. Back
```

---

## 9.1 Canny Edge Detection

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

# 10. Typical Workflow

A basic workflow looks like this:

```text
Start application
       ↓
Image I/O
       ↓
Load Image
       ↓
Choose a processing operation
       ↓
Enter required parameters
       ↓
Save Result
```

For example, to blur an image:

```text
1. Start the application

2. Image I/O
   → Load Image

3. Filtering
   → Gaussian Blur

4. Enter kernel size

5. Save the resulting image
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

# 11. Input Guidelines

Follow these guidelines when entering parameters.

### Kernel Sizes

Filtering operations generally require positive odd kernel sizes.

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

### Threshold Values

Threshold values must be between:

```text
0 and 255
```

### Maximum Values

Maximum threshold values must also be between:

```text
0 and 255
```

### Scale Factors

Scale factors must be positive.

Example:

```text
1.5
0.5
2.0
```

### Coordinates

Coordinates should be entered as integer pixel positions where required.

---

# 12. Common Errors

## Image Cannot Be Loaded

If an image path is incorrect, the application will report that the image could not be loaded.

Check that:

* The file exists.
* The path is correct.
* The image format is supported.

Example:

```text
examples/input/image.jpg
```

---

## Thresholding Requires Grayscale

If thresholding reports:

```text
Thresholding requires a grayscale image.
```

convert the image to grayscale first.

---

## Invalid Kernel Size

If a filtering operation requires an odd kernel size, use values such as:

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

## Image Window Does Not Close

When displaying an image, focus the OpenCV image window and press:

```text
ESC
```

to close it.

---

# 13. Exiting the Application

To exit the application, return to the main menu and select:

```text
7. Exit
```

The application will display:

```text
Goodbye!
```

and terminate.

---

## Current Feature Categories

The current CLI provides:

| Category          | Features                                                                                                                     |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Image I/O         | Load, Save, Display                                                                                                          |
| Image Information | Dimensions, Width, Height, Channels, Data Type, Pixel Value, Statistics, Grayscale Check, Color Check                        |
| Transformations   | Resize, Crop, Rotate, Grayscale, Flips, Translation, Scaling, Shearing, Affine, Perspective, Padding                         |
| Filtering         | Gaussian, Median, Average, Bilateral, Custom Convolution, Sharpening, Unsharp Mask, Noise Reduction, Salt-and-Pepper Removal |
| Thresholding      | Binary Threshold                                                                                                             |
| Edge Detection    | Canny Edge Detection                                                                                                         |

---

## Future Improvements

The CLI architecture is under active development. Future versions may introduce:

* Persistent image state
* Chained image operations
* Improved command organization
* More thresholding techniques
* More edge detection algorithms
* Additional filtering techniques
* Additional image-processing operations
* Improved error handling
* More advanced CLI workflows

The documentation will evolve alongside the project.
