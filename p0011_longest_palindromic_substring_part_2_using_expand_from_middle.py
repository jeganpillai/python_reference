# Question: Given a string, find the longest palindromic substring. You may assume that the maximum length of the string is 1000.
# use "Expand Around Center" 

def Grow_With_Data(s):
    start = 0 
    end = 0
    max_len = 0
    for i in range(len(s)):
        len1 = helper(s, i, i)
        len2 = helper(s, i, i+1)
        # print('The checking values are len1 = ', len1, ' and len2 = ', len2, ' max length = ', max_len)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
        # print('after IF condition, max_len = ', max_len, ' start = ', start, ' and end = ', end)
    return s[start:end+1]

def helper(s, left, right):
    # print('In helper: ', left, ' and ', right)
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        # print('In loop with left = ', left, ' and right = ', right)
    return right - left - 1

assert Grow_With_Data('bababad') == 'ababa' 
assert Grow_With_Data('malayalam') == 'malayalam'
print('\n(Passed!)')

