# Question: minimum number of operations needed so that all elements of the array are greater than or equal to the threshold
# Video: https://www.youtube.com/watch?v=y9bb2uY6l_8

# *** Approach 1: Simple Count of Elements ***
def Grow_With_Data(nums, k):
    result = 0
    for i in nums:
        result += 1 if i < k else 0
        # print(i, ' : ', k, ' : ', result)
    return result 
Grow_With_Data(nums, k)
assert Grow_With_Data([2,11,10,1,3], 10) == 3
assert Grow_With_Data([1,1,2,4,9], 1) == 0
assert Grow_With_Data([1,1,2,4,9], 9) == 4
print('Passed!')

# *** Approach 2: Count and Remove the Element ***
def Grow_With_Data(nums, k):
    result = 0
    while min(nums) < k:
        result += 1
        nums.remove(min(nums))
    print(result, ' : ', nums)
    return result 
assert Grow_With_Data([2,11,10,1,3], 10) == 3
assert Grow_With_Data([1,1,2,4,9], 1) == 0
assert Grow_With_Data([1,1,2,4,9], 9) == 4
print('Passed!')

