# Question: Given a array of words, convert all the elements to its lower case 
# video: https://www.youtube.com/watch?v=ytX0DecMdmU

# Approach 1: Using FOR loop 
def Grow_With_Data(s):
    result = []
    for i in s:
        result.append(i.lower())
    return result 
assert Grow_With_Data(s) == ['hello', 'world', 'python', 'day']

# Approach 2: List Comprehension 
def Grow_With_Data(s):
    result = [i.lower() for i in s]
    return result 
assert Grow_With_Data(s) == ['hello', 'world', 'python', 'day']

# Approach 3: Without Loop option and use JOIN() function 
def Grow_With_Data(s):
    result = ','.join(s).lower().split(',')
    return result 
assert Grow_With_Data(s) == ['hello', 'world', 'python', 'day']
