#Taking inputs
t = float(input('Enter the temperature only in °C: '))

#Creation function for the conversion 
def convert_to_fahrenheit():
    return (t *(9 / 5)) + 32

#Calling the function and printing it 
print(f'The temperature after the conversion is {convert_to_fahrenheit()}°F')