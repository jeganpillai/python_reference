# Question: Given a string, find the length of the first longest substring without repeating characters.

# brute force method 
def helper(s):
    max_len = []
    for i in range(0,len(s)):                                           
        curr_max = [s[i]]                                        
        for j in range(i+1, len(s)):                            
            if s[j] in curr_max:           
                break                    
            else:                                              
                curr_max.append(s[j])                     
        if len(curr_max) > len(max_len): 
            max_len = curr_max           
    return (curr_max, ' and ', max_len)
helper('abcabcbb')

# approach 2: only the length of the longest substring 
s = 'abcabcbb'
def helper(s):
    pos_dict = {}
    max_len, curr_max, start = 0,0,0
    for indx, val in enumerate(s):
        if val in pos_dict and pos_dict[val] >= start:
            max_len = max(max_len, curr_max)
            curr_max = indx - pos_dict[val]
            start = pos_dict[val] + 1
        else:
            curr_max += 1 
        pos_dict[val] = indx
    return max(max_len, curr_max)
helper(s)

# approach 3: gets the longest substring and the length 
s = 'abcabcbb'
def helper(s):
    pos_dict = {}
    max_len = []
    curr_max = []
    start = 0
    for indx, val in enumerate(s):
        if val in pos_dict and pos_dict[val] >= start:
            max_len = max(max_len,curr_max, key=len)
            curr_max = list(s[pos_dict[val]+1 : indx+1])
            start = pos_dict[val] + 1
        else:
            curr_max.append(val)
        pos_dict[val] = indx
    return ''.join(max(max_len, curr_max, key = len)), len(''.join(max(max_len, curr_max, key = len)))
helper(s)

## for better coding practice: 
def lengthOfLongestSubstring(s):
    pos_dict = {}
    max_len = []
    curr_max = []
    start = 0
    for indx, val in enumerate(s):
        if val in pos_dict and pos_dict[val] >= start:
            max_len = max(max_len,curr_max, key=len)
            curr_max = list(s[pos_dict[val]+1 : indx+1])
            start = pos_dict[val] + 1
        else:
            curr_max.append(val)
        pos_dict[val] = indx
    return len(''.join(max(max_len, curr_max, key = len)))

assert lengthOfLongestSubstring('abcabcbb') == 3 
assert lengthOfLongestSubstring('bbbbb') == 1
assert lengthOfLongestSubstring('pwwkew') == 3 
print("\n(Passed!)")
