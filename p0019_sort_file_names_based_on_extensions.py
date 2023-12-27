# Question: Sort file names based on their extensions
# video: https://www.youtube.com/watch?v=PT3CaXPRByY

# 1. list of letters with Caps and Small letter
letter = ['a','A','g','h','f','R']
sorted(letter)

# 2. within smaller letters, how its sorted? 
files = ['an','apple','a','day']
sorted(files)

# 3. How to change the sorting to Decending? 
files = ['an','apple','a','day']
sorted(files, reverse=True)

# 4. How to sort based on the length of the element? 
files = ['an','apple','a','day']
sorted(files, reverse=True, key = len)

# we can do it in different format 
files = ['an','apple','a','day']
sorted(files, reverse=True, key = lambda x: len(x))

# 5. How to sort based on the last character? 
files = ['an','apple','a','day']
sorted(files, reverse=True, key = lambda x: x[-1])

# 6. How to get the file extension alone?
a = 'dog_pictures.zip'
a.split('.')[-1] 

#7. Now, using all these tips, how to sort the file name based on the extension? 
files = ['dog_pictures.zip', 'cat_pictures.zip', 'fluffy.jpg', 'meow.mp3', 'ascii_cat.txt']
sorted(files, key = lambda x: x.split('.')[1])

# 8. If you see this zip file, we have two files. How to sort it based on the file extension and then the file name? 
files = ['dog_pictures.zip', 'cat_pictures.zip', 'fluffy.jpg', 'meow.mp3', 'ascii_cat.txt']
sorted(files, key = lambda x: [x.split('.')[-1],x])
