# Question: Find the index of the Words Containing specific Characters

# English Video: 
# Tamil Video: 

# Approach 1: Using range() function 
def Grow_With_Data(words, x):
    result = []
    for i in range(len(words)):
        if x in words[i]:
            result.append(i)
    return result
assert Grow_With_Data(['grow','with','data'], 't') == [1,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'a') == [0,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'z') == []
print('Passed!')

# Approach 2: List comprehension using range() function
def Grow_With_Data(words, x):
    result = [i for i in range(len(words)) if x in words[i]]
    return result
assert Grow_With_Data(['grow','with','data'], 't') == [1,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'a') == [0,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'z') == []
print('Passed!')

# Approach 3: Using Eneumerate function
def Grow_With_Data(words, x):
    result = []
    for i, val in enumerate(words):
        if x in val:
            result.append(i)
    return result
assert Grow_With_Data(['grow','with','data'], 't') == [1,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'a') == [0,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'z') == []
print('Passed!')

# Approach 4: List comprehension using enuemarate function
def Grow_With_Data(words, x):
    result = [i for i, val in enumerate(words) if x in val]
    return result
assert Grow_With_Data(['grow','with','data'], 't') == [1,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'a') == [0,2]
assert Grow_With_Data(["abc","bcd","aaaa","cbc"], 'z') == []
print('Passed!')
