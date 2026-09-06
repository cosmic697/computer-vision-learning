from image_processor.thresholding import ( threshold_image, binary_inverse_threshold, truncation_threshold, to_zero_threshold, adaptive_threshold, otsu_threshold,)
from cli.helpers import get_image
from cli import state

def threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        threshold = int(input("Enter threshold value (0-255): ").strip())
        max_val = int(input("Enter maximum value (0-255): ").strip())
        result = threshold_image( image, threshold, max_val)
        state.current_image = result
        print("\nBinary threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply threshold: {error}")

def binary_inverse_threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        threshold = int(input("Enter threshold value (0-255): ").strip())
        max_val = int(input("Enter maximum value (0-255): ").strip())
        result = binary_inverse_threshold(image,threshold,max_val)
        state.current_image = result
        print("\nBinary inverse threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply binary inverse threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply binary inverse threshold: {error}")

def truncation_threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        threshold = int(input("Enter threshold value (0-255): ").strip())
        result = truncation_threshold(image,threshold)
        state.current_image = result
        print("\nTruncation threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply truncation threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply truncation threshold: {error}")

def to_zero_threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        threshold = int(input("Enter threshold value (0-255): ").strip())
        result = to_zero_threshold(image,threshold)
        state.current_image = result
        print("\nTo-zero threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply to-zero threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply to-zero threshold: {error}")

def adaptive_threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        max_val = int(input("Enter maximum value (0-255): ").strip())
        block_size = int(input("Enter block size (odd number > 1): ").strip())
        constant = int(input("Enter constant: ").strip())
        result = adaptive_threshold(image,max_val=max_val,block_size=block_size,constant=constant)
        state.current_image = result
        print("\nAdaptive threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply adaptive threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply adaptive threshold: {error}")

def otsu_threshold_command():
    image = get_image()
    if image is None:
        return
    try:
        max_val = int( input("Enter maximum value (0-255): ").strip())
        result = otsu_threshold( image, max_val)
        state.current_image = result
        print("\nOtsu threshold applied successfully.")
    except ValueError as error:
        print(f"\nFailed to apply Otsu threshold: {error}")
    except Exception as error:
        print(f"\nFailed to apply Otsu threshold: {error}")