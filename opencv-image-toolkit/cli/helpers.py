import shutil

from image_processor.io import load_image, save_image

def print_centered(text: str) -> None:
    """Print text centered in the terminal."""
    width = shutil.get_terminal_size().columns
    print(text.center(width))

def print_header(title: str) -> None:
    """Print a formatted section header."""
    print()
    print_centered("=" * 50)
    print_centered(title)
    print_centered("=" * 50)
    print()

def get_image():
    """Ask the user for an image path and load the image."""
    path = input("Enter image path: ").strip()
    try:
        image = load_image(path)
        print("\nImage loaded successfully.")
        return image
    except Exception as error:
        print(f"\nFailed to load image: {error}")
        return None

def get_output_path() -> str:
    """Ask the user for an output image path."""
    return input("Enter output path: ").strip()

def save_result(image) -> None:
    """Ask for an output path and save the image."""
    output_path = get_output_path()
    try:
        save_image(image, output_path)
        print(f"\nImage saved successfully: {output_path}")
    except Exception as error:
        print(f"\nFailed to save image: {error}")

def pause() -> None:
    """Pause the CLI until the user presses Enter."""
    input("\nPress Enter to continue...")