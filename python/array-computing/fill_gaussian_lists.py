import numpy as np

def gaussian(position):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * position**2)

positions = np.linspace(-4, 4, 41)
gaussian_values = [gaussian(x) for x in positions]

for x, g in zip(positions, gaussian_values):
    print(f"x = {x:.2f}, g(x) = {g:.5f}")
