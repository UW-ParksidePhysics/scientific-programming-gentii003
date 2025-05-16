import numpy as np

def calculate_quadratic_fit(data):
    x = data[0]
    y = data[1]

    coeff = np.polyfit(x, y, 2)
    return coeff[::-1]