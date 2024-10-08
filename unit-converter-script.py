def select_unit_type():
    while True:
        unit_type = input("Select unit type (length/temperature): ").lower()
        if unit_type in ['length', 'temperature']:
            return unit_type
        print("Invalid unit type. Please choose 'length' or 'temperature'.")

def enter_value(unit_type):
    while True:
        try:
            value = float(input(f"Enter {unit_type} value: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def convert_length(value):
    units = {
        '1': ('feet', 0.3048),
        '2': ('inches', 0.0254),
        '3': ('yards', 0.9144),
        '4': ('miles', 1609.34)
    }
    
    print("Select input unit:")
    for key, (unit, _) in units.items():
        print(f"{key}. {unit}")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in units:
            input_unit, conversion_factor = units[choice]
            break
        print("Invalid choice. Please select a number between 1 and 4.")
    
    meters = value * conversion_factor
    return f"{value} {input_unit} is equal to {meters:.2f} meters"

def convert_temperature(value):
    unit = input("Enter input unit (C for Celsius, F for Fahrenheit): ").upper()
    if unit == 'C':
        celsius = value
        fahrenheit = (celsius * 9/5) + 32
        return f"{celsius}°C is equal to {fahrenheit:.2f}°F"
    elif unit == 'F':
        fahrenheit = value
        celsius = (fahrenheit - 32) * 5/9
        return f"{fahrenheit}°F is equal to {celsius:.2f}°C"
    else:
        return "Invalid temperature unit. Please use C or F."

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        unit_type = select_unit_type()
        value = enter_value(unit_type)
        
        if unit_type == 'length':
            result = convert_length(value)
        else:  # temperature
            result = convert_temperature(value)
        
        print(result)
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
