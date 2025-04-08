import numpy as np

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Create empty lists
x_values = []
y_values = []

# Fill with 41 uniformly spaced x values in [-4, 4]
for i in range(41):
    x = -4 + i * (8 / 40)  # step size = (4 - (-4)) / (41 - 1)
    x_values.append(x)
    y_values.append(gaussian(x))

# (Optional) print to verify
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, g(x) = {y:.5f}")

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")