# Question: Partition the string into one or more substrings in optimal way

# Approach 1: Iterative Approach with Unique Character Tracking
def Grow_With_Data(s):
    chk = set()
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] not in chk:
            chk.add(s[i])
            continue
        count += 1
        chk = set(s[i])
    return count 
assert Grow_With_Data('abacaba') == 4
assert Grow_With_Data('ssssss') == 6
print('Passed!')

# Approach 2: Iterative Approach with Direct Substring Counting
def Grow_With_Data(s):
    chk = set()
    count = 1
    for i in s:
        if i in chk:
            count += 1
            chk.clear()
        chk.add(i)
    return count 
assert Grow_With_Data('abacaba') == 4
assert Grow_With_Data('ssssss') == 6
print('Passed!')
