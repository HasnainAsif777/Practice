def temperature_conversion():
    while True:
        try:
            temperature = int(input("Temperature: "))
            break
        except ValueError:
            print("Please enter valid Integer value!")
    while True:
        try:
            unit = input("Unit: ")
            if unit.upper() not in ["C", "F"]:
                raise ValueError("Invalid unit")
            break
        except ValueError:
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit ")
    if unit.upper() == "C":
        converted_temperature = temperature * 1.8 + 32
        converted_unit = "Fahrenheit"
    if unit.upper() == "F":
        converted_temperature = (temperature - 32) / 1.8
        converted_unit = "Celsius"

    return converted_temperature, converted_unit



