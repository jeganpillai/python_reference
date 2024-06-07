# Question: Permutation Difference Between Two Strings

# English Video: 
# Tamil Video: 

# Approach 1: Simple Looping logic 
def Grow_With_Data(s,t):
    d = {}
    for indx, val in enumerate(s):
        d[val] = indx
    result = 0
    for indx, val in enumerate(t):
        result += abs(indx - d[val])
    return result
assert Grow_With_Data('abcde','edbac') == 12
assert Grow_With_Data('abc','bac') == 2
print('Passed!!')

# Approach 2: Simplified code using List Comprehension 
def Grow_With_Data(s,t):
    d = {val:indx for indx, val in enumerate(s)}
    return sum([abs(indx - d[val]) for indx, val in enumerate(t)])
    
assert Grow_With_Data('abcde','edbac') == 12
assert Grow_With_Data('abc','bac') == 2
print('Passed!!')

# Approach 3: Using Index function 
def Grow_With_Data(s, t):
    result = 0 
    for indx, val in enumerate(s):
        result += abs(indx - t.index(val))
    return result 

assert Grow_With_Data('abcde','edbac') == 12
assert Grow_With_Data('abc','bac') == 2
print('Passed!!')
