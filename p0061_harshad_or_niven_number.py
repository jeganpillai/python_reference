# Question: Find if the given number is a Harshad number or not.

# English Video: https://www.youtube.com/watch?v=NUeHFLpG3-0
# Tamil Video: https://www.youtube.com/watch?v=HmnQcHfFUxA

# Approach 1: General Looping logic 
def Grow_With_Data(num):
    chk = 0
    for i in str(num):
        chk += int(i)
    if num % chk == 0:
        return chk
    else:
        return -1
assert Grow_With_Data(18) == 9
assert Grow_With_Data(23) == -1
print('Passed!')

# Approach 2: Using List Comprehension 
def Grow_With_Data(num):
    chk = sum([int(i) for i in str(num)])
    return chk if num / chk == num // chk else -1
assert Grow_With_Data(18) == 9
assert Grow_With_Data(23) == -1
print('Passed!')

# Approach 3: Using While loop
def Grow_With_Data(num):
    chk = 0 
    x = num
    while num > 0:
        chk += num % 10
        num //= 10
    return chk if x / chk == x // chk else -1
assert Grow_With_Data(18) == 9
assert Grow_With_Data(23) == -1
print('Passed!')
