#In this program we will try to find out the grade of the student based on the marks scored by him/her.

name = str(input('Enter your name: '))
marks = int(input('Enter your marks: '))
#Here we are taking the input from the user and storing it in the variables.

if marks == 100 or marks >= 90:
    print(name, 'Your grade is EX')
elif marks < 90 and marks >= 80:
    print(name, 'Your grade is A')
elif marks < 80 and marks >= 70:
    print(name, 'Your grade is B')
elif marks < 70 and marks >= 60:
    print(name, 'Your grade is C')
elif marks < 60 and marks >= 50:
    print(name, 'Your grade is D')
else:
    print(name, 'Your grade is F')

