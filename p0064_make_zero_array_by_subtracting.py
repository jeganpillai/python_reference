# Question: Make Zero Array By Subtracting equal amounts

# English Video: 
# Tamil Video: 

# Approach 1: Brute Force Method with FOR Loop 
def Grow_With_Data(nums):
    if not nums or sum(nums) == 0:
        return 0
    # find the minimum positive non-zero element
    min_non_zero = float('inf')
    for num in nums:
        if num != 0:
            min_non_zero = min(min_non_zero,num)
    operations = 0
    while min_non_zero != 0:
        for i in range(len(nums)):
            if nums[i] > 0: 
                nums[i] = nums[i] - min_non_zero
        operations += 1
        min_non_zero = float('inf') if sum(nums) > 0 else 0
        for num in nums:
            if num != 0:
                min_non_zero = min(min_non_zero, num)

    return operations
assert Grow_With_Data([1,5,0,3,5]) == 3
assert Grow_With_Data([0]) == 0
print('Passed!')

# Approach 2: Simplified Brute Force Approach with List Comprehension 
def Grow_With_Data(nums):
    if not nums or sum(nums) == 0:
        return 0
    # find the minimum positive non-zero element
    min_non_zero = min([i for i in nums if i > 0])
    operations = 0
    while min_non_zero != 0:
        for i in range(len(nums)):
            if nums[i] > 0: 
                nums[i] = nums[i] - min_non_zero
        operations += 1
        min_non_zero = min([i for i in nums if i > 0]) if sum(nums) > 0 else 0
    return operations
assert Grow_With_Data([1,5,0,3,5]) == 3
assert Grow_With_Data([0]) == 0
print('Passed!')

# Approach 3: Set Operations for Efficient Solution 
def Grow_With_Data(nums):
    return len(set(nums) - {0})
assert Grow_With_Data([1,5,0,3,5]) == 3
assert Grow_With_Data([0]) == 0
print('Passed!')
