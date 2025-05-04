user = str(input('Enter your name: '))
age = int(input('Enter your age: '))

#this statement is called if elif ladder.

if(age >=18):
    print(f'Congratulations {user}, you are above the age of consent.')
    print('Good for you')
elif(age<0):
    print(f'{user}, Please provide the correct age you can not put negative age.')
    print('Run program again.')
elif(age == 0):
    print('You can not enter the invalid age.')
else:
    print('You are underage so you can not proceed further in this program.')

print('End of the program')