# Question: Better Compression of String

# English Video: 
# Tamil Video: 

# Approach 1: Basic looping logic 
def Grow_With_Data(compressed):
    d = {}
    for indx, val in enumerate(compressed):
        if val.isdigit():
            # print(val, compressed[indx-1])
            d[compressed[indx-1]] = d.get(compressed[indx-1],0) + int(val)
    result = ''
    for val in sorted(d.keys()):
        # print(val, d[val])
        result += val + str(d[val])
    return result
Grow_With_Data(compressed)
assert Grow_With_Data('a3c9b2c1') == 'a3b2c10'
assert Grow_With_Data('c2b3a1') == 'a1b3c2'
assert Grow_With_Data('a2b4c1') == 'a2b4c1'
print('Passed!!')

# Approach 2: Using WHILE loop 
def Grow_With_Data(compressed):
    frequency = {}
    n = len(compressed)
    i = 0
    while i < n:
        char = compressed[i]
        freq = 0
        i += 1
        while i < n and compressed[i].isdigit():
            freq = freq * 10 + int(compressed[i])
            i += 1
            # print(freq)
        
        frequency[char] = frequency.get(char,0) + freq
    # print(frequency)
    return ''.join([f'{char}{frequency[char]}' for char in sorted(frequency)])
assert Grow_With_Data('a3c9b2c1') == 'a3b2c10'
assert Grow_With_Data('c2b3a1') == 'a1b3c2'
assert Grow_With_Data('a2b4c1') == 'a2b4c1'
assert Grow_With_Data('i10g6u6') == 'g6i10u6'
print('Passed!!')

# Approach 3: Using Regular Expression
import re
def Grow_With_Data(compressed):
    check = re.findall(r'([a-z])(\d+)', compressed)
    frequency = {}
    for v in check:
        # print(v[0], v[1])
        frequency[v[0]] = frequency.get(v[0],0) + int(v[1])
    frequency
    return ''.join([f'{char}{frequency[char]}' for char in sorted(frequency.keys())])
assert Grow_With_Data('a3c9b2c1') == 'a3b2c10'
assert Grow_With_Data('c2b3a1') == 'a1b3c2'
assert Grow_With_Data('a2b4c1') == 'a2b4c1'
assert Grow_With_Data('i10g6u6') == 'g6i10u6'
print('Passed!!')
