# Question: Find the given word is valid or not

# English Video: https://www.youtube.com/watch?v=G8owWNIv_VU
# Tamil Video: https://www.youtube.com/watch?v=Npqm9WAVPUo

# Approach 1: Brute force method using FOR loop 
def Grow_With_Data(s):
    output = []
    for indx, val in enumerate(s):
        if indx == 0:
            if val == '?':
                if s[indx+1] == '?':
                    output.append('1')
                elif int(s[indx+1]) >= 2:
                    output.append('0')
                else:
                    output.append('1')
            else:
                output.append(val)
        if indx == 1:
            if val == '?':
                if s[indx - 1] == '?':
                    output.append('1')
                elif s[indx - 1] == '1':
                    output.append('1')
                else:
                    output.append('9')
            else:
                output.append(val)
        if indx == 2:
            output.append(':')
        if indx == 3:
            if val == '?':
                output.append('5')
            else:
                output.append(val)
        if indx == 4:
            if val == '?':
                output.append('9')
            else:
                output.append(val)
    return ''.join(output)
assert Grow_With_Data('1?:?4') =='11:54'
assert Grow_With_Data('0?:5?') =='09:59'
assert Grow_With_Data('?1:?6') == '11:56'
assert Grow_With_Data('?2:2?') == '02:29'
print('Passed!')


# Approach 2: Simple If condition block 
def Grow_With_Data(s):
    s = list(s)
    if s[0] == '?' and s[1] == '?':
        s[0] = '1'
        s[1] = '1'
    elif s[0] == '?':
        s[0] = '0' if int(s[1]) >= 2 else '1'
    if s[1] == '?':
        s[1] = '9' if s[0] == '0' else '1'
    if s[3] == '?':
        s[3] = '5'
    if s[4] == '?':
        s[4] = '9'
    return ''.join(s)
assert Grow_With_Data('1?:?4') =='11:54'
assert Grow_With_Data('0?:5?') =='09:59'
assert Grow_With_Data('?1:?6') == '11:56'
assert Grow_With_Data('?2:2?') == '02:29'
print('Passed!')

# Approach 3: Simplify the code further 
def Grow_With_Data(s):
    s = list(s)
    if s[0] == '?':
        s[0] = '1' if s[1] in ('?','0','1') else '0'
    if s[1] == '?':
        s[1] = '9' if s[0] == '0' else '1'
    if s[3] == '?':
        s[3] = '5'
    if s[4] == '?':
        s[4] = '9'
    return ''.join(s)
assert Grow_With_Data('1?:?4') =='11:54'
assert Grow_With_Data('0?:5?') =='09:59'
assert Grow_With_Data('?1:?6') == '11:56'
assert Grow_With_Data('?2:2?') == '02:29'
print('Passed!')
