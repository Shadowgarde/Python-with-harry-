#I have the given template in which I have to fill the detail 
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>                
'''# orginal string abhi bhi same h, kyuki wo immutable h and usko change nhi kiya ja skta h isliye isne usko hi change kiya h 

print(letter.replace('<|Name|>', 'Shubham').replace('<|Date|>', '4 May 2025'))