# Question: convert Roman letters to integer
# Video: https://www.youtube.com/watch?v=DOxo5E3wXSE
'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
def Grow_With_Data(s):
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for indx, val in enumerate(s):
        if indx == len(s)-1:
            result += roman_dict[val]
        elif roman_dict[val] < roman_dict[s[indx+1]]:
            result -= roman_dict[val]
        else:
            result += roman_dict[val]
    return result 
assert Grow_With_Data('III') == 3
assert Grow_With_Data('IV') == 4
assert Grow_With_Data('IX') == 9
assert Grow_With_Data('LVIII') == 58
assert Grow_With_Data('MCMXCIV') == 1994
print ('\n Pass')
