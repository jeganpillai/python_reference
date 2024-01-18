# Question: Count elements with Maximum Frequency 
# Video: https://www.youtube.com/watch?v=U2ysXF_M6CA

# Approach 1: Brute Force Method 
def Grow_With_Data(nums):
    max_freq = 0
    max_freq_count = 0 
    for num in nums:
        current_freq = nums.count(num)
        if current_freq > max_freq:
            max_freq = current_freq
            max_freq_count = 1 
        elif current_freq == max_freq:
            max_freq_count += 1 
    return max_freq_count 
assert Grow_With_Data([1,2,2,3,1,4]) == 4
assert Grow_With_Data([1, 2, 3, 4, 5]) == 5
print('\n Passed!')

# Approach 2: Using Dictionary
def Grow_With_Data(nums):
    d = {} 
    for i in nums:
        d[i] = d[i] + 1 if i in d else 1 
    max_val = max(d.values())
    result = 0
    for key, val in d.items():
        if val == max_val:
            result += 1
    return result
assert Grow_With_Data([1,2,2,3,1,4]) == 4
assert Grow_With_Data([1, 2, 3, 4, 5]) == 5
print('\n Passed!')

# Approach 3: Better version of approach 2
def Grow_With_Data(nums):
    d = {} 
    for i in nums:
        d[i] = d.get(i, 0) + 1 
    max_val = max(d.values())
    result = sum(val for val in d.values() if val == max_val)
    return result
assert Grow_With_Data([1,2,2,3,1,4]) == 4
assert Grow_With_Data([1, 2, 3, 4, 5]) == 5
print('\n Passed!')

