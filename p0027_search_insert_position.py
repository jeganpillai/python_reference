# Question: find the insert position of the target in the given array
# Video: https://www.youtube.com/watch?v=Qcgu4iKYBGI

# 1. Brute Force Method
def Grow_With_Data(nums, target):
    pos = 0
    for indx, val in enumerate(nums):
        if val == target:
            return indx
        elif indx == len(nums) - 1 and val < target:
            return indx+1
        elif val < target:
            pos += 1 
        else:
            pass 
    return pos
assert Grow_With_Data([1,3,5,6], 5) == 2
assert Grow_With_Data([1,3,5,6], 2) == 1
assert Grow_With_Data([1,3,5,6], 7) == 4
assert Grow_With_Data([1,3,5,6], 0) == 0
print('\n Pass')

# 2. Effective Index Finder
def Grow_With_Data(nums, target):
    if target in nums:
        return nums.index(target)
    for indx, val in enumerate(nums):
        if val > target:
            return indx
    return len(nums)
assert Grow_With_Data([1,3,5,6], 5) == 2
assert Grow_With_Data([1,3,5,6], 2) == 1
assert Grow_With_Data([1,3,5,6], 7) == 4
assert Grow_With_Data([1,3,5,6], 0) == 0
print('\n Pass')

# 3. Binary Search
def Grow_With_Data(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2 
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
assert Grow_With_Data([1,3,5,6], 5) == 2
assert Grow_With_Data([1,3,5,6], 2) == 1
assert Grow_With_Data([1,3,5,6], 7) == 4
assert Grow_With_Data([1,3,5,6], 0) == 0
print('\n Pass')
