# Question: Remove Duplicates from Sorted Array

# English Video: https://www.youtube.com/watch?v=yszE93DYefQ
# Tamil Video: https://www.youtube.com/watch?v=YQhWfLrN5Ig

# Approach 1: In-place approach with additional set() data type
def Grow_With_Data(nums):
    if not nums:
        return 0
    chk = set()
    result = 0
    for num in nums:
        if num not in chk:
            chk.add(num)
            nums[result] = num
            result += 1
    return result
assert Grow_With_Data([1,1,2]) == 2
assert Grow_With_Data([0,0,1,1,1,2,2,3,3,4]) == 5
print('Passed!')

# Approach 2: In-place with no additional array stored
def Grow_With_Data(nums):
    if not nums:
        return 0
    result = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[result]:
            result += 1
            nums[result] = nums[j]
    return result + 1
assert Grow_With_Data([1,1,2]) == 2
assert Grow_With_Data([0,0,1,1,1,2,2,3,3,4]) == 5
print('Passed!')
