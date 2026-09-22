def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit = float(input("Enter Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print("Celsius:", celsius)