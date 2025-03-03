import numpy as np

v_0 = 10  #m/s
g = 9.8  #m/s^2
number_of_intervals = 10

t_max = (2 * v_0/g)
t_values = np.linspace(0,t_max,number_of_intervals + 1)

y=0
i = 0
while t <= t_max:
    y(t) = v_0 * - 0.5 * g * t**2
    print(f"{t:<10.2f}{y:<15.2f}")

    i += 1
    if i > number_of_intervals:
        break
        t += t_values[i]