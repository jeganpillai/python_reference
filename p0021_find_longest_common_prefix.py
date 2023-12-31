# Question: find the Longest Common Prefix string amongst an array of strings
# Video: https://www.youtube.com/watch?v=XseKX9VPJvw

-- Approach 1: Character-by-Character Comparison
def Grow_With_Data(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]

    min_length = min(len(s) for s in strs)
    min_length

    result = ''

    for i in range(min_length):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            result += char
        else:
            break
    return result
assert Grow_With_Data(["flower", "flow", "flight"]) == 'fl'
assert Grow_With_Data(["dog", "racecar", "car"]) == '' 
assert Grow_With_Data([]) == ''
assert Grow_With_Data(['a']) == 'a'
assert Grow_With_Data(['aca','cba']) == ''
print('\n Pass')

# Approach 2: Iterative Comparison with Sorting
def Grow_With_Data(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]

    strs = sorted(strs, key = len)
    result = ''
    
    for indx, val in enumerate(strs[0]):
        for sindx, sval in enumerate(strs[1:]):
            match = True 
            if val != sval[indx]:
                match = False 
                break
        if match:
            result += val
        else:
            break
    return result
assert Grow_With_Data(["flower", "flow", "flight"]) == 'fl'
assert Grow_With_Data(["dog", "racecar", "car"]) == '' 
assert Grow_With_Data([]) == ''
assert Grow_With_Data(['a']) == 'a'
assert Grow_With_Data(['aca','cba']) == ''
print('\n Pass')
  
-- Approach 3: End-to-End Comparison After Sorting
def Grow_With_Data(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]

    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1 
    return first[:i]
assert Grow_With_Data(["flower", "flow", "flight"]) == 'fl'
assert Grow_With_Data(["dog", "racecar", "car"]) == '' 
assert Grow_With_Data([]) == ''
assert Grow_With_Data(['a']) == 'a'
assert Grow_With_Data(['aca','cba']) == ''
print('\n Pass')
