marks = []

f1 = int(input('Enter the Marks here: '))
marks.append(f1)
f2 = int(input('Enter the Marks here: '))
marks.append(f2)
f3 = int(input('Enter the Marks here: '))   #Types matters in case you want sort it out str me sort nhi karege isliye hum int data type ka use krte h 
marks.append(f3)
f4 = int(input('Enter the Marks here: '))
marks.append(f4)
f5 = int(input('Enter the Marks here: '))
marks.append(f5)
f6 = int(input('Enter the Marks here: '))
marks.append(f6)


marks.sort()

print(marks)