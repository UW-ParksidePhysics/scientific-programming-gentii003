input_filename = "temperatures.txt"
output_filename = "converted_temperatures.txt"

# Read Fahrenheit values from file
with open(input_filename, "r") as file:
    fahrenheit_values = [float(line.strip()) for line in file if line.strip()]

# Convert to Celsius
celsius_values = [(f - 32) * 5 / 9 for f in fahrenheit_values]

# Write both Fahrenheit and Celsius to output file
with open(output_filename, "w") as file:
    file.write("Fahrenheit\tCelsius\n")
    for f, c in zip(fahrenheit_values, celsius_values):
        file.write(f"{f:.2f}\t{c:.2f}\n")

print(f"Converted temperatures saved to {output_filename}")
#help from chatgbt