# Question: Find the Number of Good Pairs

# English Video: 
# Tamil Video: 

# Approach 1: Using Integer Division
nums1 = [1,3,4]; nums2 = [1,3,4]; k = 1
def Grow_With_Data(nums1, nums2, k):
    cnt = 0
    for i in nums1:
        for j in nums2:
            cnt += 1 if i/(j * k) == i//(j*k) else 0
    return cnt
assert Grow_With_Data([1,3,4], [1,3,4], 1) == 5
assert Grow_With_Data([1,2,4,12], [2,4], 3) == 2
print('Passed!!')

# Approach 2: Using List to track the result 
def Grow_With_Data(nums1, nums2, k):
    cnt = []
    for i in nums1:
        for j in nums2:
            cnt.append(i/(j * k) == i//(j*k))
    return sum(cnt)
assert Grow_With_Data([1,3,4], [1,3,4], 1) == 5
assert Grow_With_Data([1,2,4,12], [2,4], 3) == 2
print('Passed!!')

# Approach 3: Using MOD function 
def Grow_With_Data(nums1, nums2, k):
    cnt = []
    for i in nums1:
        for j in nums2:
            cnt.append(i%(j * k) == 0)
    return sum(cnt)
assert Grow_With_Data([1,3,4], [1,3,4], 1) == 5
assert Grow_With_Data([1,2,4,12], [2,4], 3) == 2
print('Passed!!')
