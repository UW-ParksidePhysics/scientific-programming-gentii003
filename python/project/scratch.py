import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

def draw_sun(ax,center=(0, 0), radius=.25):

    fig, ax = plt.subplots()
    star = plt.Circle((0, 0), 0.2, color='yellow', zorder=2)
    ax.add_patch(star)

    plt.show()


def draw_planet(radius, semi_major, semi_minor, orbit_center, inclination_deg, t, color='red'):

    semi_major = 4
    semi_minor = -2
    t = np.radians(t)
    orbit_center = (orbit_center[0], orbit_center[1])
    θ = np.deg2rad(inclination_deg)
    x = semi_major * np.cos(t) * np.cos(θ) - semi_minor * np.sin(t) * np.sin(θ) + orbit_center[0]
    y = semi_major * np.cos(t) * np.sin(θ) + semi_minor * np.sin(t) * np.cos(θ) + orbit_center[1]
    planet = Circle((x, y), radius=0.1, color=color)

    draw_planet()
    radius.add_patch(planet)

    plt.show()



if __name__ == '__main__':
    draw_sun(5)
    draw_planet(1, 4)
