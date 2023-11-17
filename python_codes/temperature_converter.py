#15. WAP to receive temperature  in Celsius Output in Fahrenheit (PyQ2019)
'''
Formula in BODMAS :
Celsius to Fahrenheit: (temp * 9/5) + 32
Fahrenheit to Celsius: (temp - 32) * 5/9
'''

def tempConvert(temp, scale):
    """
    Converts temperature between Celsius and Fahrenheit scales.

    Parameters:
    - temp: Temperature value to be converted.
    - scale: The scale of the temperature, 'C' for Celsius, 'F' for Fahrenheit.

    Returns:
    - Converted temperature value.
    """
    if scale == 'C':
        convertedTemp = (temp - 32) * 5 / 9
        convertedTempName = "Fahrenheit"
        return convertedTemp, convertedTempName
    elif scale == 'F':
        convertedTemp = (temp * 9 / 5) + 32
        convertedTempName = "Celsius"
        return convertedTemp, convertedTempName
    else:
        print("Invalid scale")
        return None, None
# Prompt the user for a temperature
temp = float(input("Enter a temperature: "))
# Prompt the user for the scale
scale = input("Enter the scale (C or F): ")
# Convert the temperature using the tempConvert function
convertedTemp, convertedTempName = tempConvert(temp, scale)
# Check if there is a valid conversion
if convertedTemp is not None:
    # Print the converted temperature and its name
    print("Converted temperature: ", convertedTemp, "in", convertedTempName)
else:
    print("Invalid scale")
