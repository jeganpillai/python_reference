# Question : find the sum of unique elements in an integer array
# Video: https://www.youtube.com/watch?v=TF4-pi5RTVg

# Approach 1: Brute Force Method
def Grow_With_Data(nums):
    all_values = []
    duplicates = []
    result = 0
    for i in nums:
        if i in all_values:
            duplicates.append(i)
            continue
        all_values.append(i)
    for i in all_values:
        if not i in duplicates:
            result += i
    return result
assert Grow_With_Data([1,2,3,2]) == 4 
assert Grow_With_Data([1,1,1,1,1]) == 0 
assert Grow_With_Data([1,2,3,4,5]) == 15 

print("\n(Passed!)")

# Approach 2: Using Dictionary
def Grow_With_Data(nums):
    d = {}
    for i in nums:
        d[i] = d[i] + 1 if i in d else 1
    print(d)
    result = 0
    for key, val in d.items():
        result += key if val == 1 else 0
    print(result)
    return result
assert Grow_With_Data([1,2,3,2]) == 4 
assert Grow_With_Data([1,1,1,1,1]) == 0 
assert Grow_With_Data([1,2,3,4,5]) == 15 

print("\n(Passed!)")

