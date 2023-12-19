# QUestion: Given a integer array and an integer d, return the number of triplets (i, j, k) such that (nums[i] + nums[j] + nums[k]) % d == 0.

# Approach 1: brute force method
def Grow_With_Data(nums, d):
    n = len(nums)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (nums[i] + nums[j] + nums[k]) % d == 0:
                    count += 1
    return count

assert Grow_With_Data([3, 3, 4, 7, 8], 5) == 3 # (3,3,4),(3,4,8),(3,4,8)
assert Grow_With_Data([3,3,3,3],3) == 4 # (3,3,3) : (0,1,2), (0,1,3), (0,2,3), (1,2,3)
assert Grow_With_Data([3,3,3,3],6) == 0 
assert Grow_With_Data([44,77],2) == 0
assert Grow_With_Data([13,63,80],6) == 1 # 13+63+80 = 156/6 = 26
print('\nPass')

# Approach 2: 
def Grow_With_Data(nums, d):
    res = 0
    for i in range(len(nums)-2):
        count = {} # dict() #  defaultdict(int)
        left = (d-nums[i])%d
        for j in range(i+1,len(nums)):

            if nums[j] % d in count:
                res += count[nums[j] % d]

            complement = (left - nums[j]) % d
            if complement in count:
                count[complement] += 1
            else:
                count[complement] = 1
    return res

assert Grow_With_Data([3, 3, 4, 7, 8], 5) == 3
assert Grow_With_Data([3,3,3,3],3) == 4 
assert Grow_With_Data([3,3,3,3],6) == 0
assert Grow_With_Data([44,77],2) == 0
assert Grow_With_Data([13,63,80],6) == 1
print('\nPass')

# Approach 3: 
def Grow_With_Data(nums, d):
    if len(nums) < 3:
        return 0

    n = len(nums)
    count = 0
    remainder_count = [0] * d 

    for num in nums:
        remainder_count[num % d] += 1 
    count = remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6

    for i in range(1, d // 2 + 1):
        count += remainder_count[i] * remainder_count[(d - i)] * remainder_count[(2 * i) % d]

    print(count)
    return count

assert Grow_With_Data([3, 3, 4, 7, 8], 5) == 3
assert Grow_With_Data([3,3,3,3],3) == 4 
assert Grow_With_Data([3,3,3,3],6) == 0
assert Grow_With_Data([44,77],2) == 0
print('\nPass')
