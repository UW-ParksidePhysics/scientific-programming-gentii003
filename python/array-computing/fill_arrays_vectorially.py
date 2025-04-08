import numpy as np

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

x_values = np.linspace(-4, 4, 41)
y_values = gaussian(x_values)

for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, g(x) = {y:.5f}")

if __name__ == "__main__":
    gaussian(x_values)
