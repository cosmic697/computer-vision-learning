from cli.helpers import print_header, pause

from cli.commands.io_commands import (
    load_image_command,
    save_image_command,
    display_image_command,
)
from cli.commands.information_commands import (
    dimensions_command,
    width_command,
    height_command,
    channels_command,
    dtype_command,
    pixel_command,
    statistics_command,
    grayscale_check_command,
    color_check_command,
)
from cli.commands.transformation_commands import (
    resize_command,
    crop_command,
    rotate_command,
    grayscale_command,
    horizontal_flip_command,
    vertical_flip_command,
    both_flip_command,
    translation_command,
    scaling_command,
    shearing_command,
    affine_command,
    perspective_command,
    padding_command,
)
from cli.commands.filtering_commands import (
    gaussian_blur_command,
    median_blur_command,
    average_blur_command,
    bilateral_blur_command,
    custom_convolution_command,
    sharpening_command,
    unsharp_mask_command,
    noise_reduction_command,
    salt_pepper_removal_command,
)
from cli.commands.thresholding_commands import (
    threshold_command,
    binary_inverse_threshold_command,
    truncation_threshold_command,
    to_zero_threshold_command,
    adaptive_threshold_command,
    otsu_threshold_command,
)
from cli.commands.edges_commands import (
    edge_detection_command,
)

def io_menu() -> None:
    """Display and handle the Image I/O menu."""
    while True:
        print_header("Image I/O")
        print("1. Load Image")
        print("2. Save Image")
        print("3. Display Image")
        print("4. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            load_image_command()
            pause()
        elif choice == "2":
            save_image_command()
            pause()
        elif choice == "3":
            display_image_command()
            pause()
        elif choice == "4":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()


def information_menu() -> None:
    """Display and handle the Image Information menu."""
    while True:
        print_header("Image Information")
        print("1. Dimensions")
        print("2. Width")
        print("3. Height")
        print("4. Channels")
        print("5. Data Type")
        print("6. Pixel Value")
        print("7. Statistics")
        print("8. Check Grayscale")
        print("9. Check Color")
        print("10. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            dimensions_command()
            pause()
        elif choice == "2":
            width_command()
            pause()
        elif choice == "3":
            height_command()
            pause()
        elif choice == "4":
            channels_command()
            pause()
        elif choice == "5":
            dtype_command()
            pause()
        elif choice == "6":
            pixel_command()
            pause()
        elif choice == "7":
            statistics_command()
            pause()
        elif choice == "8":
            grayscale_check_command()
            pause()
        elif choice == "9":
            color_check_command()
            pause()
        elif choice == "10":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()

def transformations_menu() -> None:
    """Display and handle the Image Transformations menu."""
    while True:
        print_header("Transformations")
        print("1. Resize")
        print("2. Crop")
        print("3. Rotate")
        print("4. Grayscale")
        print("5. Horizontal Flip")
        print("6. Vertical Flip")
        print("7. Flip Both")
        print("8. Translate")
        print("9. Scale")
        print("10. Shear")
        print("11. Affine Transform")
        print("12. Perspective Transform")
        print("13. Add Padding")
        print("14. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            resize_command()
            pause()
        elif choice == "2":
            crop_command()
            pause()
        elif choice == "3":
            rotate_command()
            pause()
        elif choice == "4":
            grayscale_command()
            pause()
        elif choice == "5":
            horizontal_flip_command()
            pause()
        elif choice == "6":
            vertical_flip_command()
            pause()
        elif choice == "7":
            both_flip_command()
            pause()
        elif choice == "8":
            translation_command()
            pause()
        elif choice == "9":
            scaling_command()
            pause()
        elif choice == "10":
            shearing_command()
            pause()
        elif choice == "11":
            affine_command()
            pause()
        elif choice == "12":
            perspective_command()
            pause()
        elif choice == "13":
            padding_command()
            pause()
        elif choice == "14":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()

def filtering_menu() -> None:
    """Display and handle the Image Filtering menu."""

    while True:
        print_header("Filtering")
        print("1. Gaussian Blur")
        print("2. Median Blur")
        print("3. Average Blur")
        print("4. Bilateral Filter")
        print("5. Custom Convolution")
        print("6. Sharpening")
        print("7. Unsharp Mask")
        print("8. Noise Reduction")
        print("9. Remove Salt-and-Pepper Noise")
        print("10. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            gaussian_blur_command()
            pause()
        elif choice == "2":
            median_blur_command()
            pause()
        elif choice == "3":
            average_blur_command()
            pause()
        elif choice == "4":
            bilateral_blur_command()
            pause()
        elif choice == "5":
            custom_convolution_command()
            pause()
        elif choice == "6":
            sharpening_command()
            pause()
        elif choice == "7":
            unsharp_mask_command()
            pause()
        elif choice == "8":
            noise_reduction_command()
            pause()
        elif choice == "9":
            salt_pepper_removal_command()
            pause()
        elif choice == "10":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()

def thresholding_menu() -> None:
    while True:
        print_header("Thresholding")
        print("1. Binary Threshold")
        print("2. Binary Inverse Threshold")
        print("3. Truncation Threshold")
        print("4. To-Zero Threshold")
        print("5. Adaptive Threshold")
        print("6. Otsu Threshold")
        print("7. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            threshold_command()
            pause()
        elif choice == "2":
            binary_inverse_threshold_command()
            pause()
        elif choice == "3":
            truncation_threshold_command()
            pause()
        elif choice == "4":
            to_zero_threshold_command()
            pause()
        elif choice == "5":
            adaptive_threshold_command()
            pause()
        elif choice == "6":
            otsu_threshold_command()
            pause()
        elif choice == "7":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()

def edge_menu() -> None:
    """Display and handle the Edge Detection menu."""
    while True:
        print_header("Edge Detection")
        print("1. Canny Edge Detection")
        print("2. Back")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            edge_detection_command()
            pause()
        elif choice == "2":
            return
        else:
            print("\nInvalid choice. Please try again.")
            pause()

def main_menu() -> None:
    """Display and handle the main application menu."""
    while True:
        print_header("OpenCV Image Toolkit")
        print("1. Image I/O")
        print("2. Image Information")
        print("3. Transformations")
        print("4. Filtering")
        print("5. Thresholding")
        print("6. Edge Detection")
        print("7. Exit")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            io_menu()
        elif choice == "2":
            information_menu()
        elif choice == "3":
            transformations_menu()
        elif choice == "4":
            filtering_menu()
        elif choice == "5":
            thresholding_menu()
        elif choice == "6":
            edge_menu()
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            pause()

