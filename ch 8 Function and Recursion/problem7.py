#def a function to remove the item from the list 
def rem(l, word):
    n =[]
    for item in l:
        if item != word:                          #The problem was that i put return inside the loop thats why it was showing only first item of the list
            
            n.append(item.strip(word))
    return n
        # l.remove(word)
        # return l

l = ['Shubham', 'Harsh', 'Rohan', 'Aryan', 'Karan']

print(rem(l, 'ar'))
