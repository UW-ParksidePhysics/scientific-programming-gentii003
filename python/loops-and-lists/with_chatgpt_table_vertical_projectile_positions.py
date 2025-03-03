import numpy as np

# Define constants
v0 = 10  # Initial velocity (m/s)
g = 9.81  # Acceleration due to gravity (m/s^2)
n = 10  # Number of intervals

# Compute t_max (time when the object reaches the ground)
t_max = 2 * v0 / g

# Compute step size
dt = t_max / n  # Uniform step size

# Initialize time variable
t = 0
i = 0  # Counter for iterations

# Print table header
print(f"{'t (s)':<10}{'y(t) (m)':<15}")
print("-" * 25)

# While loop to generate the table
while t <= t_max + 1e-6:  # Adjust for floating-point precision
    y = v0 * t - 0.5 * g * t**2
    print(f"{t:<10.2f}{y:<15.2f}")
    t += dt  # Increment time
    i += 1
