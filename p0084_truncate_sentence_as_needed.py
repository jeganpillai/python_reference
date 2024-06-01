# Question: Truncate Sentence as Needed

# English Video: https://www.youtube.com/watch?v=gZ88hXMu7IM
# Tamil Video: https://www.youtube.com/watch?v=jQWex4Ad7T0

# Approach 1: Brute Force Method 
def Grow_with_data(s, k):
    s = s.split()
    result = []
    for i in range(len(s)):
        if i < k:
            result.append(s[i])
    return ' '.join(result)

assert Grow_with_data('Hello how are you Contestant', 4) == 'Hello how are you'
assert Grow_with_data('What is the solution to this problem', 4) == 'What is the solution'
assert Grow_with_data('chopper is not a tanuki', 5) == 'chopper is not a tanuki'
print('Passed!')

# Approach 2: Using enumerate and truncate 
def Grow_with_data(s, k):
    result = []
    for indx, val in enumerate(s.split()):
        if indx < k:
            result.append(val)
    return ' '.join(result)
assert Grow_with_data('Hello how are you Contestant', 4) == 'Hello how are you'
assert Grow_with_data('What is the solution to this problem', 4) == 'What is the solution'
assert Grow_with_data('chopper is not a tanuki', 5) == 'chopper is not a tanuki'
print('Passed!')

# Approach 3: Simple split, slice and join
def Grow_with_data(s, k):
    return ' '.join(s.split()[:k])

assert Grow_with_data('Hello how are you Contestant', 4) == 'Hello how are you'
assert Grow_with_data('What is the solution to this problem', 4) == 'What is the solution'
assert Grow_with_data('chopper is not a tanuki', 5) == 'chopper is not a tanuki'
print('Passed!')
