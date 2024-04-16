# Question: Remove Vowels from a given string

# English Video: 
# Tamil Video: 

# Approach 1: General FOR loop
def Grow_With_Data(s):
    output = ''
    chk = {'a','e','i','o','u'}
    for i in s:
        if not i.lower() in chk:
            output += i
    return output
assert Grow_With_Data('GrowWithData') == 'GrwWthDt'
assert Grow_With_Data('UnitedNations') == 'ntdNtns'
print('Passed!')

# Approach 2: List comprehension way 
def Grow_With_Data(s):
    return ''.join([i for i in s if not i.lower() in set('aeiou')])
assert Grow_With_Data('GrowWithData') == 'GrwWthDt'
assert Grow_With_Data('UnitedNations') == 'ntdNtns'
print('Passed!')
