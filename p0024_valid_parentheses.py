# Question: Determine if the input string has valid parentheses
# Video: https://www.youtube.com/watch?v=7NNAQMlr0PA

'''
For a string to be considered valid:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. An empty string is also considered valid 
'''

# Approach 1: Basic loop 
def Grow_With_Data(s):
    match_pair = {')':'(', '}':'{',']':'['}
    deposit = []
    for i in s:
        if not i in match_pair:
            deposit.append(i)
        elif not deposit or deposit[-1] != match_pair[i]:
            return False
        else:
            deposit.pop()
    if deposit:
        return False
    return True
assert Grow_With_Data('()') == True
assert Grow_With_Data('()[]{}') == True
assert Grow_With_Data('(]') == False
assert Grow_With_Data('([)]') == False
assert Grow_With_Data('{[]}') == True
assert Grow_With_Data('()(') == False 
print('\n Pass')

# Approach 2: Finetuned code
def Grow_With_Data(s):
    match_pair = {')':'(', '}':'{',']':'['}
    deposit = []
    for i in s:
        if i in match_pair:
            top_element = deposit.pop() if deposit else '#'
            if match_pair[i] != top_element:
                return False
        else:
            deposit.append(i)
    return not deposit
assert Grow_With_Data('()') == True
assert Grow_With_Data('()[]{}') == True
assert Grow_With_Data('(]') == False
assert Grow_With_Data('([)]') == False
assert Grow_With_Data('{[]}') == True
assert Grow_With_Data('()(') == False 
print('\n Pass')

# Approach 3: Better coding 
def Grow_With_Data(s):
    match_pair = {')': '(', '}': '{', ']': '['}
    deposit = []

    for char in s:
        if char in match_pair.values():
            deposit.append(char)
        elif char in match_pair.keys():
            if not deposit or match_pair[char] != deposit.pop():
                return False

    return not deposit
assert Grow_With_Data('()') == True
assert Grow_With_Data('()[]{}') == True
assert Grow_With_Data('(]') == False
assert Grow_With_Data('([)]') == False
assert Grow_With_Data('{[]}') == True
assert Grow_With_Data('()(') == False 
print('\n Pass')
