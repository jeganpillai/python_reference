# Question: find the max number of operations we can do with the same scores
# Video: https://www.youtube.com/watch?v=XW19oqrl9mk

# using FOR loop 
def Grow_With_Data(nums):
    chk = 0
    result = 0
    for i in range(0,len(nums),2):
        if i == 0:
            chk = sum(nums[i: i+2])
            result = 1
        elif sum(nums[i: i+2]) == chk and len(nums[i: i+2]) == 2:
                result += 1
        else:
            break
    return result
Grow_With_Data(nums)
assert Grow_With_Data([3,2,1,4,5]) == 2
assert Grow_With_Data([3,2,6,1,4]) == 1
assert Grow_With_Data([2,2,3,2,4,2,3,3,1,3]) == 1
print('Passed!')

# using FOR loop with short format 
def Grow_With_Data(nums):
    chk = nums[0] + nums[1]
    result = 1
    for i in range(2,len(nums),2):
        if sum(nums[i: i+2]) == chk and len(nums[i: i+2]) == 2:
                result += 1
        else:
            break
    return result
Grow_With_Data(nums)
assert Grow_With_Data([3,2,1,4,5]) == 2
assert Grow_With_Data([3,2,6,1,4]) == 1
assert Grow_With_Data([2,2,3,2,4,2,3,3,1,3]) == 1
print('Passed!')

# using WHILE loop 
def Grow_With_Data(nums):
    chk = nums[0] + nums[1]
    result = 1
    nums.pop(0)
    nums.pop(0)
    while len(nums) > 1:
        if nums[0] + nums[1] == chk:
            result += 1
        else:
            break
        nums.pop(0)
        nums.pop(0)
    return result
assert Grow_With_Data([3,2,1,4,5]) == 2
assert Grow_With_Data([3,2,6,1,4]) == 1
assert Grow_With_Data([2,2,3,2,4,2,3,3,1,3]) == 1
print('Passed!')
