from image_processor.io import (load_image,save_image,display_image,)

from cli.helpers import get_image, get_output_path

def load_image_command():
    """Load an image through the CLI."""
    path = input("\nEnter image path: ").strip()
    try:
        image = load_image(path)
        print("\nImage loaded successfully.")
        print(f"Shape: {image.shape}")
        print(f"Data type: {image.dtype}")
        return image
    except Exception as error:
        print(f"\nFailed to load image: {error}")
        return None

def save_image_command():
    """Save an image through the CLI."""
    image = get_image()

    if image is None:
        return
    output_path = get_output_path()
    try:
        save_image(image, output_path)
        print("\nImage saved successfully.")
    except Exception as error:
        print(f"\nFailed to save image: {error}")

def display_image_command():
    """Display an image through the CLI."""
    image = get_image()
    if image is None:
        return
    try:
        display_image(image)
        print("\nImage displayed successfully.")
    except Exception as error:
        print(f"\nFailed to display image: {error}")