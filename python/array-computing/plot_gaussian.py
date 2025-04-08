import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Generate x and y values
x_values = np.linspace(-4, 4, 1000)
y_values = gaussian(x_values)

# Plot
plt.plot(x_values, y_values, label=r"$g(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$")
plt.title("Gaussian Function")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.legend()
plt.show()


if __name__ == "__main__":