#### RENAME from project.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
#In this code I am creating a visual representation of orbiting icons in our solar system.

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()

# Parameters
circle_radius = .5
ellipse_a = 2  # semi-major axis
ellipse_b = 1  # semi-minor axis

# Angle values
theta = np.linspace(0, 2 * np.pi, 300)

# Circle coordinates
circle_x = circle_radius * np.cos(theta)
circle_y = circle_radius * np.sin(theta)

# Ellipse coordinates
ellipse_x = ellipse_a * np.cos(theta)
ellipse_y = ellipse_b * np.sin(theta)

# Plot the yellow circle
ax.plot(circle_x, circle_y, color='yellow', linewidth=2)
ax.fill(circle_x, circle_y, color='yellow', alpha=0.6)

# Plot the ellipse
ax.plot(ellipse_x, ellipse_y, color='blue', linewidth=2)

# Formatting
ax.set_aspect('equal')
ax.set_xlim(-ellipse_a - 0.5, ellipse_a + 0.5)
ax.set_ylim(-ellipse_b - 0.5, ellipse_b + 0.5)


# Show the plot
plt.show()
