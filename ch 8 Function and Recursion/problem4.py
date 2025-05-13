#It takes the the n number required by the user
n = int(input('Enter the numbers you want sum of: '))

def sum_of_natural_numbers(n):
    #It takes the n number required by the user and returns the sum of the numbers from
    #1 to n using the formula n*(n+1)/2
    return n*(n + 1)/2
#It calls the function and prints the results
print(f'The toltal sum is {sum_of_natural_numbers(n)}')


#Harry solution 
# def sum(n):
#     if(n == 1):   #It is base condition 
#         return 1
#     return sum(n -1) + n
# print(sum(4))

