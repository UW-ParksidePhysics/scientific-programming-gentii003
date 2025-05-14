from scipy.stats import describe
import numpy as np

def parse_file_name(filename):
    parts = filename.split('.')
    chemical_symbol = parts[0]
    crystal_symbol = parts[1]
    density_function = parts[2]
    return chemical_symbol, crystal_symbol, density_function

def read_file(filename):

    with open(filename,'r') as file:
        file_data = np.loadtxt(filename)
        return file_data

def calculate_bivariate_statistics(data):
    """
    Calculate bivariate statistics of ag
    """
    x, y = data
    y_stats = describe(y)

    return [
        y_stats.mean,
        np.sqrt(y_stats.variance),
        min(x),
        max(x),
        min(y),
        max(y),
    ]


def calculate_quadratic_fit(data):
    x = data[0]
    y = data[1]

    coeff = np.polyfit(x, y, 2)
    return coeff[::-1]


if __name__ == "__main__":
    file_name = 'ag.Fm-3m.GGA-PBE'
    chemical_symbol, crystal_symbol, density_function = parse_file_name(file_name)
    #print("=== File Metadata ===")
    print(f'chemical_symbol: {chemical_symbol}')
    print(f'crystal_symbol: {crystal_symbol}')
    print(f'density_function: {density_function}')

    data = read_file('ag.Fm-3m.GGA-PBE')
    print(f'{data=}, shape={data.shape}')

    data = np.loadtxt("ag.Fm-3m.GGA-PBE").T
    results = calculate_bivariate_statistics(data)

    stats = calculate_bivariate_statistics(data)
    print("mean of y", results[0])
    print("standard deviation of y", results[1])
    print("min(x)", results[2])
    print("max(x)", results[3])
    print("min(y)", results[4])
    print("max(y)", results[5])

    x_values = np.linspace(-2, 2, 5)
    y_values = 1 + 2 * x_values + 3 * x_values ** 2
    coefficients = calculate_quadratic_fit(data)

    data = [np.linspace(-1, 1), np.linspace(-1, 1) ** 2]
    print("Quadratic coefficients", coefficients)
