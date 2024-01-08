# Question Given a value, remove all the instanes of that value in a given array
# Video: https://www.youtube.com/watch?v=IMEme4QmyyQ

# Approach 1: In-place Modification
def Grow_With_Data(nums, val):
    indx = 0 
    while indx < len(nums):
        if nums[indx] == val:
            nums.pop(indx)
        else:
            indx += 1
    return indx
assert Grow_With_Data([3,2,2,3], 3) == 2           # nums = [2, 2]
assert Grow_With_Data([0,1,2,2,3,0,4,2], 2) == 5   # nums = [0, 1, 3, 0, 4]
print('\n Pass')
  
# Approach 2: Efficient Space Utilization
def Grow_With_Data(nums, val):
    len_chk = len(nums)
    indx = 0
    while indx < len_chk:
        if nums[indx] == val:
            nums[indx] = nums[-1]
            nums.pop()
            len_chk = len(nums)
        else:
            indx += 1 
    return len(nums)
assert Grow_With_Data([3,2,2,3], 3) == 2           # nums = [2, 2]
assert Grow_With_Data([0,1,2,2,3,0,4,2], 2) == 5   # nums = [0, 1, 3, 0, 4]
print('\n Pass')
  
# Approach 3: Return New Length
def Grow_With_Data(nums, val):
    left, right = 0, len(nums)
    
    while left < right:
        if nums[left] == val:
            nums[left] = nums[right - 1]
            right -= 1
        else:
            left += 1
    
    return right
assert Grow_With_Data([3,2,2,3], 3) == 2           # nums = [2, 2]
assert Grow_With_Data([0,1,2,2,3,0,4,2], 2) == 5   # nums = [0, 1, 3, 0, 4]
print('\n Pass')
  
