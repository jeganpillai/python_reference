# Question: XOR of Numbers Appear Twice

# English Video: 
# Tamil Video: 

# Approach 1: Using FOR loop 
def Grow_With_Data(nums):
    chk = set()
    result = 0
    for num in nums:
        if num not in chk:
            chk.add(num)
        else:
            result ^= num
    return result 
assert Grow_With_Data([1,2,1,3]) == 1
assert Grow_With_Data([1,2,3]) == 0
assert Grow_With_Data([1,2,2,1]) == 3
print('Passed!!')

# Appraoch 2: Using Dictionary
def Grow_With_Data(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    lst = [key for key, val in d.items() if val == 2]
    
    xor_result = 0
    for i in lst:
        xor_result ^= i
    return xor_result

appraassert Grow_With_Data([1,2,1,3]) == 1
assert Grow_With_Data([1,2,3]) == 0
assert Grow_With_Data([1,2,2,1]) == 3
print('Passed!!')
