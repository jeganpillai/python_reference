# Question : Identify the type of triangle from the given element of length three
# Video: https://www.youtube.com/watch?v=78GyTXm8B9s
"""
A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
"""
# *** Approach 1: Basic code structure *** 
def Grow_With_Data(nums):
    if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[2] + nums[0] > nums[1]:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return 'equilateral'
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        return 'none'

Grow_With_Data(nums)
assert Grow_With_Data([3,3,3]) == 'equilateral' 
assert Grow_With_Data([3,4,5]) == 'scalene'
assert Grow_With_Data([8,4,4]) == 'none'
print('\n Passed!')

# *** Approach 2: Replace multiple AND with SET() and algorithm to validate sum of two sides must be greater than the third side *** 
def Grow_With_Data(nums):
    if sum(sorted(nums)[:2]) > max(nums):
        if len(set(nums)) == 1:
            return 'equilateral'
        elif len(set(nums)) == 2:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        return 'none'
assert Grow_With_Data([3,3,3]) == 'equilateral' 
assert Grow_With_Data([3,4,5]) == 'scalene'
assert Grow_With_Data([8,4,4]) == 'none'
print('\n Passed!')  

# *** Approach 3: Single line of code *** 
def Grow_With_Data(nums):
    return 'none' if sum(sorted(nums)[:2]) <= max(nums) else 'equilateral' if len(set(nums)) == 1 else 'isosceles' if len(set(nums)) == 2 else 'scalene'
assert Grow_With_Data([3,3,3]) == 'equilateral' 
assert Grow_With_Data([3,4,5]) == 'scalene'
assert Grow_With_Data([8,4,4]) == 'none'
print('\n Passed!')  


