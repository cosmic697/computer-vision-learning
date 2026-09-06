import cv2
from image_processor.morphology import ( create_structuring_element, erode_image, dilate_image,open_image,close_image,morphological_gradient,top_hat,black_hat,hit_or_miss,)
from cli.helpers import get_image
from cli import state

def get_morphology_kernel():
    print("\nSelect structuring element:")
    print("1. Rectangle")
    print("2. Ellipse")
    print("3. Cross")
    choice = input("Enter choice: ").strip()
    shapes = {"1": cv2.MORPH_RECT,"2": cv2.MORPH_ELLIPSE,"3": cv2.MORPH_CROSS,}
    if choice not in shapes:
        print("\nInvalid choice.")
        return None
    try:
        kernel_size = int(input("Enter kernel size (positive odd number): ") )
        kernel = create_structuring_element(shapes[choice],kernel_size)
        return kernel
    except (ValueError, TypeError) as error:
        print(f"\nInvalid kernel: {error}")
        return None
    
def get_iterations():
    try:
        iterations = int(input("Enter number of iterations: ") )
        if iterations <= 0:
            print("\nIterations must be positive.")
            return None
        return iterations
    except ValueError:
        print("\nIterations must be an integer.")
        return None

def erode_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = erode_image(image,kernel,iterations)
        state.current_image = result
        print("\nErosion applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply erosion: {error}")

def dilate_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = dilate_image(image,kernel,iterations)
        state.current_image = result
        print("\nDilation applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply dilation: {error}")

def opening_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = open_image(image,kernel,iterations)
        state.current_image = result
        print("\nOpening applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply opening: {error}")

def closing_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = close_image( image, kernel,iterations)
        state.current_image = result
        print("\nClosing applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply closing: {error}")

def morphological_gradient_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = morphological_gradient(image,kernel,iterations)
        state.current_image = result
        print("\nMorphological gradient applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply morphological gradient: {error}")

def top_hat_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = top_hat(image,kernel,iterations)
        state.current_image = result
        print("\nTop Hat applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply Top Hat: {error}")


def black_hat_command():
    image = get_image()
    if image is None:
        return
    kernel = get_morphology_kernel()
    if kernel is None:
        return
    iterations = get_iterations()
    if iterations is None:
        return
    try:
        result = black_hat( image, kernel, iterations )
        state.current_image = result
        print("\nBlack Hat applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply Black Hat: {error}")

def get_hitmiss_kernel():
    print("\nHit-or-Miss kernel")
    print("Use:")
    print("  1  = foreground")
    print(" -1  = background")
    print("  0  = don't care")
    print("\nEnter 9 values for a 3x3 kernel.")
    print("Example: 1 1 0 1 -1 -1 0 -1 -1")
    values = input("Kernel: ").split()
    if len(values) != 9:
        print("\nPlease enter exactly 9 values.")
        return None
    try:
        values = [int(value) for value in values]
    except ValueError:
        print("\nKernel values must be integers.")
        return None
    if not all(value in (-1, 0, 1) for value in values):
        print("\nKernel values must be -1, 0, or 1.")
        return None
    kernel = __import__("numpy").array(values,dtype=__import__("numpy").int8).reshape(3, 3)
    return kernel

def hit_or_miss_command():
    image = get_image()
    if image is None:
        return
    kernel = get_hitmiss_kernel()
    if kernel is None:
        return
    try:
        result = hit_or_miss(image,kernel)
        state.current_image = result
        print("\nHit-or-Miss applied successfully.")
    except Exception as error:
        print(f"\nFailed to apply Hit-or-Miss: {error}")