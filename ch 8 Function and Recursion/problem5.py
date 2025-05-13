#program to print * in descending orders
star = int(input('Enter the number the of stars: ')) #Mistake to make is that i put string insted of int while taking input.

def print_star(n):
    if (n == 0):
        return
    print('*' * n)
    print_star(n - 1)
print_star(star) #Since it was already printing thats why it shows traceback call fails
