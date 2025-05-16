from scipy.stats import describe
import numpy as np
import matplotlib.pyplot as plt
from equations_of_state import fit_equation_of_state
from scipy.constants import physical_constants


def parse_file_name(filename):
    parts = filename.split('.')
    chemical_symbol = parts[0]
    crystal_symbol = parts[1]
    density_function = parts[2]
    return chemical_symbol, crystal_symbol, density_function

def read_file(filename):

    with open(filename,'r') as file:
        file_data = np.loadtxt(filename).T
        return file_data

def calculate_bivariate_statistics(data):
    """
    Calculate bivariate statistics of ag
    """
    x, y = data[0], data[1]

    y_stats = describe(y)

    return [
        y_stats.mean,
        np.sqrt(y_stats.variance),
        min(x),max(x),
        min(y),max(y),
    ]


def calculate_quadratic_fit(data):
    x = data[0]
    y = data[1]

    coeff = np.polyfit(x, y, 2)
    return coeff[::-1]


# Conversion factors
BOHR_TO_ANGSTROM = physical_constants["Bohr radius"][0] * 1e10  # meters to angstroms
RYDBERG_TO_EV = physical_constants["Rydberg constant times hc in eV"][0]  # eV
HARTREE_TO_JOULES = physical_constants["Hartree energy"][0]  # J
RYDBERG_TO_JOULES = HARTREE_TO_JOULES / 2  # 1 Ry = 0.5 Hartree
BOHR_VOLUME_TO_ANGSTROM3 = BOHR_TO_ANGSTROM ** 3  # (bohr^3) to angstrom^3
RYDBERG_PER_BOHR3_TO_GPA = (RYDBERG_TO_JOULES / (BOHR_TO_ANGSTROM ** 3)) / 1e9  # Pa to GPa

def convert_units(value, from_units, to_units):
    if from_units == "cubic_bohr/atom" and to_units == "cubic_angstrom/atom":
        return value * BOHR_VOLUME_TO_ANGSTROM3
    elif from_units == "rydberg/atom" and to_units == "electron_volt/atom":
        return value * RYDBERG_TO_EV
    elif from_units == "rydberg/cubic_bohr" and to_units == "gigapascal":
        return value * RYDBERG_PER_BOHR3_TO_GPA
    else:
        raise ValueError(f"Unsupported conversion from {from_units} to {to_units}")





if __name__ == "__main__":
    #parse file
    file_name = 'ag.Fm-3m.GGA-PBE'
    chemical_symbol, crystal_symbol, density_function = parse_file_name(file_name)
    print(f'chemical_symbol: {chemical_symbol}')
    print(f'crystal_symbol: {crystal_symbol}')
    print(f'density_function: {density_function}')

    #read data
    data = read_file('ag.Fm-3m.GGA-PBE')
    print(f'{data=}, shape={data.shape}')

    #calculate bivariate statistics
    results = calculate_bivariate_statistics(data)

    stats = calculate_bivariate_statistics(data)
    print("mean of y", results[0])
    print("standard deviation of y", results[1])
    print("min(x)", results[2])
    print("max(x)", results[3])
    print("min(y)", results[4])
    print("max(y)", results[5])

     #Quadratic fit
    x_values = np.linspace(-2, 2, 5)
    y_values = 1 + 2 * x_values + 3 * x_values ** 2
    coefficients = calculate_quadratic_fit(data)

    #data = [np.linspace(-1, 1), np.linspace(-1, 1) ** 2]
    print(f"Quadratic coefficients:, {coefficients}\n")

    #fit_eos
    fit_eos = fit_equation_of_state(data[0], data[1], coefficients, 'murnaghan',90)
    print(fit_eos)

    #def fit_equation_of_state(volumes, energies, quadratic_coefficients, equation_of_state='vinet',
                              #number_of_points=50):
    #convert units

    volume = convert_units([0], "cubic_bohr/atom", "cubic_angstrom/atom")
    energy = convert_units([1], "rydberg/atom", "electron_volt/atom")
    b = convert_units(1, "rydberg/cubic_bohr", "gigapascal")


    print("1 cubic bohr/atom =", convert_units(1, "cubic_bohr/atom", "cubic_angstrom/atom"), "cubic angstroms/atom")
    print("1 rydberg/atom =", convert_units(1, "rydberg/atom", "electron_volt/atom"), "electron volts/atom")
    print("1 rydberg/cubic bohr =", convert_units(1, "rydberg/cubic_bohr", "gigapascal"), "GPa")

    #print(f"1 cubic bohr/atom = {volume} cubic angstroms/atom")
    #print(f"1 rydberg/atom = {energy} electron volts/atom")
    #print(f"1 rydberg/cubic bohr = {b} gigapascals")


    #plot units
    volume = convert_units(data[0], "cubic_bohr/atom", "cubic_angstrom/atom")
    energy = convert_units(data[1], "rydberg/atom", "electron_volt/atom")

    coeff = np.polyfit(volume, energy, 2)
    volume_fit = np.linspace(min(volume), max(volume), 200)
    energy_fit = np.polyval(coeff, volume_fit)

    fig, ax = plt.subplots(figsize=(10, 8))
    plt.plot(volume, energy, 'bo')
    plt.plot(volume_fit, energy_fit, 'k-')

    #padding
    x_pad = 0.1 * (max(volume) - min(volume))
    y_pad = 0.1 * (max(energy) - min(energy))
    plt.xlim(min(volume) - x_pad, max(volume) + x_pad)
    plt.ylim(min(energy) - y_pad, max(energy) + y_pad)
    plt.xlabel(r'Volume $V$ (Å$^3$/atom)')
    plt.ylabel(r'Energy $E$ (eV/atom)')

    # annotate
    plt.text(0.05,0.938,'Ag',transform=fig.transFigure,fontsize=26)
    plt.text(0.53, 0.20, r'$Fm\overline{3}m$', transform=ax.transAxes, fontsize=15,fontstyle='italic')

    plt.show()





