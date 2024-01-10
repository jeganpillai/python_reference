# Question: Find the index of the first occurance of needle in haystack
# Video: https://www.youtube.com/watch?v=j7mxQp8EiBc

# approach 1: General Looping Logic
def Grow_With_Data(haystack, needle):
    if needle: 
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 
    else:
        return 0
assert Grow_With_Data('hello','ll') == 2 
assert Grow_With_Data('hello','') == 0 
assert Grow_With_Data('hello','a') == -1
print('\n Pass')

# approach 2: index() 
def Grow_With_Data(haystack, needle):
    try: 
        return haystack.index(needle)
    except Exception: #  ValueError: 
        return -1

# approach 3: find()
def Grow_With_Data(haystack, needle):
    return haystack.find(needle) 
