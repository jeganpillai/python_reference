# Question: Find the peak elements in an array
# Video: https://www.youtube.com/watch?v=feRw_AizC2M

# Approach 1: Using RANGE() function 
def Grow_With_Data(mountain):
    result = []
    n = len(mountain)
    for i in range(1, n-1):
        if mountain[i] > mountain[i+1] and mountain[i] > mountain[i-1]:
            result.append(i)
    return result
assert Grow_With_Data([1,4,3,8,5]) == [1,3]
assert Grow_With_Data([2,4,4]) == []
print('Passed!')

# Approach 2: Using ENUMERATE() function 
def Grow_With_Data(mountain):
    result = []
    n = len(mountain)
    for indx, val in enumerate(mountain):
        if indx == 0 or indx == n-1:
            continue
        if val > mountain[indx+1] and val > mountain[indx-1]:
            result.append(indx)
    return result
assert Grow_With_Data([1,4,3,8,5]) == [1,3]
assert Grow_With_Data([2,4,4]) == []
print('Passed!')

# Approach 3: Single line of code 
def Grow_With_Data(mountain):
    return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] and mountain[i] > mountain[i + 1]]
assert Grow_With_Data([1,4,3,8,5]) == [1,3]
assert Grow_With_Data([2,4,4]) == []
print('Passed!')

# Using ZIP() and ENUMERATE() functions 
def Grow_With_Data(mountain):
    result = []
    for indx, (a,b,c) in enumerate(zip(mountain, mountain[1:], mountain[2:])):
        if a < b > c:
            result.append(indx + 1)
    return result
assert Grow_With_Data([1,4,3,8,5]) == [1,3]
assert Grow_With_Data([2,4,4]) == []
print('Passed!')
