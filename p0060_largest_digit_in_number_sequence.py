# Question: Find the largest digit in an number sequence.
# English Video:
# Tamil Video: 

# Approach 1: Convert to string and find the largest
def Grow_With_Data(num):
    return int(max(list(str(num))))
assert Grow_With_Data(14634) == 6
assert Grow_With_Data(543333) == 5
assert Grow_With_Data(0) == 0
print('Passed!')

# Approach 2: Use List to Track Digits
def Grow_With_Data(num):
    if num == 0:
        return 0
    result = []
    while num > 0:
        result.append(num%10)
        num = num//10
    return max(result)
assert Grow_With_Data(14634) == 6
assert Grow_With_Data(543333) == 5
assert Grow_With_Data(0) == 0
print('Passed!')

# Approach 3: Track Single Digit at a Time
num = 14634
def Grow_With_Data(num):
    result = 0
    while num > 0:
        if num%10 > result:
            result = num%10
        num = num//10
    return result
assert Grow_With_Data(14634) == 6
assert Grow_With_Data(543333) == 5
assert Grow_With_Data(0) == 0
print('Passed!')
