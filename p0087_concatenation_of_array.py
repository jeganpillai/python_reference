# Question: Concatenation of Array

# English Video: 
# Tamil Video: 

# Approach 1a: Basic FOR Loop 
def Grow_With_Data(nums):
    result = []
    for i in nums:
        result.append(i)
    for i in nums:
        result.append(i)
    return result
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 1b: Using WHILE Loop 
def Grow_With_Data(nums):
    result = []
    lup = 2
    while lup > 0:
        print('Here')
        for i in nums:
            result.append(i)
        lup -= 1
    return result
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 1c: Simplified APPEND Logic 
def Grow_With_Data(nums):
    result = nums[:]
    for i in nums:
        result.append(i)
    return result
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 2: Overwrite Zero Array 
def Grow_With_Data(nums):
    n = len(nums)
    result = [0] * (2 * n)
    for i in range(n):
        result[i] = nums[i]
        result[i+n] = nums[i]
    return result
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 3: Using Extend Function 
def Grow_With_Data(nums):
    nums.extend(nums)
    return nums
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 4: Basic Arithmetic 
def Grow_With_Data(nums):
    return nums + nums
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')

# Approach 5: Multiply the Array 
def Grow_With_Data(nums):
    return nums * 2
assert Grow_With_Data([1,2,1]) == [1,2,1,1,2,1]
assert Grow_With_Data([1,3,2,1]) == [1,3,2,1,1,3,2,1]
print('Passed!')
