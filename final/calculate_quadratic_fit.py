import numpy as np

def calculate_quadratic_fit(data):
    x = data[0]
    y = data[1]

    coeff = np.polyfit(x, y, 2)
    return coeff[::-1]

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])
    data = np.vstack((x, y))
    print(calculate_quadratic_fit(data))