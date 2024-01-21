# Question: Increment an integer array by one and return the resulting array of digits.
# Video: https://www.youtube.com/watch?v=hWbBsyq7GPQ

*** Approach 1: Convert to String and Increment ***
def Grow_With_Data(digits):
    return [int(i) for i in list(str(int(''.join(str(i) for i in digits)) + 1))]

assert Grow_With_Data([1,2,3]) == [1,2,4]
assert Grow_With_Data([4,3,2,1]) == [4,3,2,2]
assert Grow_With_Data([9]) == [1,0]
print('\n Passed!')

*** Approach 2: Using FOR Loop and Increment ***
def Grow_With_Data(digits):
    extra = 1 
    for i in range(len(digits)):
        if digits[-1-i] == 9:
            digits[-1-i] = 0
            if i == len(digits) - 1:
                digits.insert(0,1)
                return digits
        else:
            digits[-1-i] += 1 
            return digits
assert Grow_With_Data([1,2,3]) == [1,2,4]
assert Grow_With_Data([4,3,2,1]) == [4,3,2,2]
assert Grow_With_Data([9]) == [1,0]
print('\n Passed!')
          
*** Approach 3: Using WHILE Loop and Increment ***
def Grow_With_Data(digits):
    i = -1
    while digits[i] == 9:
        digits[i] = 0
        i -= 1 
        if -i > len(digits):
            print('First ', digits)
            digits.insert(0,1)
            return digits
    else:
        digits[i] += 1 
        return digits
assert Grow_With_Data([1,2,3]) == [1,2,4]
assert Grow_With_Data([4,3,2,1]) == [4,3,2,2]
assert Grow_With_Data([9]) == [1,0]
print('\n Passed!')
