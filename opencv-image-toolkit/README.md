# OpenCV Image Processing Toolkit

A beginner-friendly Python project for learning the fundamentals of image processing and computer vision using OpenCV.

The goal of this project is not just to use OpenCV functions, but to understand how common image-processing operations work and how they can be combined to build simple computer vision pipelines.

---

## Features

The toolkit will progressively support:

* Read and save images
* Display images
* Convert images to grayscale
* Resize images
* Crop images
* Rotate images
* Apply image blurring
* Apply thresholding
* Detect edges
* Compare original and processed images

More operations may be added as the project develops.

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
│   └── output/
│
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
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

The toolkit will eventually provide a simple way to apply different image-processing operations from the command line.

Example:

```bash
python main.py --image examples/input/image.jpg --operation grayscale
```

Additional operations will be added as development continues.

---

## Learning Goals

This project is being developed as a practical introduction to computer vision.

The main learning goals are:

1. Understand how digital images are represented as numerical arrays.
2. Learn the basic OpenCV image-processing API.
3. Understand common image-processing operations.
4. Practice working with images using Python and NumPy.
5. Learn how individual computer vision operations can be combined into processing pipelines.
6. Develop the habit of implementing and testing concepts rather than simply copying library functions.

---

## Development Approach

This project is primarily a learning project.

For each feature, the goal is to:

```text
Understand the concept
        ↓
Learn the algorithm
        ↓
Implement it using OpenCV
        ↓
Experiment with different inputs
        ↓
Test the result
        ↓
Document what was learned
```

As my understanding of computer vision improves, some operations may also be implemented manually to better understand the underlying algorithms.

---

## Planned Operations

### Basic Operations

* [ ] Read image
* [ ] Display image
* [ ] Save image
* [ ] Get image dimensions
* [ ] Convert to grayscale
* [ ] Resize
* [ ] Crop
* [ ] Rotate

### Image Processing

* [ ] Gaussian blur
* [ ] Median blur
* [ ] Thresholding
* [ ] Adaptive thresholding
* [ ] Image sharpening
* [ ] Morphological operations

### Edge & Feature Processing

* [ ] Sobel edge detection
* [ ] Canny edge detection
* [ ] Contour detection
* [ ] Basic feature detection

### Future Improvements

* [ ] Command-line interface
* [ ] Better error handling
* [ ] Input validation
* [ ] Automated tests
* [ ] Example images and results
* [ ] Performance improvements

---

## What I Learned

This section will be updated throughout development.

Topics currently being studied:

* Digital image representation
* Image dimensions and channels
* NumPy arrays
* OpenCV image I/O
* Image transformations
* Image filtering
* Thresholding
* Edge detection

---

## Status

**In Development**

This project is being built incrementally as part of my journey into computer vision.

---

## License

This project is licensed under the MIT License.
