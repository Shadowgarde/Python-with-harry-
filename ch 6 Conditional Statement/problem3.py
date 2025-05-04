#I am making the basic spam filter
comment = input("Enter your comment: ")

p1 ="make a lot of money"
p2 ="buy now"
p3 ="subscribe this"
p4 ="click this"

if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
    print("This is a spam comment")
else:
    print("This is not a spam comment.")
