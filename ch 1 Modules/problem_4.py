import os  

# Specify the directory path  
directory_path = '/D:'  # Current directory, change as needed  

# List the contents of the directory  
contents = os.listdir(directory_path)  

# Print the contents  
for item in contents:  
    print(item)  