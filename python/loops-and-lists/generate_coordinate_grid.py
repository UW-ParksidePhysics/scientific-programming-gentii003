start_point = 1
end_point = 2
number_of_intervals = 20

step_size = (end_point - start_point)/number_of_intervals

coordinates_list = []
for i in range(number_of_intervals + 1):
    coordinate = start_point + i * step_size
    coordinates_list.append(coordinate)

print(coordinates_list)

# Using list comprehension
coordinates_list_comprehension = [start_point + index * step_size for index in range(number_of_intervals + 1)]

# Print the result
print(coordinates_list_comprehension)
