from image_processor.io import (load_image,display_image,save_image,)

from cli.helpers import get_image, get_output_path

from cli import state


def load_image_command():

    """Load an image and store it as the current image."""

    path = input("\nEnter image path: ").strip()

    try:

        image = load_image(path)

        state.current_image = image

        print("\nImage loaded successfully.")

        print(f"Shape: {image.shape}")

        print(f"Data type: {image.dtype}")

        return image

    except Exception as error:

        print(f"\nFailed to load image: {error}")

        return None


def save_image_command():

    """Save the currently loaded image."""

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

    """Display the currently loaded image."""

    image = get_image()

    if image is None:

        return

    try:

        display_image(image)

    except Exception as error:

        print(f"\nFailed to display image: {error}")