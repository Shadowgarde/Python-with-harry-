name = str(input("Enter the user name: "))
# Now I want to put the student marks of 3 subjects here 
marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))


#Now i will check on the user individual percentage 
individual_percentage_of_marks1 = (100*marks1)/100
individual_percentage_of_marks2 = (100*marks2)/100
individual_percentage_of_marks3 = (100*marks3)/100

if individual_percentage_of_marks1 >= 33:
    print("You have passed in subject 1")
if individual_percentage_of_marks2 >= 33:
    print("You have passed in subject 2")
if individual_percentage_of_marks3 >= 33:
    print("You have passed in subject 3")


#I will check the total percentage of the user.
total_percentage = (100*(marks1 + marks2 + marks3))/300

if total_percentage >= 40:
    print("You are passed in total percentage.")
else: 
    print('You have failed, try again next year')


print(f'Congratulations {name}, You have been promoted to the next class.')

#There is one more way to do it 
#We can use the if-elif-else statement to check the percentage of the user.
#Here is the code for it
# I could go for the condition like this 
# if total_percentage >= 40 and individual_percentage_of_marks1 >=33 and individual_percentage_of_marks2 >=33 and individual_percentage_of_marks3 >= 33:
#     print('You are passed in total percentage and all subjects')