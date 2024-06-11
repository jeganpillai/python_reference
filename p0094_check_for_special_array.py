# Question: Check for Special Array

# English Video: 
# Tamil Video: 

# Approach 1: Brute Force Method 
def Grow_With_Data(nums):
    if len(nums) == 1:
        return True
    for i in range(len(nums) - 1):
        cnt = 0
        if nums[i]%2 == 0:
            cnt += 1
        if nums[i+1]%2 == 0:
            cnt += 1
        print(cnt)
        if cnt == 0 or cnt == 2:
            return False
    return True
assert Grow_With_Data([1]) == True
assert Grow_With_Data([2,1,4]) == True
assert Grow_With_Data([4,3,1,6]) == False
print('Passed!!')

# Approach 2: Simplified version 
def Grow_With_Data(nums):
    if len(nums) == 1:
        return True
    for i in range(len(nums) - 1):
        if nums[i]%2 == nums[i+1]%2:
            return False
    return True
assert Grow_With_Data([1]) == True
assert Grow_With_Data([2,1,4]) == True
assert Grow_With_Data([4,3,1,6]) == False
print('Passed!!')
