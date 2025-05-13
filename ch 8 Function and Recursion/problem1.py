#Taking Inputs
n1 = int(input('Enter the number: '))
n2 = int(input('Enter the number: '))
n3 = int(input('Enter the number: '))

#Creating function 
def greatest(n1, n2, n3):
    # if n1 > n2 and n1 > n3:
    #     return n1
    # elif n2 > n1 and n2 > n3:
    #     return n2
    # elif n3 > n1 and n3 > n2:
    #     return n3
    # elif n1 == n2 and n1 == n3:
    #     return 'All numbers are equal.'

    if n1 == n2 == n3:
        return 'All numbers are equal.'
    greatest_num = max(n1, n2, n3)
    return f'The greatest number is {greatest_num}.'


print(greatest(n1, n2, n3))