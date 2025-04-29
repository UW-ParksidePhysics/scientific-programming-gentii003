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
#In this code I am creating a visual representation of orbiting icons in our solar system. With the help of multiple import functions and other defining functions
#I was able to draw the sun as well as the inclination line for each planets orbit with respect to Earths orbit. I also
# used a dictionary of symbols and data to impliment into my code for multiple inclinations to call back on.
#The planets are astronomical symbols to properly represent each planet as well as Ceres and pluto. This project
#has taught the capabilities of coding as well as furthered my knowledge of the planets. With this visualization I
#hope to represent the planets different inclinations throughout or solar system. It's very easy to view the solar system as a flat system
# was to help show that is it not though some inclinations are very small each one is still unique.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Arc


astronomical_symbols = dict(
    Sun='☉',
    Moon='☽',
    Mercury='☿',
    Venus='♀',
    Earth='⊕',
    Mars='♂',
    Jupiter='♃',
    Saturn='♄',
    Uranus='⛢',
    Neptune='♆',
    Pluto='♇',
    Ceres='⚳'
)

# Functions

def draw_sun(axis, center=(0, 0), radius=0.25):
    sun = Circle(center, radius=radius, color='white', fill=True)
    axis.add_patch(sun)
    axis.text(center[0], center[1], astronomical_symbols['Sun'],
              ha='center', va='center', fontsize=36, color='black')

def draw_orbit(axis, semi_major, semi_minor, orbit_center, inclination_deg):
    ellipse = Ellipse(xy=orbit_center, width=2*semi_major, height=2*semi_minor,
                      angle=inclination_deg, edgecolor='black', facecolor='none', linestyle='-', linewidth=1.5)
    axis.add_patch(ellipse)

def draw_guidelines(axis, y_level=0):
    axis.axhline(y=y_level, color='black', linestyle='--', linewidth=1.5, label="Earth's Orbit")

def label_icon(axis):
    axis.text(0, 0.3, "Sun", ha='center', fontsize=1, color='black')

def setup_axes(axis):
    axis.set_aspect('equal', adjustable='box')
    axis.set_xlim(-6, 6)
    axis.set_ylim(-4, 4)
    axis.legend()

def draw_inclination_arc(axis, angle_deg, center=(0,0), radius=1.5):
    visible_angle = max(angle_deg, 5)  # Minimum arc for visibility
    arc = Arc(center, width=2*radius, height=2*radius,
              theta1=0, theta2=visible_angle, color='red', linewidth=2)
    axis.add_patch(arc)

    label_angle_rad = np.deg2rad(visible_angle/2)
    x = (radius + 0.4) * np.cos(label_angle_rad)
    y = (radius + 0.4) * np.sin(label_angle_rad)

    axis.text(x, y, f"{angle_deg}°", ha='center', va='center', fontsize=12, color='red')

def place_planet_symbol(axis, semi_major, semi_minor, orbit_center, inclination_deg, t, symbol, color='red'):
    θ = np.deg2rad(inclination_deg)
    x = semi_major * np.cos(t) * np.cos(θ) - semi_minor * np.sin(t) * np.sin(θ) + orbit_center[0]
    y = semi_major * np.cos(t) * np.sin(θ) + semi_minor * np.sin(t) * np.cos(θ) + orbit_center[1]

    axis.text(x, y, symbol, fontsize=26, ha='center', va='center', color=color)

    return (x, y)

def draw_radius_line(axis, inclination_deg, length=5, sun_position=(0, 0)):
    """
    Draw a full radius line through the Sun at the inclination angle.
    """
    θ = np.deg2rad(inclination_deg)
    x_end = sun_position[0] + length * np.cos(θ)
    y_end = sun_position[1] + length * np.sin(θ)

    x_start = sun_position[0] - length * np.cos(θ)
    y_start = sun_position[1] - length * np.sin(θ)

    axis.plot(
        [x_start, x_end],
        [y_start, y_end],
        color='black', linestyle='-', linewidth=2, label='Inclination Radius'
    )




planets_data = {
    'Mercury': {'inclination': 7.0,  't': 0,           'symbol': astronomical_symbols['Mercury'], 'color': 'black'},
    'Venus':   {'inclination': 3.4,  't': np.pi/4,     'symbol': astronomical_symbols['Venus'],   'color': 'black'},
    'Earth':   {'inclination': 0.0,  't': np.pi/2,     'symbol': astronomical_symbols['Earth'],   'color': 'black'},
    'Mars':    {'inclination': 2, 't': np.pi/3,     'symbol': astronomical_symbols['Mars'],    'color': 'black'},
    'Jupiter': {'inclination': 1.3,  't': np.pi/5,     'symbol': astronomical_symbols['Jupiter'], 'color': 'black'},
    'Saturn':  {'inclination': 2.5,  't': np.pi/6,     'symbol': astronomical_symbols['Saturn'],  'color': 'black'},
    'Uranus':  {'inclination': 1,  't': np.pi/8,     'symbol': astronomical_symbols['Uranus'],  'color': 'black'},
    'Neptune': {'inclination': 2,  't': np.pi/9,     'symbol': astronomical_symbols['Neptune'], 'color': 'black'},
    'Ceres':   {'inclination': 11, 't': np.pi/7,     'symbol': astronomical_symbols['Ceres'],   'color': 'black'},
    'Pluto':   {'inclination': 17, 't': np.pi/10,    'symbol': astronomical_symbols['Pluto'], 'color': 'black'},
}


if __name__ == '__main__':
    semi_major = 4
    semi_minor = 2
    orbit_center = (0, 0)

    while True:
        print("\nAvailable planets:", ", ".join(planets_data.keys()))
        chosen_planet = input("Which planet would you like to visualize? (type 'exit' to quit): ").capitalize()

        if chosen_planet.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if chosen_planet not in planets_data:
            print(f"Planet '{chosen_planet}' not found. Please check spelling.")
            continue

        data = planets_data[chosen_planet]
        inclination = data['inclination']
        t = 0
        symbol = data['symbol']
        color = data['color']

        fig, axis = plt.subplots(figsize=(10, 8))
        draw_sun(axis)
        draw_guidelines(axis)

        draw_orbit(axis, semi_major, semi_minor, orbit_center, inclination)

        place_planet_symbol(axis, semi_major, semi_minor, orbit_center, inclination, t, symbol=symbol, color=color)
        draw_radius_line(axis, inclination)

        label_icon(axis)
        draw_inclination_arc(axis, inclination, radius=semi_major)
        setup_axes(axis)

        plt.title(f"Visualization of Inclination with {chosen_planet} {symbol}")
        plt.show()

