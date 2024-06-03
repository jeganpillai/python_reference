# Question: Sort Only the Vowels present in the string

# English Video: https://www.youtube.com/watch?v=ZBUh6I5pCJ8
# Tamil Video: https://www.youtube.com/watch?v=2seZ5WJUlFY

# Approach 1: Using FOR loop
def Grow_With_Data(s):
    vowels = []
    for i in s:
        if i.lower() in ['a','e','i','o','u']:
            vowels.append(i)
    vowels.sort()
    cnt = 0
    result = []
    for i in s:
        if i.lower() in ['a','e','i','o','u']:
            result.append(vowels[cnt])
            cnt += 1
        else:
            result.append(i)
    return ''.join(result)
assert Grow_With_Data('GrowWIthDAta') == 'GrAwWIthDato'
assert Grow_With_Data('lEetcOde') == 'lEOtcede'
assert Grow_With_Data('lYmpH') == 'lYmpH'
print('Passed!!')

# Approach 2: Using enumerate
def Grow_With_Data(s):
    vowels = []
    index_pos = []
    for indx, val in enumerate(s):
        if val.lower() in ['a','e','i','o','u']:
            vowels.append(val)
            index_pos.append(indx)
    vowels.sort()
    result = list(s)
    for indx, val in enumerate(index_pos):
        result[val] = vowels[indx]
    return ''.join(result)
assert Grow_With_Data('GrowWIthDAta') == 'GrAwWIthDato'
assert Grow_With_Data('lEetcOde') == 'lEOtcede'
assert Grow_With_Data('lYmpH') == 'lYmpH'
print('Passed!!')
