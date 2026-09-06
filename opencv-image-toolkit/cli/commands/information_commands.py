from image_processor.information import (get_dimensions,get_width,get_height,get_channels,get_dtype,get_pixel,get_statistics,is_grayscale,is_color,)

from cli.helpers import get_image


def dimensions_command():

    """Display the dimensions of an image."""

    image = get_image()

    if image is None:

        return

    try:

        dimensions = get_dimensions(image)

        print(f"\nDimensions: {dimensions}")

    except Exception as error:

        print(f"\nFailed to get dimensions: {error}")


def width_command():

    """Display the width of an image."""

    image = get_image()

    if image is None:

        return

    try:

        width = get_width(image)

        print(f"\nWidth: {width}")

    except Exception as error:

        print(f"\nFailed to get width: {error}")


def height_command():

    """Display the height of an image."""

    image = get_image()

    if image is None:

        return

    try:

        height = get_height(image)

        print(f"\nHeight: {height}")

    except Exception as error:

        print(f"\nFailed to get height: {error}")


def channels_command():

    """Display the number of channels in an image."""

    image = get_image()

    if image is None:

        return

    try:

        channels = get_channels(image)

        print(f"\nChannels: {channels}")

    except Exception as error:

        print(f"\nFailed to get channels: {error}")


def dtype_command():

    """Display the data type of an image."""

    image = get_image()

    if image is None:

        return

    try:

        dtype = get_dtype(image)

        print(f"\nData type: {dtype}")

    except Exception as error:

        print(f"\nFailed to get data type: {error}")


def pixel_command():

    """Display the pixel value at a given coordinate."""

    image = get_image()

    if image is None:

        return

    try:

        x = int(input("Enter x coordinate: "))

        y = int(input("Enter y coordinate: "))

        pixel = get_pixel(image, x, y)

        print(f"\nPixel value at ({x}, {y}): {pixel}")

    except ValueError:

        print("\nCoordinates must be integers.")

    except Exception as error:

        print(f"\nFailed to get pixel value: {error}")


def statistics_command():

    """Display image statistics."""

    image = get_image()

    if image is None:

        return

    try:

        statistics = get_statistics(image)

        print("\nImage Statistics:")

        for name, value in statistics.items():

            print(f"{name}: {value}")

    except Exception as error:

        print(f"\nFailed to get statistics: {error}")


def grayscale_check_command():

    """Check whether an image is grayscale."""

    image = get_image()

    if image is None:

        return

    try:

        result = is_grayscale(image)

        print(f"\nGrayscale image: {result}")

    except Exception as error:

        print(f"\nFailed to check image: {error}")


def color_check_command():

    """Check whether an image is a color image."""

    image = get_image()

    if image is None:

        return

    try:

        result = is_color(image)

        print(f"\nColor image: {result}")

    except Exception as error:

        print(f"\nFailed to check image: {error}")