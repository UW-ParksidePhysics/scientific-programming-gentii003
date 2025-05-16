"""
Visualizes the orbital inclination of planets in the solar system.

This script plots an elliptical orbit around the Sun, draws an inclination angle arc,
guidelines for Earth's orbital plane, and places the selected planet symbol along its inclined orbit.
It uses planetary inclination data and lets the user choose which planet to visualize.

Modules:
    - numpy
    - matplotlib.pyplot
    - matplotlib.patches (Circle, Ellipse, Arc)
    - data (contains planetary inclination and symbol data)

Run this script directly to interactively visualize different planetary orbits and inclinations.
"""

#In this code I am creating a visual representation of orbiting icons in our solar system. With the help of multiple import functions and other defining functions
#I was able to draw the sun as well as the inclination line for each planets orbit with respect to Earths orbit. I also
# used a dictionary of symbols and data to implement into my code for multiple inclinations to call back on.
#The planets are astronomical symbols to properly represent each planet as well as Ceres and pluto. This project
#has taught the capabilities of coding as well as furthered my knowledge of the planets. With this visualization I
#hope to represent the planets different inclinations throughout or solar system. It's very easy to view the solar system as a flat system
# was to help show that is it not though some inclinations are very small each one is still unique.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Arc
from data import astronomical_symbols, planets_data


# Functions
# Draws the Sun at the center of the plot
def draw_sun(ax, center=(0, 0), radius=0.25):
    sun = Circle(center, radius=radius, color='white', fill=True)
    ax.add_patch(sun)
    ax.text(center[0], center[1], astronomical_symbols['Sun'],
              ha='center', va='center', fontsize=36, color='black')

# Draws a horizontal dashed line to represent Earth’s orbital plane (baseline for comparison)
def draw_orbit(ax, semi_maj, semi_min, orbiting_center, inclination_deg):
    ellipse = Ellipse(xy=orbiting_center, width=2 * semi_maj, height=2 * semi_min,
                      angle=inclination_deg, edgecolor='black', facecolor='none', linestyle='-', linewidth=1.5)
    ax.add_patch(ellipse)
# Draws a horizontal dashed line to represent Earth’s orbital plane

def draw_guidelines(ax, y_level=0):
    ax.axhline(y=y_level, color='black', linestyle='--', linewidth=1.5, label="Earth's Orbit")

#Adds a small label
def label_icon(ax):
    ax.text(0, 0.3, "Sun", ha='center', fontsize=1, color='black')

# Adjusts the graph
def setup_axes(ax):
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.legend()

# Draws a red curved arc representing the angle of inclination
def draw_inclination_arc(ax, angle_deg, center=(0, 0), radius=1):
    visible_angle = max(angle_deg, 5)  # Minimum arc for visibility
    arc = Arc(center, width=2*radius, height=2*radius,
              theta1=0, theta2=visible_angle, color='red', linewidth=2)
    ax.add_patch(arc)

    label_angle_rad = np.deg2rad(visible_angle/2)
    x = (radius + 0.4) * np.cos(label_angle_rad) # change 0.4 to something larger i think
    y = (radius + 0.4) * np.sin(label_angle_rad) # change 0.4 to something larger i think

    ax.text(x, y, f"{angle_deg}°", ha='center', va='center', fontsize=12, color='red')

# Puts the planet's symbol somewhere on its orbit
def place_planet_symbol(ax, semi_maj, semi_min, orbiting_center, inclination_deg, t, symbol, color='red'):
    θ = np.deg2rad(inclination_deg)
    x = semi_maj * np.cos(t) * np.cos(θ) - semi_min * np.sin(t) * np.sin(θ) + orbiting_center[0]
    y = semi_maj * np.cos(t) * np.sin(θ) + semi_min * np.sin(t) * np.cos(θ) + orbiting_center[1]

    ax.text(x, y, symbol, fontsize=26, ha='center', va='center', color=color)

    return x, y

# Draws a straight inclined line through the Sun, showing the angle of the orbit tilt
def draw_radius_line(ax, inclination_deg, length=5, sun_position=(0, 0)):

    θ = np.deg2rad(inclination_deg)
    x_end = sun_position[0] + length * np.cos(θ)
    y_end = sun_position[1] + length * np.sin(θ)

    x_start = sun_position[0] - length * np.cos(θ)
    y_start = sun_position[1] - length * np.sin(θ)

    ax.plot(
        [x_start, x_end],
        [y_start, y_end],
        color='black', linestyle='-', linewidth=2, label='Inclination Radius'
    )

# main program that runs when you launch the file
if __name__ == '__main__':
    semi_major = 4
    semi_minor = 2
    orbit_center = (0, 0)

    for planet in planets_data:
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

