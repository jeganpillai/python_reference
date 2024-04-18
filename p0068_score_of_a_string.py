# Question: Find the Score of a String

# English Video: 
# Tamil Video: 

# Approach 1: Using enumerate function 
def Grow_With_Data(s):
    result = 0
    for indx, val in enumerate(s[:-1]):
        result += abs(ord(val) - ord(s[indx + 1]))
    return result
assert Grow_With_Data('hello') == 13
assert Grow_With_Data('zaz') == 50
print('Passed!')

# Approach 2: Using range() function
def Grow_With_Data(s):
    result = 0
    for indx in range(len(s)-1):
        result += abs(ord(s[indx]) - ord(s[indx + 1]))
    return result
assert Grow_With_Data('hello') == 13
assert Grow_With_Data('zaz') == 50
print('Passed!')
