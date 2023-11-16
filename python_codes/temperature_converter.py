#15. WAP to receive temperature  in Celsius .Then Output Value in Fahrenheit[Formula : (0°C × 9/5) + 32 = 32°F ]

# Function to convert Celsius to Fahrenheit
def cel_to_fahr(celsius):
    return (celsius * 9/5) + 32

# Input: Receive temperature in Celsius from the user
celsius_temperature = float(input("Enter temperature in Celsius: "))

# Output: Convert and display the temperature in Fahrenheit
fahrenheit_temperature = cel_to_fahr(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
