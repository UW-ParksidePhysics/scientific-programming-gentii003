import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

def draw_sun(axis, center=(0, 0), radius=0.25):
    sun = Circle(center, radius=radius, color='yellow', fill=True)
    axis.add_patch(sun)

def draw_orbit(axis, semi_major, semi_minor, orbit_center, inclination_deg):
    ellipse = Ellipse(xy=orbit_center, width=2 * semi_major, height=2 * semi_minor, angle=inclination_deg,
                      edgecolor='black', facecolor='none', linestyle='-', linewidth=1.5)
    axis.add_patch(ellipse)

def draw_planet(axis, semi_major, semi_minor, orbit_center, inclination_deg, t, color='red'):
    θ = np.deg2rad(inclination_deg)
    x = semi_major * np.cos(t) * np.cos(θ) - semi_minor * np.sin(t) * np.sin(θ) + orbit_center[0]
    y = semi_major * np.cos(t) * np.sin(θ) + semi_minor * np.sin(t) * np.cos(θ) + orbit_center[1]

    planet = Circle((x, y), radius=0.1, color=color)
    axis.add_patch(planet)

def draw_guidelines(axis, y_level=0):
    axis.axhline(y=y_level, color='black', linestyle='--', linewidth=1.5, label="Earth's Orbit")

def label_icon(axis):
    axis.text(0, 0.3, "Sun", ha='center', fontsize=10, color='black')

def setup_axes(axis):
    axis.set_aspect('equal', adjustable='box')
    axis.set_xlim(-6, 6)
    axis.set_ylim(-4, 4)
    axis.legend()

def set_inclination(degrees):
    return degrees


if __name__ == '__main__':
    # Orbit parameters
    semi_major = 4                      # semi-major axis
    semi_minor = 2                      # semi-minor axis
    orbit_center = (0, 0)               # center of ellipse and sun
    inclination = 30                    # tilt angle in degrees
    t = np.pi / 4                       # position on ellipse (radians)

    # Plot setup
    fig, axis = plt.subplots(figsize=(8, 6))
    draw_sun(axis, orbit_center)
    draw_orbit(axis, semi_major, semi_minor, orbit_center, inclination)
    draw_planet(axis, semi_major, semi_minor, orbit_center, inclination, t)
    draw_guidelines(axis)
    label_icon(axis)
    setup_axes(axis)
    plt.show()

#astronomical symbols
#angle
#show all the planets on the slide
#one sig fig round up
#for loop with a list of the planets
