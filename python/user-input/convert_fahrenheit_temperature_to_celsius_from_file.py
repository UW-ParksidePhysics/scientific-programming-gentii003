with open("temperature_data.txt", "r") as file:
    lines = file.readlines()

fourth_line = lines[3].strip().split()
fahrenheit = float(fourth_line[2])
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {celsius:.2f}°C")
