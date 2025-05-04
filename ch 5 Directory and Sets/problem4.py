s = set() 
s.add(20) 
s.add(20.0) #since this is float value it will merge with integer 
s.add('20') 

print(len(s))