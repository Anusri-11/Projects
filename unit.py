import sys

def main_menu():
    print("\nUnit Converter")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    
    try:
        choice = int(input("Choose a category (1-4): "))
        if choice == 1:
            convert_length()
        elif choice == 2:
            convert_weight()
        elif choice == 3:
            convert_temperature()
        elif choice == 4:
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select from 1-4.")
            main_menu()
    except ValueError:
        print("Invalid input. Please enter a number from 1-4.")
        main_menu()

def convert_length():
    print("\nLength Converter")
    print("1. Kilometers to Miles")
    print("2. Meters to Feet")
    print("3. Back to Main Menu")

    try:
        choice = int(input("Choose a conversion (1-3): "))
        if choice == 1:
            kilometers = float(input("Enter value in kilometers: "))
            miles = kilometers * 0.621371
            print(f"{kilometers} km is equal to {miles:.2f} miles.")
        elif choice == 2:
            meters = float(input("Enter value in meters: "))
            feet = meters * 3.28084
            print(f"{meters} m is equal to {feet:.2f} feet.")
        elif choice == 3:
            main_menu()
        else:
            print("Invalid choice. Please select from 1-3.")
            convert_length()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        convert_length()

def convert_weight():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Grams to Ounces")
    print("3. Back to Main Menu")

    try:
        choice = int(input("Choose a conversion (1-3): "))
        if choice == 1:
            kilograms = float(input("Enter value in kilograms: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} kg is equal to {pounds:.2f} lbs.")
        elif choice == 2:
            grams = float(input("Enter value in grams: "))
            ounces = grams * 0.035274
            print(f"{grams} g is equal to {ounces:.2f} oz.")
        elif choice == 3:
            main_menu()
        else:
            print("Invalid choice. Please select from 1-3.")
            convert_weight()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        convert_weight()

def convert_temperature():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Kelvin")
    print("3. Back to Main Menu")

    try:
        choice = int(input("Choose a conversion (1-3): "))
        if choice == 1:
            celsius = float(input("Enter value in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} °C is equal to {fahrenheit:.2f} °F.")
        elif choice == 2:
            fahrenheit = float(input("Enter value in Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
            print(f"{fahrenheit} °F is equal to {kelvin:.2f} K.")
        elif choice == 3:
            main_menu()
        else:
            print("Invalid choice. Please select from 1-3.")
            convert_temperature()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        convert_temperature()

if __name__ == "__main__":
    main_menu()
