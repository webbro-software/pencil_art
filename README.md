# Pencil Art

**pencil_art** is a Python package that converts images into pencil sketches using OpenCV. It provides a simple way to create a pencil sketch effect from a given image by applying image processing techniques such as grayscale conversion, Gaussian blurring, and inversion.

## Installation

To install the `pencil_art` package, use the following `pip` command:

```bash
pip install pencil_art
```

## Usage

### Basic Example

```python
from pencil_art import pencil_art

# Specify the input image path and output path for the pencil sketch
input_image = 'path_to_your_image.jpg'
output_image = 'output_sketch.jpg'

# Convert the image to a pencil sketch
pencil_art(input_image, output_image)
```

### Function: `pencil_art`

```python
pencil_art(input_image_path, output_image_path)
```

#### Parameters:

- `input_image_path` (str): The path to the input image file that you want to convert to a pencil sketch.
- `output_image_path` (str): The path where the resulting pencil sketch will be saved.

#### Returns:

- This function does not return any value. The pencil sketch image will be saved to the specified output path.

#### Example:

```python
input_image = 'sample_image.jpg'
output_image = 'sketched_output.jpg'
pencil_art(input_image, output_image)
```

This will read the image located at `input_image`, convert it to a pencil sketch, and save it as `output_image`.

## How It Works

The `pencil_art` function performs the following steps to generate the pencil sketch effect:

1. **Grayscale Conversion**: The input image is converted to grayscale to reduce color complexity.
2. **Gaussian Blurring**: A Gaussian blur is applied to the grayscale image to smooth out details.
3. **Inversion**: The blurred image is inverted.
4. **Sketch Creation**: The pencil sketch effect is achieved by dividing the original grayscale image by the inverted blurred image.

## Dependencies

The `pencil_art` package requires the `opencv-python` library. It is automatically installed when you install `pencil_art`.

- `opencv-python` version 4.5.0 or later

## Contributing

If you'd like to contribute to the development of the `pencil_art` package, feel free to fork the repository, make changes, and submit a pull request. We welcome improvements, bug fixes, and new features.

## License

This package is licensed under the [MIT License](./LICENCE).
