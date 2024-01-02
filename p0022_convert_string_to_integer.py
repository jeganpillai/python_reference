# Question : Convert String to Integer
# Video: https://www.youtube.com/watch?v=M_uxgF6ix5w

def Grow_With_Data(str):
    str = str.strip()
    
    if len(str) < 1 or str == '-' or str == '+':
        return 0
    sign = 1
    if str[0] in ['-','+']:
        if str[0] == '-':
            sign = -1
        str = str[1:]
    result = 0
        
    for i in range(len(str)):
        if not str[0].isdigit():
            break

        if str[i].isdigit():
            result = result*10 + int(str[i])
        else:
            break
    # return 0 if result * sign < -2**31 or result * sign > (2 ** 31 - 1) else result * sign
    return max(-2**31, min(result * sign, 2**31-1))
assert Grow_With_Data('42') == 42
assert Grow_With_Data('+-2') == 0
assert Grow_With_Data('   -42') == -42
assert Grow_With_Data('4193 with words') == 4193
assert Grow_With_Data('words and 987') == 0
assert Grow_With_Data('-91283472332') == -2**31
assert Grow_With_Data('') == 0
assert Grow_With_Data('-') == 0
assert Grow_With_Data('+1') == 1
assert Grow_With_Data('+') == 0
assert Grow_With_Data('+-2') == 0
assert Grow_With_Data('3.14159') == 3
assert Grow_With_Data('2147483648') == 2**31-1
assert Grow_With_Data('.1') == 0
print('\n Pass')
