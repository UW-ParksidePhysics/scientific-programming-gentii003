import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Arc

# --------- Astronomical Symbols Dictionary ---------
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

# --------- Functions ---------

def draw_sun(axis, center=(0, 0), radius=0.25):
    sun = Circle(center, radius=radius, color='yellow', fill=True)
    axis.add_patch(sun)
    axis.text(center[0], center[1], astronomical_symbols['Sun'],
              ha='center', va='center', fontsize=16, color='black')

def draw_orbit(axis, semi_major, semi_minor, orbit_center, inclination_deg):
    ellipse = Ellipse(xy=orbit_center, width=2*semi_major, height=2*semi_minor,
                      angle=inclination_deg, edgecolor='black', facecolor='none', linestyle='-', linewidth=1.5)
    axis.add_patch(ellipse)

def draw_guidelines(axis, y_level=0):
    axis.axhline(y=y_level, color='blue', linestyle='--', linewidth=1.5, label="Earth's Orbit")

def label_icon(axis):
    axis.text(0, 0.3, "Sun", ha='center', fontsize=10, color='black')

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

    axis.text(x, y, f"{angle_deg}°", ha='center', va='center', fontsize=10, color='red')

def place_planet_symbol(axis, semi_major, semi_minor, orbit_center, inclination_deg, t, symbol, color='red'):
    θ = np.deg2rad(inclination_deg)
    x = semi_major * np.cos(t) * np.cos(θ) - semi_minor * np.sin(t) * np.sin(θ) + orbit_center[0]
    y = semi_major * np.cos(t) * np.sin(θ) + semi_minor * np.sin(t) * np.cos(θ) + orbit_center[1]

    axis.text(x, y, symbol, fontsize=14, ha='center', va='center', color=color)

    return (x, y)

def draw_radius_line(axis, inclination_deg, length=5, sun_position=(0, 0)):
    θ = np.deg2rad(inclination_deg)
    x_end = sun_position[0] + length * np.cos(θ)
    y_end = sun_position[1] + length * np.sin(θ)

    axis.plot(
        [sun_position[0], x_end],
        [sun_position[1], y_end],
        color='black', linestyle='-', linewidth=2, label='Inclination'
    )

# --------- Planet Data ---------

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
}

# ------------------------------
# MAIN PROGRAM
# ------------------------------

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

        plt.title(f"Visualization of Inclination with {chosen_planet} {symbol} and Radius Line")
        plt.show()
