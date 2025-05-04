#Program to find weather the name exist on the list or not.

l = ['Harry', 'Shubham', 'Sachin', 'Rahul', 'Rohan']
name = str(input('Enter your name: '))

if name in l:
    print('Your name exist in the list.')
else:
    print('Your name does not exist in the list.')