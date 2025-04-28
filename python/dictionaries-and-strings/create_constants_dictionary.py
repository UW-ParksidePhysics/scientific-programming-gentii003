def parse_constants_file(filename):

    constants = {}
    with open(filename, 'r') as file:
        lines = file.readlines()


    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        name = ' '.join(parts[:-2])
        value = float(parts[-2])

        constants[name] = value

    return constants

if __name__ == '__main__':
    constants = parse_constants_file('constants')

    for name, value in constants.items():
        print(f"{name}: {value}")
