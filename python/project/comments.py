#use ellipse
#symbol for sun and planets
#make a black nad white version adn color version and in color version make earth orbit blue
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle

def plot_orbit():
    fig, ax = plt.subplots()

    # Central yellow star
    star = plt.Circle((0, 0), 0.2, color='yellow', zorder=2)
    ax.add_patch(star)

    # Ellipse parameters
    center = (0, 0)
    width = 4
    height = 2
    angle_deg = 30
    angle_rad = np.deg2rad(angle_deg)

    # Add orbit ellipse
    orbit = Ellipse(xy=center, width=width, height=height, angle=angle_deg,
                    edgecolor='black', facecolor='none', linestyle='-', linewidth=2, zorder=1)
    ax.add_patch(orbit)

    # Earth's horizon line
    x_values = np.linspace(-3, 3, 500)
    ax.plot(x_values, np.zeros_like(x_values), color='black', linestyle='--', linewidth=1.5, label="Earth's Horizon")

    # Calculate a point on the tilted ellipse
    angle = np.pi / 4
    a = width / 2
    b = height / 2
    x_orbit = a * np.cos(angle) * np.cos(angle_rad) - b * np.sin(angle) * np.sin(angle_rad)
    y_orbit = a * np.cos(angle) * np.sin(angle_rad) + b * np.sin(angle) * np.cos(angle_rad)

    #orbiting planet
    planet = Circle((x_orbit, y_orbit), 0.1, color='black', zorder=3)
    ax.add_patch(planet)

    #plot settings
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    plot_orbit()
