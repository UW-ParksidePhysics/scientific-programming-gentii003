#### RENAME from orbital icons.py to (your_project_short_name).py
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

"""docstring statement"""



import numpy as np
import matplotlib.pyplot as plt

def draw_sun():
    sun = plt.Circle((1, 1), radius=0.25, color='yellow', fill=False)

    fig, ax = plt.subplots(1)

    ax.add_patch(sun)

    ax.set_aspect('equal', adjustable='box')

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    print(sun)
    plt.show()



def draw_orbit():

    a = 10
    b = 5
    center_x = 0
    center_y = 0

    #points for the ellipse
    t = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(t) + center_x
    y = b * np.sin(t) + center_y

    # Plot the orbit
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Orbit')


    plt.scatter(center_x, center_y, marker='+', label='Center')

    #plt.xlabel('X-axis')
    #plt.ylabel('Y-axis')
    #plt.title('Elliptical Orbit')

    #plt.legend()
    #plt.gca().set_aspect('equal', adjustable='box')
    #plt.grid(True)
    #plt.show()


def draw_guidlines():
    pass


def label_icon():
    pass


def draw_angle_arc():
    pass


def draw_object():
    pass


def semimajor_axis():
    pass


if __name__ == '__main__':
    circle = plt.Circle((1, 1), radius=0.25, color='yellow', fill=False)
    fig, ax = plt.subplots(circle)
    ax.add_patch(circle)


plt.show()



