post = input('Enter your post here: ')
find_name = input('Enter the name you are searching for: ')
if find_name.lower() in post.lower():
    print('Harry is mentioned in the post')
else:
    print('Harry is not mentioned in the post')