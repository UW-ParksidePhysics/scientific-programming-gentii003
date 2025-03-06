import numpy as np

initial_velocity = 10  #m/s
gravitational_acceleration = 9.8  #m/s^2
number_of_intervals = 10

maximum_time = 2 * initial_velocity / gravitational_acceleration
times = np.linspace(0, maximum_time, number_of_intervals + 1)

position = 0
time = 0
time_interval = (maximum_time - time)/number_of_intervals

while time <= maximum_time:
    position = initial_velocity * time - 0.5 * gravitational_acceleration * time ** 2
    print(f"{time:<10.2f}{position:<15.2f}")
    time += time_interval

#for loop
#pick 2 solid objects and compare time

