#!/usr/bin/env python3
"""
Temperature Conversion Tool: Celsius <-> Fahrenheit
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """Main function to handle user input and conversion"""
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit == "c":
        result = convert_to_fahrenheit(temp)
        print("{:.2f}°C is {:.2f}°F".format(temp, result))
    elif unit == "f":
        result = convert_to_celsius(temp)
        print("{:.2f}°F is {:.2f}°C".format(temp, result))
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()