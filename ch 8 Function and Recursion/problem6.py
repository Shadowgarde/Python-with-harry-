#To convert inches into centimeter
# The formula is n * 2.54
# where n is the number of inches
def inches_to_cm(inch):        #This is function and it has one parameter 
    return inch * 2.54     #I am returning the result of this calculation by taking the input from the user 

num = float(input('Enter the value in inches: '))

print(f'The value in centimeters is {inches_to_cm(num)}')