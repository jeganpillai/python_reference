# Question: Divide an Array into subarrays with minimum cost
# Video: https://www.youtube.com/watch?v=2rZ6b4KjaWw

# *** Approach 1: Brute Force Method *** 
def Grow_With_Data(nums):
    result = float('inf')
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                print(nums[:j], nums[j:k], nums[k:] )
                result = min(result, nums[:j][0] + nums[j:k][0] + nums[k:][0])

    return result
assert Grow_With_Data([1,2,3,12]) == 6
assert Grow_With_Data([5,4,3]) == 12
assert Grow_With_Data([10,3,1,1]) == 12
print('\n Passed!')

# *** Approach 2: General FOR loop *** 
def Grow_With_Data(nums):
    n = len(nums)
    s = nums[0]
    nums = sorted(nums[1:n])
    s = s + nums[0] + nums[1]
    return s
assert Grow_With_Data([1,2,3,12]) == 6
assert Grow_With_Data([5,4,3]) == 12
assert Grow_With_Data([10,3,1,1]) == 12
print('\n Passed!')

# *** Approach 3: Short and Simple version *** 
def Grow_With_Data(nums):
    return nums[0] + sum(sorted(nums[1:])[:2])
assert Grow_With_Data([1,2,3,12]) == 6
assert Grow_With_Data([5,4,3]) == 12
assert Grow_With_Data([10,3,1,1]) == 12
print('\n Passed!')
