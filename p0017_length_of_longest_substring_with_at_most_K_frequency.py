# Question: Get The Length Of Longest Substring With At Most K Frequency
# Video: 

# Two points Algorithm to create sliding window
def Grow_With_Data(nums, k):
    left, right, freq, max_length = 0, 0, {}, 0

    for indx, val in enumerate(nums):
        freq[val] = freq.get(val,0) + 1

        if freq[val] > k:
            max_length = max(max_length, right - left)
            while nums[left] != val:
                freq[nums[left]] -= 1
                left += 1
            freq[nums[left]] -= 1
            left += 1

        right += 1

    return max(max_length, right - left)
assert Grow_With_Data([1,2,3,1,2,3,1,2],1) == 3 
assert Grow_With_Data([1,2,3,1,2,3,1,2],2) == 6 
assert Grow_With_Data([1,4,4,3],1) == 2 
assert Grow_With_Data([2,2,3],1) == 2
print('\n Pass')

# simpler version 
def Grow_With_Data(nums, k):
    freq = {}
    left = 0 
    max_length = 0

    for indx, val in enumerate(nums):
        freq[val] = freq.get(val,0) + 1        
        while freq[val] > k:
            freq[nums[left]] -= 1 
            left += 1 
        max_length = max(max_length, indx - left + 1 )
    return max_length

assert Grow_With_Data([1,2,3,1,2,3,1,2],1) == 3 
assert Grow_With_Data([1,2,3,1,2,3,1,2],2) == 6 
assert Grow_With_Data([1,4,4,3],1) == 2 
assert Grow_With_Data([2,2,3],1) == 2
print('\n Pass')
