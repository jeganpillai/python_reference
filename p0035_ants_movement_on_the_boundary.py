# Question: Track Ant's movement on the Boundary
# Video: https://www.youtube.com/watch?v=EnY99z0gRTo

""" 
If the element is < 0, the Ant moves left by that elements value.
If the element is > 0, the Ant moves right by that element value.
Return the number of times the ant returns to the boundary.

If the ant crosses the boundary during its movement, it does not count.  
"""

def Grow_With_Data(nums):
    chk = 0 
    result = 0
    for indx, val in enumerate(nums):
        chk += val
        if chk == 0:
            result += 1 
    return result

assert Grow_With_Data([2,3,-5]) == 1 
assert Grow_With_Data([3,2,-3,-4]) == 0
assert Grow_With_Data([3,2,-3,-4,-2,3,1]) == 1
print('\n Passed!')
