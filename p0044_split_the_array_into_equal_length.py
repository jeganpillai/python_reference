# Question: split the given array into two arrays of equal length with distinct elements in it.
# Video: https://www.youtube.com/watch?v=ndS0Zcd_2-o

# Scenario 1: If input array is even length 
def Grow_With_Data(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1 
    # set1 = [key for key, val in d.items() if val == 2]
    set2 = [key for key, val in d.items() if val > 2]
    # set3 = [key for key, val in d.items() if val == 1]
    return not set2
assert Grow_With_Data([1,1,2,2,3,4]) == True
assert Grow_With_Data([1,1,1,1]) == False
assert Grow_With_Data([4,4,9,10]) == True 
assert Grow_With_Data([6,1,3,1,1,8,9,2]) == False 
assert Grow_With_Data([6,4,2,3,7,10,7,1]) == True 
print('Passed!')

# Scenario 2: If inoput array is of odd length also
def Grow_With_Data(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1 
    # set1 = [key for key, val in d.items() if val == 2]
    set2 = [key for key, val in d.items() if val > 2]
    set3 = [key for key, val in d.items() if val == 1]
    return not set2 and len(set3)%2 == 0
assert Grow_With_Data([1,1,2,2,3,4]) == True
assert Grow_With_Data([1,1,1,1]) == False
assert Grow_With_Data([4,4,9,10]) == True 
assert Grow_With_Data([6,1,3,1,1,8,9,2]) == False 
assert Grow_With_Data([6,4,2,3,7,10,7,1]) == True 
assert Grow_With_Data([1,1,2,2,3,4,5]) == False 
print('Passed!')
