# Question: Find the Integer Added to Array

# English Video: 
# Tamil Video: 

# Approach 1: Sort and Check Difference for All Elements
def Grow_With_Data(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    
    x = nums2[0] - nums1[0]

    for i in range(1, len(nums1)):
        if nums2[i] - nums1[i] != x:
            return None
    return x
assert Grow_With_Data([2,6,4], [9,7,5]) == 3
assert Grow_With_Data([10], [5]) == -5 
assert Grow_With_Data([1,1,1,1], [1,1,1,1]) == 0
print('Passed!!')

# Approach 2: Use sort() In-Place of sorted()
def Grow_With_Data(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    x = nums2[0] - nums1[0]

    for i in range(1, len(nums1)):
        if nums2[i] - nums1[i] != x:
            return None
    return x
assert Grow_With_Data([2,6,4], [9,7,5]) == 3
assert Grow_With_Data([10], [5]) == -5 
assert Grow_With_Data([1,1,1,1], [1,1,1,1]) == 0
print('Passed!!')

# Approach 3: Using Simple Algorithm
def Grow_With_Data(nums1, nums2):
    return sorted(nums2)[0] - sorted(nums1)[0]
assert Grow_With_Data([2,6,4], [9,7,5]) == 3
assert Grow_With_Data([10], [5]) == -5 
assert Grow_With_Data([1,1,1,1], [1,1,1,1]) == 0
print('Passed!!')

# Approach 4: Using min() Function
def Grow_With_Data(nums1, nums2):
    return min(nums2) - min(nums1)
assert Grow_With_Data([2,6,4], [9,7,5]) == 3
assert Grow_With_Data([10], [5]) == -5 
assert Grow_With_Data([1,1,1,1], [1,1,1,1]) == 0
print('Passed!!')

# Approach 5: Find the Average Difference
def Grow_With_Data(nums1, nums2):
    return (sum(nums2) - sum(nums1))/len(nums1)
assert Grow_With_Data([2,6,4], [9,7,5]) == 3
assert Grow_With_Data([10], [5]) == -5 
assert Grow_With_Data([1,1,1,1], [1,1,1,1]) == 0
print('Passed!!')

