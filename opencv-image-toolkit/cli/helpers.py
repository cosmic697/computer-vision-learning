import shutil

from image_processor.io import save_image

from cli import state

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
    """Return the image currently stored in application state."""
    if state.current_image is None:
        print("\nNo image is currently loaded.")
        print("Please load an image first.")
        return None
    return state.current_image

def get_output_path() -> str:
    """Ask the user for an output image path."""
    return input("Enter output path: ").strip()

def save_result(image) -> None:
    """Save an image to a user-specified output path."""
    if image is None:
        print("\nNo image available to save.")
        return
    output_path = get_output_path()
    try:
        save_image(image, output_path)
        print(f"\nImage saved successfully: {output_path}")
    except Exception as error:
        print(f"\nFailed to save image: {error}")

def pause() -> None:
    """Pause the CLI until the user presses Enter."""
    input("\nPress Enter to continue...")