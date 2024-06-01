# Question: check the number of elements which are not in correct sorting order

# English Video: 
# Tamil Video: 

# Approach 1: FOR loop
def Grow_With_Data(heights):
    sorted_heights  = sorted(heights)
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            cnt += 1
    return cnt
assert Grow_With_Data([1,1,4,2,1,3]) == 3 
assert Grow_With_Data([5,1,2,3,4]) == 5
assert Grow_With_Data([1,2,3,4,5]) == 0
print('Passed!!')

# Approach 2: Using zip() function 
def Grow_With_Data(heights):
    sorted_heights  = sorted(heights)
    cnt = 0
    for i in zip(heights, sorted_heights):
        if i[0] != i[1]:
            cnt += 1
    return cnt 
assert Grow_With_Data([1,1,4,2,1,3]) == 3 
assert Grow_With_Data([5,1,2,3,4]) == 5
assert Grow_With_Data([1,2,3,4,5]) == 0
print('Passed!!')

# Approach 3: List Comprehension 
def Grow_With_Data(heights):
    sorted_heights  = sorted(heights)
    return sum([heights[i] != sorted_heights[i] for i in range(len(heights))])
assert Grow_With_Data([1,1,4,2,1,3]) == 3 
assert Grow_With_Data([5,1,2,3,4]) == 5
assert Grow_With_Data([1,2,3,4,5]) == 0
print('Passed!!')
