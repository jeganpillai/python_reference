# Question: count numbers with unique digits
# Video: https://www.youtube.com/watch?v=ushz6zMzy1g

# Approach 1: convert number to string and track with string concatenation 
def Grow_With_Data(a,b):
    result = 0
    for number in range(a, b+1):
        s = str(number)
        chk = ''
        for digit in s:
            if digit in chk:
                break 
            else:
                chk = chk + digit
        if chk == s:
            result += 1 
    return result
assert Grow_With_Data(1,20) == 19
assert Grow_With_Data(9,19) == 10
assert Grow_With_Data(80,120) == 27
print('\n Passed!')

# Approach 2: convert number to string and track with list append 
def Grow_With_Data(a,b):
    result = 0
    for number in range(a, b+1):
        s = str(number)
        chk = []
        for digit in s:
            if digit in chk:
                break 
            else:
                chk.append(digit)
        if ''.join(chk) == s:
            result += 1 
    return result
assert Grow_With_Data(1,20) == 19
assert Grow_With_Data(9,19) == 10
assert Grow_With_Data(80,120) == 27
print('\n Passed!')

# Approach 3: without conversting the number, use MOD and check for duplicate digits 
def Grow_With_Data(a,b):
    result = 0
    for number in range(a, b+1):
        pos = number
        chk = []
        while number > 0:
            i = number%10
            if i in chk:
                break
            else:
                chk.insert(0,i)
            number = number // 10
        if int(''.join(str(z) for z in chk)) == pos:
            result += 1 
    print('chk: ', chk, ' and ', result)
    return result
assert Grow_With_Data(1,20) == 19
assert Grow_With_Data(9,19) == 10
assert Grow_With_Data(80,120) == 27
print('\n Passed!')

# Approach 4: Simple approach by using SET() function 
def Grow_With_Data(a,b):
    result = 0
    for i in range(a, b+1):
        s = list(str(i))
        if len(s) == len(set(s)):
            result += 1 
    return result
assert Grow_With_Data(1,20) == 19
assert Grow_With_Data(9,19) == 10
assert Grow_With_Data(80,120) == 27
print('\n Passed!')

