'''
  *
 ***
*****
'''

n = int(input('Enter the number of stars needed: '))

stars = '*'
spaces = ' '

for i in range(1, n + 1):
    print(spaces * (n - i), end='')     #it is used for printing spaces before stars
    print(stars * (2 * i - 1), end= '')  #for odd number of stars so thats why 2*i-1
    print('')