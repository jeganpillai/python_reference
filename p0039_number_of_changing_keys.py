# Question: find the number of times we change keys while typing the string
# Video: https://www.youtube.com/watch?v=UUCpuy919h4
"""
You are given a string typed by a user. Changing a key is defined as using a key different from the last used key. 

For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.

Return the number of times the user had to change the key while typing the string.
"""
# *** Approach 1: Assigning the Previous Character to a Variable *** 
def Grow_With_Data(s):
    result = 0 
    current_key = s[0].lower()
    for char in s[1:]:
        if char.lower() != current_key:
            result += 1 
            current_key = char.lower()
    return result

assert Grow_With_Data('aAbBcC') == 2 
assert Grow_With_Data('AaAaAaaA') == 0
print('\n Passed!')

# *** Approach 2: Comparing the Current and Previous Characters Each Time *** 
def Grow_With_Data(s):
    result = 0 
    for indx, val in enumerate(s):
        if indx == 0:
            continue
        # print(val.lower() , s[indx-1].lower(), ' indx: ', indx, ' result: ', result)
        if not val.lower() == s[indx-1].lower():
            result += 1
    return result
assert Grow_With_Data('aAbBcC') == 2 
assert Grow_With_Data('AaAaAaaA') == 0
print('\n Passed!')
