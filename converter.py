def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("Choose conversion type:")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Volume")
        print("5. Time")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            convert_temperature()
        elif choice == '2':
            convert_length()
        elif choice == '3':
            convert_weight()
        elif choice == '4':
            convert_volume()
        elif choice == '5':
            convert_time()
        elif choice == '6':
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def convert_temperature():
    print("\n--- Temperature Conversion ---")
    print("Available units: Celsius (C), Fahrenheit (F), Kelvin (K)")
    from_unit_raw = input("Convert from (e.g., C, F, K): ").strip().upper()
    to_unit_raw = input("Convert to (e.g., C, F, K): ").strip().upper()

    from_unit = from_unit_raw
    to_unit = to_unit_raw

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit_raw} is equal to {value} {to_unit_raw}")
    elif from_unit == 'C' or from_unit_raw.startswith('CEL'):
        if to_unit == 'F' or to_unit_raw.startswith('FAH'):
            result = (value * 9/5) + 32
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'K' or to_unit_raw.startswith('KEL'):
            result = value + 273.15
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported temperature conversion.")
    elif from_unit == 'F' or from_unit_raw.startswith('FAH'):
        if to_unit == 'C' or to_unit_raw.startswith('CEL'):
            result = (value - 32) * 5/9
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'K' or to_unit_raw.startswith('KEL'):
            result = (value - 32) * 5/9 + 273.15
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported temperature conversion.")
    elif from_unit == 'K' or from_unit_raw.startswith('KEL'):
        if to_unit == 'C' or to_unit_raw.startswith('CEL'):
            result = value - 273.15
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'F' or to_unit_raw.startswith('FAH'):
            result = (value - 273.15) * 9/5 + 32
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported temperature conversion.")
    else:
        print(f"Invalid 'from' unit: {from_unit_raw}")

def convert_length():
    print("\n--- Length Conversion ---")
    print("Available units: Meters (M), Kilometers (KM), Miles (MI), Feet (FT)")
    from_unit_raw = input("Convert from (e.g., M, KM, MI, FT): ").strip().upper()
    to_unit_raw = input("Convert to (e.g., M, KM, MI, FT): ").strip().upper()

    from_unit = from_unit_raw
    to_unit = to_unit_raw

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit_raw} is equal to {value} {to_unit_raw}")
    elif from_unit == 'M' or from_unit_raw.startswith('MET'):
        if to_unit == 'KM' or to_unit_raw.startswith('KIL'):
            result = value / 1000
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'MI' or to_unit_raw.startswith('MIL'):
            result = value / 1609.34
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'FT' or to_unit_raw.startswith('FEE'):
            result = value * 3.28084
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported length conversion.")
    elif from_unit == 'KM' or from_unit_raw.startswith('KIL'):
        if to_unit == 'M' or to_unit_raw.startswith('MET'):
            result = value * 1000
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'MI' or to_unit_raw.startswith('MIL'):
            result = value / 1.60934
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'FT' or to_unit_raw.startswith('FEE'):
            result = value * 3280.84
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported length conversion.")
    elif from_unit == 'MI' or from_unit_raw.startswith('MIL'):
        if to_unit == 'M' or to_unit_raw.startswith('MET'):
            result = value * 1609.34
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'KM' or to_unit_raw.startswith('KIL'):
            result = value * 1.60934
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'FT' or to_unit_raw.startswith('FEE'):
            result = value * 5280
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported length conversion.")
    elif from_unit == 'FT' or from_unit_raw.startswith('FEE'):
        if to_unit == 'M' or to_unit_raw.startswith('MET'):
            result = value / 3.28084
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'KM' or to_unit_raw.startswith('KIL'):
            result = value / 3280.84
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'MI' or to_unit_raw.startswith('MIL'):
            result = value / 5280
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported length conversion.")
    else:
        print(f"Invalid 'from' unit: {from_unit_raw}")

def convert_weight():
    print("\n--- Weight Conversion ---")
    print("Available units: Kilograms (KG), Pounds (LB), Ounces (OZ)")
    from_unit_raw = input("Convert from (e.g., KG, LB, OZ): ").strip().upper()
    to_unit_raw = input("Convert to (e.g., KG, LB, OZ): ").strip().upper()

    from_unit = from_unit_raw
    to_unit = to_unit_raw

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit_raw} is equal to {value} {to_unit_raw}")
    elif from_unit == 'KG' or from_unit_raw.startswith('KIL'):
        if to_unit == 'LB' or to_unit_raw.startswith('POU'):
            result = value * 2.20462
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'OZ' or to_unit_raw.startswith('OUN'):
            result = value * 35.274
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported weight conversion.")
    elif from_unit == 'LB' or from_unit_raw.startswith('POU'):
        if to_unit == 'KG' or to_unit_raw.startswith('KIL'):
            result = value / 2.20462
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'OZ' or to_unit_raw.startswith('OUN'):
            result = value * 16
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported weight conversion.")
    elif from_unit == 'OZ' or from_unit_raw.startswith('OUN'):
        if to_unit == 'KG' or to_unit_raw.startswith('KIL'):
            result = value / 35.274
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'LB' or to_unit_raw.startswith('POU'):
            result = value / 16
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported weight conversion.")
    else:
        print(f"Invalid 'from' unit: {from_unit_raw}")

def convert_volume():
    print("\n--- Volume Conversion ---")
    print("Available units: Liters (L), Gallons (GAL), Milliliters (ML)")
    from_unit_raw = input("Convert from (e.g., L, GAL, ML): ").strip().upper()
    to_unit_raw = input("Convert to (e.g., L, GAL, ML): ").strip().upper()

    from_unit = from_unit_raw
    to_unit = to_unit_raw

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit_raw} is equal to {value} {to_unit_raw}")
    elif from_unit == 'L' or from_unit_raw.startswith('LIT'):
        if to_unit == 'GAL' or to_unit_raw.startswith('GAL'):
            result = value / 3.78541
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'ML' or to_unit_raw.startswith('MIL'):
            result = value * 1000
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported volume conversion.")
    elif from_unit == 'GAL' or from_unit_raw.startswith('GAL'):
        if to_unit == 'L' or to_unit_raw.startswith('LIT'):
            result = value * 3.78541
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'ML' or to_unit_raw.startswith('MIL'):
            result = value * 3785.41
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported volume conversion.")
    elif from_unit == 'ML' or from_unit_raw.startswith('MIL'):
        if to_unit == 'L' or to_unit_raw.startswith('LIT'):
            result = value / 1000
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'GAL' or to_unit_raw.startswith('GAL'):
            result = value / 3785.41
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported volume conversion.")
    else:
        print(f"Invalid 'from' unit: {from_unit_raw}")

def convert_time():
    print("\n--- Time Conversion ---")
    print("Available units: Seconds (S), Minutes (MIN), Hours (H)")
    from_unit_raw = input("Convert from (e.g., S, MIN, H): ").strip().upper()
    to_unit_raw = input("Convert to (e.g., S, MIN, H): ").strip().upper()

    from_unit = from_unit_raw
    to_unit = to_unit_raw

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit_raw} is equal to {value} {to_unit_raw}")
    elif from_unit == 'S' or from_unit_raw.startswith('SEC'):
        if to_unit == 'MIN' or to_unit_raw.startswith('MIN'):
            result = value / 60
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'H' or to_unit_raw.startswith('HOU'):
            result = value / 3600
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported time conversion.")
    elif from_unit == 'MIN' or from_unit_raw.startswith('MIN'):
        if to_unit == 'S' or to_unit_raw.startswith('SEC'):
            result = value * 60
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'H' or to_unit_raw.startswith('HOU'):
            result = value / 60
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported time conversion.")
    elif from_unit == 'H' or from_unit_raw.startswith('HOU'):
        if to_unit == 'S' or to_unit_raw.startswith('SEC'):
            result = value * 3600
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        elif to_unit == 'MIN' or to_unit_raw.startswith('MIN'):
            result = value * 60
            print(f"{value} {from_unit_raw} is {result} {to_unit_raw}")
        else:
            print("Unsupported time conversion.")

if __name__ == "__main__":
    unit_converter()