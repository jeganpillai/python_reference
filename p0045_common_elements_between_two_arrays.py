# Question: find the common elements between two arrays
# Video: https://www.youtube.com/watch?v=R7z41_qwFnM

# *** Approach 1: Convert the input array to a dictionary and check ***
nums1 = [4,3,2,3,1]; nums2 = [2,2,5,2,3,6]
# nums1 = [3,4,2,3]; nums2 = [1,5]
def Grow_With_Data(nums1, nums2):
    dict1 = {}
    dict2 = {}

    for num in nums1:
        dict1[num] = dict1.get(num,0) + 1 
    for num in nums2:
        dict2[num] = dict2.get(num,0) + 1 
    # dict1, dict2

    comms_in_nums2 = sum(1 for num in nums1 if num in dict2)
    comms_in_nums1 = sum(1 for num in nums2 if num in dict1)
    return [comms_in_nums2, comms_in_nums1]
Grow_With_Data(nums1, nums2)
assert Grow_With_Data([4,3,2,3,1], [2,2,5,2,3,6]) == [3,4]
assert Grow_With_Data([3,4,2,3], [1,5]) == [0,0]

# *** Approach 2: Directly compare two arrays ***
def Grow_With_Data(nums1, nums2):
    comms_in_nums2 = sum(1 for num in nums1 if num in nums2)
    comms_in_nums1 = sum(1 for num in nums2 if num in nums1)
    return [comms_in_nums2, comms_in_nums1]
assert Grow_With_Data([4,3,2,3,1], [2,2,5,2,3,6]) == [3,4]
assert Grow_With_Data([3,4,2,3], [1,5]) == [0,0]
print('Passed!')

# *** Approach 3: Convert the input array to a set and check ***
nums1 = [4,3,2,3,1]; nums2 = [2,2,5,2,3,6]
nums1 = [3,4,2,3]; nums2 = [1,5]
def Grow_With_Data(nums1, nums2):
    comms_in_nums2 = sum(1 for num in nums1 if num in set(nums2))
    comms_in_nums1 = sum(1 for num in nums2 if num in set(nums1))
    return [comms_in_nums2, comms_in_nums1]
assert Grow_With_Data([4,3,2,3,1], [2,2,5,2,3,6]) == [3,4]
assert Grow_With_Data([3,4,2,3], [1,5]) == [0,0]
print('Passed!')
