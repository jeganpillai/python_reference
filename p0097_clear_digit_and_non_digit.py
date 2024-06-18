# Question: Clear Digit and Non Digit

# English Video: 
# Tamil Video: 

def Grow_With_Data(s):
    s = list(s)
    while any(char.isdigit() for char in s):
        for indx, val in enumerate(s):
            if val.isdigit():
                del s[indx]
                del s[indx-1]
                break
    return ''.join(s)

assert Grow_With_Data('abc') == 'abc'
assert Grow_With_Data('cb34') == ''
assert Grow_With_Data('cb34') == 'a'
assert Grow_With_Data('li5i56') == ''
print('Passed!!')
