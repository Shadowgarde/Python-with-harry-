#Create the table using function 
#Now here is the thing I think I should create a function then inside of fuction I creates a loop for the table
# After which I will call this fuction after taking the input from the user so that I can work on it faster
# This is my initial plan a  I am going to follow it.


def create_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {i * n}")
    return i

# Now I am gonna take the input from the user
num = int(input('Enter the number you want the table of: '))
# I am going to call the function 

create_table(num)



'''So here the summery in this programm i created the function 
with the loop to create the format of the table.'''