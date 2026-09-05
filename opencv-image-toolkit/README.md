# OpenCV Image Toolkit

A beginner-friendly Python project for learning the fundamentals of image processing and computer vision using OpenCV.

The goal of this project is not just to use OpenCV functions, but to understand how common image-processing operations work and how they can be combined to build simple computer vision pipelines.

---

## Features

The toolkit currently supports:

* Read images
* Save images
* Convert images to grayscale
* Resize images
* Crop images
* Rotate images
* Apply Gaussian blur
* Apply binary thresholding
* Detect edges using Canny

More operations will be added as the project develops.

---

## Technologies

* Python
* OpenCV
* NumPy

---

## Project Structure

```text
opencv-image-toolkit/
│
├── README.md
├── requirements.txt
├── main.py
├── image_processor.py
│
├── examples/
│   ├── input/
│   │   └── test.jpg
│   └── output/
│
├── tests/
│   └── test_image_processor.py
│
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/cosmic697/computer-vision-learning.git
cd opencv-image-toolkit
```

Create and activate a virtual environment:

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

The project is currently under development.

The current demo can be run with:

```bash
python3 main.py
```

The demo reads an image from:

```text
examples/input/
```

and saves the processed images to:

```text
examples/output/
```

The current demo applies several image-processing operations including:

* Grayscale conversion
* Resizing
* Cropping
* Rotation
* Gaussian blur
* Thresholding
* Canny edge detection

A command-line interface will be added in a future version.

---

## Testing

The project uses Python's built-in `unittest` framework.

Run the test suite with:

```bash
python3 -m unittest tests/test_image_processor.py
```

The current test suite contains **23 tests** covering:

* Normal image-processing operations
* Invalid inputs
* Error handling
* Image dimensions
* Output validation
* Threshold values
* Kernel size validation
* Edge detection thresholds

---

## Learning Goals

This project is being developed as a practical introduction to computer vision.

The main learning goals are:

1. Understand how digital images are represented as numerical arrays.
2. Learn how OpenCV works with images.
3. Understand common image-processing operations.
4. Practice working with images using Python and NumPy.
5. Learn how individual computer vision operations can be combined into processing pipelines.
6. Practice writing tests for image-processing functions.
7. Develop the habit of understanding and experimenting with concepts instead of simply copying library functions.

---

## Planned Operations

### Basic Operations

* [x] Read image
* [ ] Display image
* [x] Save image
* [ ] Get image dimensions
* [x] Convert to grayscale
* [x] Resize
* [x] Crop
* [x] Rotate

### Image Processing

* [x] Gaussian blur
* [ ] Median blur
* [x] Thresholding
* [ ] Adaptive thresholding
* [ ] Image sharpening
* [ ] Morphological operations

### Edge & Feature Processing

* [ ] Sobel edge detection
* [x] Canny edge detection
* [ ] Contour detection
* [ ] Basic feature detection

### Future Improvements

* [ ] Command-line interface
* [ ] Better error handling
* [ ] More input validation
* [ ] More automated tests
* [ ] Example images and results
* [ ] Performance improvements

---

## What I Learned

This section will be updated throughout development.

Topics currently studied:

* Digital image representation
* Image dimensions and channels
* NumPy arrays
* OpenCV image I/O
* Image transformations
* Image filtering
* Gaussian blur
* Thresholding
* Canny edge detection
* Basic input validation
* Unit testing with `unittest`

---

## Status

**In Development**

This project is being built incrementally as part of my computer vision learning journey.

The current focus is on understanding basic image processing, writing reusable functions, and testing them properly before moving on to more advanced computer vision techniques.

