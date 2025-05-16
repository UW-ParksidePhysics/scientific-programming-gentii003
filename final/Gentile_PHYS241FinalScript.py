"""
Equation of State

This script reads volume and energy data, converts the units,
fits a quadratic equation, calculates the bulk modulus(I did not get it to work), and plots the result.

computes:
- Unit conversion to Å³/atom and eV/atom
- Quadratic fit and bulk modulus calculation
- Annotated plot with symmetry, chemical symbol, bulk modulus, and equilibrium volume
- Optional display or PNG export via `display_graph`

Set `display_graph = True` to show the plot, or `False` to save it as a PNG.
"""
__author__ = 'Sophia Gentile'


import numpy as np
import matplotlib.pyplot as plt

from calculate_lowest_eigenvector import calculate_lowest_eigenvectors
from generate_matrix import generate_matrix
from python.matrices.eigenvectors import eigenvalues
from read_two_columns_text import read_columns
from calaculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from convert_units import convert_units, calculate_bulk_modulus
from equations_of_state import fit_equation_of_state
from datetime import date


def parse_file_name(filename):
    parts = filename.split('.')
    chemical_symbol = parts[0]
    crystal_symbol = parts[1]
    density_function = parts[2]
    return chemical_symbol, crystal_symbol, density_function


if __name__ == "__main__":
    #parse file
    file_name = 'ag.Fm-3m.GGA-PBE'
    chemical_symbol, crystal_symbol, density_function = parse_file_name(file_name)
    print(f'chemical_symbol: {chemical_symbol}')
    print(f'crystal_symbol: {crystal_symbol}')
    print(f'density_function: {density_function}')

    #read data
    data = read_columns('ag.Fm-3m.GGA-PBE')
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
    fit_eos = fit_equation_of_state(data[0], data[1], coefficients, 'murnaghan', 90)
    print(fit_eos)

    #def fit_equation_of_state(volumes, energies, quadratic_coefficients, equation_of_state='vinet',
    #number_of_points=50):

    #convert units
    volume = convert_units(data[0], "cubic_bohr/atom", "cubic_angstrom/atom")
    energy = convert_units(data[1], "rydberg/atom", "electron_volt/atom")
    b = convert_units(1, "rydberg/cubic_bohr", "gigapascal")

    print("Converted volume values (Å³/atom):", volume)
    print("Converted energy values (eV/atom):", energy)

    #bulk modulus calculation
    bulk_modulus = calculate_bulk_modulus(volume, energy)
    equilibrium_volume = volume[np.argmin(np.polyval(np.polyfit(volume, energy, 2), volume))]
    print(f"Equilibrium volume V₀ ≈ {equilibrium_volume:.3f} Å³/atom")

    print(f"Bulk modulus ≈ {bulk_modulus:.2f} GPa")

    #plot units(might be extra)
    volume = convert_units(data[0], "cubic_bohr/atom", "cubic_angstrom/atom")
    energy = convert_units(data[1], "rydberg/atom", "electron_volt/atom")

    coeff = np.polyfit(volume, energy, 2)
    volume_fit = np.linspace(min(volume), max(volume), 200)
    energy_fit = np.polyval(coeff, volume_fit)

    equilibrium_volume = volume_fit[np.argmin(energy_fit)]
    min_energy = min(energy_fit)

    #plotting
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.plot(volume, energy, 'bo')
    plt.plot(volume_fit, energy_fit, 'k-')
    plt.plot([equilibrium_volume, equilibrium_volume], [plt.ylim()[0], min_energy],
             linestyle='--', color='black', linewidth=1)
    y_bottom, y_top = plt.ylim()
    y_text = min_energy + 0.5 * (y_bottom - min_energy)
    plt.draw()

    #padding
    x_pad = 0.1 * (max(volume) - min(volume))
    y_pad = 0.1 * (max(energy) - min(energy))
    plt.xlim(min(volume) - x_pad, max(volume) + x_pad)
    plt.ylim(min(energy) - y_pad, max(energy) + y_pad)
    plt.xlabel(r'Volume $V$ (Å$^3$/atom)')
    plt.ylabel(r'Energy $E$ (eV/atom)')

    # annotate
    plt.text(0.05, 0.938, 'Ag', transform=fig.transFigure, fontsize=26)
    plt.text(0.53, 0.20, r'$Fm\overline{3}m$', transform=ax.transAxes, fontsize=15, fontstyle='italic')
    plt.text(0.54, 0.25, f"{bulk_modulus:.1f} GPa", transform=ax.transAxes, fontsize=10)
    #plt.text(0.6,  0.7,f"{equilibrium_volume:.2f} Å³/atom", fontsize=12, color='black', ha='left', va='center')
    plt.text(0.60, 0.05, f"{equilibrium_volume:.2f} Å³/atom", transform=ax.transAxes, fontsize=10)

    fit_function_name = "Murnaghan"
    plt.title(f"{fit_function_name} Equation of State for {chemical_symbol} in DFT {density_function}")
    today_str = date.today().isoformat()
    fig.text(0.01, 0.01, f"Created by Sophia Gentile {today_str}", ha='left', fontsize=8)


    #part 2
    dimension_number = 90
    length_scale = 1
    minimum_x = -10
    maximum_x = 10
    parameter = 4
    potential_names = 'sinusoidal'

    total_matrix = generate_matrix(minimum_x,maximum_x,dimension_number,length_scale,potential_names)
    print(total_matrix)

    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(total_matrix, 3)
    print(f"Eigenvalues: {eigenvalues}")
    x = np.linspace(minimum_x, maximum_x, dimension_number)

    # Plot eigenvectors
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['tab:blue', 'tab:orange', 'tab:green']

    for i, vec in enumerate(eigenvectors):
        if vec[np.argmax(np.abs(vec))] < 0:
            vec = -vec
        vec /= np.linalg.norm(vec)
        ax.plot(x, vec, color=colors[i], label=fr"$\psi_{{{i}}} \ E{{{i}}} = {eigenvalues[i]}$")


    ax.set_xlabel("x [a.u.]")
    ax.set_ylabel(r"$\psi_n(x)$ [a.u.]")
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("Eigenvectors in a Sinusoidal Potential")
    ax.legend()
    fig.text(0.01, 0.01, f"Created by Sophia Gentile {today_str}", ha='left', fontsize=8)
    plt.title(f"Select Wavefunction for{potential_names} Potential on a Spatial Grid of{dimension_number} Points")


    display_graph = True
    if display_graph:
        plt.show()
    else:
        plt.savefig("SinusoidalPotential.png")
        plt.close()


