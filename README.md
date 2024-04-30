# Square Transformation Visualization

This Python script allows you to visualize transformations (scaling, rotation, and translation) applied to a square using NumPy and Matplotlib.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

1. Clone or download the repository.
2. Install the required packages using `pip install numpy matplotlib`.
3. Run the script using `python square_transformation.py`.
4. Follow the prompts to enter the size of the square and choose a transformation.

## Functions

### `get_square_size()`

Prompts the user to enter the size of the square.

### `get_transformation_choice()`

Displays a menu for choosing a transformation (Scale, Rotate, Translate) and returns the user's choice.

### `apply_transformation(square, transformation_matrix)`

Applies the specified transformation matrix to the square vertices using NumPy's dot product.

### `plot_square(vertices, transformed_vertices)`

Plots the original and transformed square using Matplotlib.

### `main()`

Main function that orchestrates the entire process, including input handling, transformation selection, and visualization.

## Transformations

1. **Scale**: Enlarges or shrinks the square based on a scale factor.
2. **Rotate**: Rotates the square by a specified angle in degrees.
3. **Translate**: Moves the square by a specified amount in the x and y directions.

## Example Usage

Here's an example of how you can use this script:

1. Enter the size of the square (e.g., 5).
2. Choose a transformation (e.g., Scale).
3. Enter the scale factor (e.g., 2).

The script will then display the original square and the transformed square based on your input.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
