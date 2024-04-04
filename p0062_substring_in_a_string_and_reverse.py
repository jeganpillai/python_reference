# Question: Find the existence of a substring in a string and its reverse

# English Video: 
# Tamil Video: 

# Approach 1: Matching Substrings 
def Grow_With_Data(s):
    rev_s = ''.join(reversed(s))
    result = []
    for i in range(len(s)-1):
        if s[i:i+2] in rev_s:
            print(s[i:i+2])
            result.append(s[i:i+2])
    return True if result else False
assert Grow_With_Data('zeebra') == True
assert Grow_With_Data('abcba') == True
assert Grow_With_Data('abcd') == False
print('Passed!')

# Approach 2: First Occurrence Search
def Grow_With_Data(s):
    rev_s = ''.join(reversed(s))
    result = []
    for i in range(len(s)-1):
        if s[i:i+2] in rev_s:
            return True
    return False
assert Grow_With_Data('zeebra') == True
assert Grow_With_Data('abcba') == True
assert Grow_With_Data('abcd') == False
print('Passed!')

# Approach 3: Real-time Comparison 
def Grow_With_Data(s):
    mapping = set()
    for i in range(len(s)-1):
        if s[i] == s[i+1] or s[i+1] + s[i] in mapping:
            return True
        mapping.add(s[i:i+2])
    return False
assert Grow_With_Data('zeebra') == True
assert Grow_With_Data('abcba') == True
assert Grow_With_Data('abcd') == False
print('Passed!')

