# Square and Circle Transformation Visualizations

This repository contains Python scripts that allow you to visualize geometric transformations applied to both squares and circles using NumPy and Matplotlib.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Square Transformation

### Usage

1. Clone or download the repository.
2. Install the required packages using `pip install numpy matplotlib`.
3. Run the script `square_transformation.py`.
4. Follow the prompts to enter the size of the square and choose a transformation (Scale, Rotate, or Translate).

### Functions

- `get_square_size()`: Prompts the user to enter the size of the square.
- `get_transformation_choice()`: Displays a menu for choosing a transformation.
- `apply_transformation(square, transformation_matrix)`: Applies the specified transformation matrix to the square vertices.
- `plot_square(vertices, transformed_vertices)`: Plots the original and transformed square.

### Example Usage

1. Enter the size of the square (e.g., 5).
2. Choose a transformation (e.g., Scale).
3. Enter the scale factor (e.g., 2).

The script will display both the original square and the transformed square based on your input.

## Circle Transformation

### Usage

1. Clone or download the repository.
2. Install the required packages using `pip install numpy matplotlib`.
3. Run the script `circle_transformation.py`.
4. Follow the prompts to enter the radius of the circle and the desired scale factor.

### Functions

- `get_circle_radius()`: Prompts the user to enter the radius of the circle.
- `scale_circle(radius, scale_factor)`: Calculates the scaled radius based on the input scale factor.
- `plot_circle(radius, x, y, x_transformed=None, y_transformed=None)`: Plots the original and transformed circle.

### Example Usage

1. Enter the radius of the circle (e.g., 5).
2. Input the scale factor (e.g., 2).

The script will display both the original circle and the scaled circle based on your input.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


