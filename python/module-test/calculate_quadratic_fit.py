import numpy as np

def calculate_quadratic_fit(filename):
    """Fits a quadratic polynomial from file_data and returns
    the coefficients in correct order"""

    data = np.loadtxt(filename)
    x = data[0]
    y = data[1]
    coefficients = np.polyfit(x, y, 2)
    return coefficients[::-1]

if __name__ == "__main__":
    coefficients = calculate_quadratic_fit('volume_energies')
    print(coefficients)