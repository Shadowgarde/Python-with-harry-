# name = str(input('Enter your name: '))
# num1  = int(input(f'{name} Enter your number 1: '))
# num2  = int(input(f'{name} Enter your number 2: '))
# num3  = int(input(f'{name} Enter your number 3: '))
# num4  = int(input(f'{name} Enter your number 4: '))

# if(num1 > num2):
#     print(num1)
# elif(num2 > num3):
#     print(num2)
# elif(num3 > num4):
#     print(num3)
# elif(num4 > num1):
#     print(num4)
# elif(num2 > num1):
#     print(num2)
# elif(num3 > num2):
#     print(num3)
# elif(num3 > num4):
#     print(num4)
# else:
#     print('Am i doing something wrong. lets check the video.')
#This is wrong code and i know i did something wrong let me check what i did wrong. So there are 2 methods that can be used
#I wil try using both codes. 

#Chatgpt method
name = str(input('Enter your name: '))
num1  = int(input(f'{name} Enter your number 1: '))
num2  = int(input('Enter your number 2: '))
num3  = int(input('Enter your number 3: '))
num4  = int(input('Enter your number 4: '))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(num2)
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(num3)
else:
    print(num4)

#My method