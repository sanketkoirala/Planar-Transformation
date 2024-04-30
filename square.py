import numpy as np
import matplotlib.pyplot as plt

def get_square_size():
    try:
        size = float(input("Enter the size of the square: "))
        return size
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        return get_square_size()

def get_transformation_choice():
    print("Choose a transformation:")
    print("1. Scale")
    print("2. Rotate")
    print("3. Translate")
    choice = input("Enter the corresponding number (1/2/3): ")
    return choice

def apply_transformation(square, transformation_matrix):
    square_homogeneous = np.hstack((square, np.ones((square.shape[0], 1))))
    transformed_square_homogeneous = np.dot(square_homogeneous, transformation_matrix.T)
    transformed_square = transformed_square_homogeneous[:, :2]
    return transformed_square

def plot_square(vertices, transformed_vertices):
    plt.figure(figsize=(8, 6))
    plt.plot(vertices[:, 0], vertices[:, 1], label="Original Square", marker='o')
    plt.plot(transformed_vertices[:, 0], transformed_vertices[:, 1], label="Transformed Square", marker='x')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Original and Transformed Square")
    plt.grid()
    plt.legend()
    plt.show()

def main():
    square_size = get_square_size()

    square_vertices = np.array([
        [0, 0],
        [square_size, 0],
        [square_size, square_size],
        [0, square_size]
    ])

    choice = get_transformation_choice()

    if choice == '1':
        scale_factor = float(input("Enter the scale factor: "))
        transformation_matrix = np.diag([scale_factor, scale_factor])
    elif choice == '2':
        angle_degrees = float(input("Enter the rotation angle (in degrees): "))
        rotation_matrix = np.array([[np.cos(np.radians(angle_degrees)), -np.sin(np.radians(angle_degrees))],
                                    [np.sin(np.radians(angle_degrees)), np.cos(np.radians(angle_degrees))]])
        transformation_matrix = rotation_matrix
    elif choice == '3':
        x_translation = float(input("Enter x-translation: "))
        y_translation = float(input("Enter y-translation: "))
        translation_matrix = np.array([[1, 0, x_translation],
                                       [0, 1, y_translation]])
        transformation_matrix = translation_matrix
    else:
        print("Invalid choice. Exiting.")
        return

    transformed_square = apply_transformation(square_vertices, transformation_matrix)
    plot_square(square_vertices, transformed_square)

if __name__ == "__main__":
    main()
