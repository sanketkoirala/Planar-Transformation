import numpy as np
import matplotlib.pyplot as plt

def get_circle_radius():
    try:
        radius = float(input("Enter the radius of the circle: "))
        return radius
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        return get_circle_radius()


def scale_circle(radius, scale_factor):
    scaled_radius = radius * scale_factor
    return scaled_radius


def plot_circle(radius, x, y, x_transformed=None, y_transformed=None):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Original Circle")
    if x_transformed is not None and y_transformed is not None:
        plt.plot(x_transformed, y_transformed, label="Transformed Circle")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Original and Transformed Circle")
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()

def main():
    circle_radius = get_circle_radius()
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.cos(theta) * circle_radius
    y = np.sin(theta) * circle_radius


    scale_factor = float(input("Enter the scale factor: "))
    scaled_radius = scale_circle(circle_radius, scale_factor)
    x_scaled = np.cos(theta) * scaled_radius
    y_scaled = np.sin(theta) * scaled_radius
    plot_circle(circle_radius, x, y, x_scaled, y_scaled)
  
if __name__ == "__main__":
    main()
