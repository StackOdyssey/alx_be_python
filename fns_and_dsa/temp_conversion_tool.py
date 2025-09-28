#!/usr/bin/env python3
"""
Temperature Converter: Celsius <-> Fahrenheit
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_temperature():
    """Prompt user for temperature input and validate"""
    try:
        return float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def get_unit():
    """Prompt user for temperature unit and validate"""
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    if unit in ("c", "f"):
        return unit
    print("Invalid unit. Please enter 'C' or 'F'.")
    return None


def main():
    """Main function to run the converter"""
    temp = get_temperature()
    if temp is None:
        return

    unit = get_unit()
    if unit is None:
        return

    if unit == "c":
        result = convert_to_fahrenheit(temp)
        print(f"{temp:.2f}°C is {result:.2f}°F")
    else:
        result = convert_to_celsius(temp)
        print(f"{temp:.2f}°F is {result:.2f}°C")


if __name__ == "__main__":
    main()