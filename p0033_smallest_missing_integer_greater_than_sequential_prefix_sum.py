# Question: Find the Smallest Missing Integer Greater Than Sequential Prefix Sum
# Video: https://www.youtube.com/watch?v=ZYA0EgUDfas

# **Approach 1: Using FOR loop**
def Grow_With_Data(nums):
    result = 0
    for indx in range(len(nums)):
        if indx == 0 or nums[indx] == nums[indx-1] + 1:
            result += nums[indx]
        else:
            break
    # print('seq: ', seq)
    while True:
        if result not in nums:
            return result
        else:
            result += 1 
assert Grow_With_Data([29,30,31,32,33,34,35,36,37]) == 297
assert Grow_With_Data([3,4,5,1,12,14,13]) == 15
assert Grow_With_Data([1,2,3,2,5]) == 6
print ('\n Passed!')
          
# **Approach 2: Using WHILE loop**
def Grow_With_Data(nums):
    result = nums[0]
    indx = 0
    while indx < len(nums) - 1 and nums[indx+1] - nums[indx] == 1:
            result += nums[indx + 1]
            indx += 1 

    # print('seq: ', seq)
    while True:
        if result not in nums:
            return result
        else:
            result += 1 
assert Grow_With_Data([29,30,31,32,33,34,35,36,37]) == 297
assert Grow_With_Data([3,4,5,1,12,14,13]) == 15
assert Grow_With_Data([1,2,3,2,5]) == 6
print ('\n Passed!')
