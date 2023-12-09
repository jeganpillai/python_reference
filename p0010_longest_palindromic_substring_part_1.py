# Question: Given a string, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

def Grow_With_Data(s):
    max_of_string = s[0]
    for indx, val in enumerate(s):
        substr = s[indx+1:]
        marks = [j+indx+2 for j in range(len(substr)) if substr[j] == val]
        str = [s[indx:cut] for cut in marks if s[indx:cut] == s[indx:cut][::-1] and 
               len(max_of_string) < len(s[indx:cut])]
        if str:
            max_of_string = max(str, key = len)
        # print('value: ', val, ' other : ', marks, ' substring = ', str, ' max: ',max_of_string)
    return max_of_string

assert Grow_With_Data('bababad') == 'babab' 
assert Grow_With_Data('malayalam') == 'malayalam'
print('\n(Passed!)')
