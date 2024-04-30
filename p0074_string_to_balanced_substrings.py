# Question: Split a balanced string into balanced substrings

# Approach 1: Track L and R separatly 
def Grow_With_Data(s):
    l, r = 0, 0
    count = 0
    for c in s:
        if c == 'R': r += 1
        if c == 'L': l += 1
        if l == r: count += 1
    return count
Grow_With_Data(s)
assert Grow_With_Data('RLRRLLRLRL') == 4
assert Grow_With_Data('RLRRRLLRLL') == 2
assert Grow_With_Data('LLLLRRRR') == 1
print('Passed!')

# Approach 2: Track L and R using single variable 
def Grow_With_Data(s):
    balance = 0
    count = 0
    for c in s:
        if c == 'R': balance += 1
        if c == 'L': balance -= 1
        if balance == 0: count += 1
    return count
Grow_With_Data(s)
assert Grow_With_Data('RLRRLLRLRL') == 4
assert Grow_With_Data('RLRRRLLRLL') == 2
assert Grow_With_Data('LLLLRRRR') == 1
print('Passed!')

# Approach 3: Simplified version 
def Grow_With_Data(s):
    balance = 0
    count = 0
    for c in s:
        # balance = balance +1 if c == 'R' else balance -1
        balance += 1 if c == 'R' else -1
        if balance == 0: count += 1
    return count
Grow_With_Data(s)
assert Grow_With_Data('RLRRLLRLRL') == 4
assert Grow_With_Data('RLRRRLLRLL') == 2
assert Grow_With_Data('LLLLRRRR') == 1
print('Passed!')
