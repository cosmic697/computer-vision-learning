import cv2
from image_processor.morphology import (create_structuring_element, erode_image, dilate_image, open_image, close_image,)
from cli.helpers import get_image
from cli import state

def get_morphology_kernel():
    shape_choice = input(
        "\nChoose structuring element shape:\n"
        "1. Rectangle\n"
        "2. Ellipse\n"
        "3. Cross\n"
        "Enter choice: "
    ).strip()
    if shape_choice == "1":
        shape = cv2.MORPH_RECT
    elif shape_choice == "2":
        shape = cv2.MORPH_ELLIPSE
    elif shape_choice == "3":
        shape = cv2.MORPH_CROSS
    else:
        raise ValueError("Invalid structuring element shape.")
    kernel_size = int( input("Enter kernel size (positive odd number): ").strip())
    return create_structuring_element(shape, kernel_size)

def erode_command():
    image = get_image()
    if image is None:
        return
    try:
        kernel = get_morphology_kernel()
        iterations = int( input("Enter number of iterations: ").strip() )
        result = erode_image(image,kernel,iterations )
        state.current_image = result
        print("\nErosion applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply erosion: {error}")
    except Exception as error:
        print(f"\nFailed to apply erosion: {error}")

def dilate_command():
    image = get_image()
    if image is None:
        return
    try:
        kernel = get_morphology_kernel()
        iterations = int(input("Enter number of iterations: ").strip())
        result = dilate_image(image,kernel,iterations)
        state.current_image = result
        print("\nDilation applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply dilation: {error}")
    except Exception as error:
        print(f"\nFailed to apply dilation: {error}")

def opening_command():
    image = get_image()
    if image is None:
        return
    try:
        kernel = get_morphology_kernel()
        iterations = int(input("Enter number of iterations: ").strip())
        result = open_image(image,kernel,iterations)
        state.current_image = result
        print("\nOpening applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply opening: {error}")
    except Exception as error:
        print(f"\nFailed to apply opening: {error}")

def closing_command():
    image = get_image()
    if image is None:
        return
    try:
        kernel = get_morphology_kernel()
        iterations = int(input("Enter number of iterations: ").strip())
        result = close_image(image,kernel,iterations)
        state.current_image = result
        print("\nClosing applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply closing: {error}")
    except Exception as error:
        print(f"\nFailed to apply closing: {error}")