# Question: distribute elements in an array into two different arrays.
# Video: https://www.youtube.com/watch?v=IDNH9ThKhkY

# using normal FOR loop
def Grow_With_Data(nums):
    result_1 = [nums[0]]
    result_2 = [nums[1]]

    for i in nums[2:]:
        if result_1[-1] > result_2[-1]:
            result_1.append(i)
        else:
            result_2.append(i)
    return result_1 + result_2
assert Grow_With_Data([2,1,3]) == [2,3,1]
assert Grow_With_Data([5,4,3,8]) == [5, 3, 4, 8]
print('Passed!')

# using range() function 
def Grow_With_Data(nums):
    result_1 = [nums[0]]
    result_2 = [nums[1]]

    for i in range(2,len(nums)):
        if result_1[-1] > result_2[-1]:
            result_1.append(nums[i])
        else:
            result_2.append(nums[i])
    return result_1 + result_2
assert Grow_With_Data([2,1,3]) == [2,3,1]
assert Grow_With_Data([5,4,3,8]) == [5, 3, 4, 8]
print('Passed!')
