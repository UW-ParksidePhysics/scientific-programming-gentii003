#def sum_series(x_value, number_of_terms):
 #   summation = 0
  #  for index in range(1, number_of_terms + 1):
   #     summation += (1.0 / index) * (x_value / (1.0 + x_value))**index
    #return summation


# def calculate_sum_and_error(x_value, number_of_terms):
#     summation = 0
#     for index in range(1, number_of_terms + 1):
#         summation += (1.0 / index) * (x_value / (1.0 + x_value))**index
#     sum_value = summation
#     next_term = (1.0 / (number_of_terms + 1)) * (x_value / (1.0 + x_value))**(number_of_terms + 1)
#     from math import log
#     exact_error = log(1 + x_value) - sum_value
#     return sum_value, next_term, exact_error
#
#
# def print_sum_table(x_value):
#     from math import log
#     print('\nx=%g, ln(1+x)=%g' % (x_value, log(1 + x_value)))
#     for number_of_terms in [1, 2, 10, 100, 500]:
#         value, next_term, error = calculate_sum_and_error(x_value, number_of_terms)
#         print('n=%-4d %-10g  (next term: %8.2e  '
#               'error: %8.2e)' % (number_of_terms, value, next_term, error))
#
#
# def calculate_sum_with_epsilon(x_value, epsilon=1.0E-6):
#     x_value = float(x_value)
#     index = 1
#     term = (1.0 / index) * (x_value / (1 + x_value))**index
#     summation = term
#     while abs(term) > epsilon:
#         index += 1
#         term = (1.0 / index) * (x_value / (1 + x_value))**index
#         summation += term
#     return summation, index
#
#
# def print_epsilon_table(x_value):
#     from math import log
#     for index in range(4, 14, 2):
#         epsilon = 10**(-index)
#         approximation, number_of_terms = calculate_sum_with_epsilon(x_value, epsilon=epsilon)
#         exact = log(1 + x_value)
#         exact_error = exact - approximation
#         print('epsilon: %5.0e, exact error: %8.2e, n=%d' %
#               (epsilon, exact_error, number_of_terms))
#
#
# if __name__ == '__main__':
#     print_sum_table(10)
#     print_sum_table(100)
#     print_sum_table(1000)
#
#     print('\n\n')
#     print_epsilon_table(10)
#


# read_and_plot_logarithmic_sum_output.py

import matplotlib.pyplot as plt

def parse_sum_output(filename):
    """
    Parse the file logarithmic_sum.out and extract tolerances, errors, and maximum indices.
    Returns three lists.
    """
    tolerances = []
    errors = []
    maximum_indices = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('epsilon:'):
                parts = line.split(',')
                epsilon_part = parts[0].split(':')[1].strip()
                error_part = parts[1].split(':')[1].strip()
                n_part = parts[2].split('=')[1].strip()

                epsilon = float(epsilon_part)
                error = float(error_part)
                n = int(n_part)

                tolerances.append(epsilon)
                errors.append(error)
                maximum_indices.append(n)

    return tolerances, errors, maximum_indices

def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    """
    Plot approximation error vs maximum index n.
    y-axis is logarithmic scale.
    """
    plt.figure(figsize=(8,6))
    plt.semilogy(maximum_indices, errors, 'bo-', label='Approximation Error Δ')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Approximation Error (Δ)')
    plt.title('Error vs Maximum Index')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    tolerances, errors, maximum_indices = parse_sum_output('logarithmic_sums')
    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)



