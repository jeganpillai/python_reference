# Question: Given two strings, merge the strings by adding letters in alternating order

# English Video: https://www.youtube.com/watch?v=hWJTElXQ4Fw
# Tamil Video: https://www.youtube.com/watch?v=QCtFibRPfY8

# Approach 1: Basic FOR loop 
def Grow_With_Data(word1, word2):
    min_length = min(len(word1), len(word2))
    max_length = max(len(word1), len(word2))
    result = ''
    for i in range(min_length):
        result += word1[i]
        result += word2[i]
    if max_length != min_length:
        result += word1[min_length:] if len(word1) == max_length else word2[min_length:]
    return result
assert Grow_With_Data('abc','pqr') == 'apbqcr'
assert Grow_With_Data('ab','pqrs') == 'apbqrs'
assert Grow_With_Data('abcd','pq') == 'apbqcd'
print('Passed!')

# Approach 2: Simplify the code 
def Grow_With_Data(word1, word2):
    max_length = max(len(word1), len(word2))
    result = ''
    for i in range(max_length):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    return result
assert Grow_With_Data('abc','pqr') == 'apbqcr'
assert Grow_With_Data('ab','pqrs') == 'apbqrs'
assert Grow_With_Data('abcd','pq') == 'apbqcd'
print('Passed!')

# Approach 3: Lets see how we can use a WHILE loop here 
def Grow_With_Data(word1, word2):
    max_length = max(len(word1), len(word2))
    result = ''
    i = 0
    while i < max_length:
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
        i += 1 
    return result
assert Grow_With_Data('abc','pqr') == 'apbqcr'
assert Grow_With_Data('ab','pqrs') == 'apbqrs'
assert Grow_With_Data('abcd','pq') == 'apbqcd'
print('Passed!')

# Approach 4: Simplify the WHILE loop
def Grow_With_Data(word1, word2):
    max_length = max(len(word1), len(word2))
    result = ''
    i = 0
    while i < len(word1) and i < len(word2):
        result += word1[i]+word2[i]
        i += 1 
    result += word1[i:]+word2[i:]
    return result
assert Grow_With_Data('abc','pqr') == 'apbqcr'
assert Grow_With_Data('ab','pqrs') == 'apbqrs'
assert Grow_With_Data('abcd','pq') == 'apbqcd'
print('Passed!')
