from image_processor.thresholding import threshold_image

from cli.helpers import get_image, save_result
from cli import state

def threshold_command():
    """Apply binary thresholding to a grayscale image."""
    image = get_image()
    if image is None:
        return
    try:
        threshold = int(input("Enter threshold (0-255): "))
        max_val = int(input("Enter maximum value (0-255): "))
        result = threshold_image(
            image,
            threshold,
            max_val,
        )
        state.current_image = result
        print("\nThresholding applied successfully.")
    except ValueError:
        print("\nThreshold and maximum value must be integers.")
    except Exception as error:
        print(f"\nFailed to apply thresholding: {error}")