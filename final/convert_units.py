from scipy.constants import physical_constants
import numpy as np

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

def calculate_bulk_modulus(volume, energy):
    coeff = np.polyfit(volume, energy, 2)
    equilibrium_volume = volume[np.argmin(np.polyval(coeff, volume))]
    a = coeff[0]
    B_eVA3 = 2 * a * equilibrium_volume
    B_rydberg_per_bohr3 = B_eVA3 / RYDBERG_TO_EV * (1 / BOHR_VOLUME_TO_ANGSTROM3)
    B_GPa = convert_units(B_rydberg_per_bohr3, "rydberg/cubic_bohr", "gigapascal")
    return B_GPa


if __name__ == "__main__":
    if __name__ == "__main__":
        print("1 cubic bohr/atom =", convert_units(1, "cubic_bohr/atom", "cubic_angstrom/atom"))
        print("1 rydberg/atom =", convert_units(1, "rydberg/atom", "electron_volt/atom"))
        print("1 rydberg/cubic bohr =", convert_units(1, "rydberg/cubic_bohr", "gigapascal"))

        # Example test arrays
        volume = np.array([15, 16, 17, 18, 19])
        energy = np.array([-3.5, -3.8, -4.0, -3.85, -3.6])

        print("volume[:5] =", volume[:5])
        print("energy[:5] =", energy[:5])

        B = calculate_bulk_modulus(volume, energy)
        print(f"Test bulk modulus = {B:.2f} GPa")





