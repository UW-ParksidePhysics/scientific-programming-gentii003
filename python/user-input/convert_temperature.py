def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def test_conversion():
    tolerance = 1e-6
    passed = True

    # Test round-trip conversions
    f_temp = 100
    c_temp = fahrenheit_to_celsius(f_temp)
    f_back = celsius_to_fahrenheit(c_temp)
    if abs(f_temp - f_back) > tolerance:
        print("Failed: Fahrenheit -> Celsius -> Fahrenheit")
        passed = False

    c_temp = 25
    k_temp = celsius_to_kelvin(c_temp)
    c_back = kelvin_to_celsius(k_temp)
    if abs(c_temp - c_back) > tolerance:
        print("Failed: Celsius -> Kelvin -> Celsius")
        passed = False

    f_temp = 212
    k_temp = fahrenheit_to_kelvin(f_temp)
    f_back = kelvin_to_fahrenheit(k_temp)
    if abs(f_temp - f_back) > tolerance:
        print("Failed: Fahrenheit -> Kelvin -> Fahrenheit")
        passed = False

    if passed:
        print("All conversion tests passed.")
    else:
        assert False, "One or more conversion tests failed."



if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        test_conversion()