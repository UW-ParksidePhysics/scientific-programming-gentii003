import matplotlib.pyplot as plt
import numpy as np

def parse_viscosity_data(filename):
    """
    Parses viscosity_of_gases.dat and returns a nested dictionary.
    """
    viscosity_data = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):  # skip blank and comment lines
            parts = line.split()
            if len(parts) >= 4:
                gas_name = ' '.join(parts[:-3])
                C = float(parts[-3])
                T0 = float(parts[-2])
                mu0 = float(parts[-1])

                viscosity_data[gas_name] = {
                    'viscosity': C,
                    'reference_temperature': T0,
                    'reference_viscosity': mu0
                }

    return viscosity_data

def calculate_viscosity(temperature, gas, viscosity_data):
    """
    Calculates viscosity μ(T) for a gas using the given data.
    """
    C = viscosity_data[gas]['viscosity']
    T0 = viscosity_data[gas]['reference_temperature']
    mu0 = viscosity_data[gas]['reference_viscosity']

    viscosity = mu0 * ((T0 - C) / (temperature + C)) * (temperature / T0)**1.5
    return viscosity

def plot_viscosity(viscosity_data):
    """
    Plots viscosity μ(T) vs T for Air, Carbon dioxide, and Hydrogen.
    """
    temperatures = np.linspace(223, 373, 200)

    gases = ['Air', 'Carbon dioxide', 'Hydrogen']

    plt.figure(figsize=(10, 6))

    for gas in gases:
        viscosities = [calculate_viscosity(T, gas, viscosity_data) for T in temperatures]
        plt.plot(temperatures, viscosities, label=gas)

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity (μ)')
    plt.title('Viscosity vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    viscosity_data = parse_viscosity_data('viscosity_of_gases')
    plot_viscosity(viscosity_data)
