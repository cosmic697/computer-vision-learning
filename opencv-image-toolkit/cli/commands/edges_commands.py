from image_processor.edges import detect_edges
from cli import state
from cli.helpers import get_image, save_result

def edge_detection_command():
    """Detect edges using the Canny edge detector."""
    image = get_image()
    if image is None:
        return
    try:
        lower_threshold = int(
            input("Enter lower threshold (0-255): "))
        upper_threshold = int(
            input("Enter upper threshold (0-255): "))
        result = detect_edges(
            image,
            lower_threshold,
            upper_threshold,)
        state.current_image = result
        print("\nEdge detection applied successfully.")
    except ValueError:
        print("\nThreshold values must be integers.")
    except Exception as error:
        print(f"\nFailed to detect edges: {error}")