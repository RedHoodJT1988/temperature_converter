# convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# convert celsius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# convert fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

# convert kelvin to celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# convert kelvin to fahrenheit
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    except ValueError:
        return {"error": "Invalid temperature value. Please enter a number"}
    if unit == "celsius":
        return {
            "Fahrenheit": f'{celsius_to_fahrenheit(value):.2f} F',
            "Kelvin": f"{celsius_to_kelvin(value):.2f} K"
        }
    elif unit == "fahrenheit":
        return {
            "Celsius": f"{fahrenheit_to_celsius(value):.2f} C",
            "Kelvin": f"{fahrenheit_to_kelvin(value):.2f} K"
        }
    elif unit == "kelvin":
        return {
            "Celsius": f"{kelvin_to_celsius(value):.2f} C",
            "Fahrenheit": f"{kelvin_to_fahrenheit(value):.2f} F"
        }
    else:
        return {"error": "Invalid unit. Supported unites: Celsius, Fahrenheit, Kelvin"}

result = convert_temperature()
print("Result: ", result)
