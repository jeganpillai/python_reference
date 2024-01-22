# Question: Find the longest valid parentheses
# Video: https://www.youtube.com/watch?v=Jkh3-1K96BM

# *** Approach 1: General FOR loop ***
def Grow_With_Data(s):
    stack = []
    dp = [0] * len(s)
    max_length = 0
    for indx, val in enumerate(s):
        if val =='(':
            stack.append(indx)
            continue 
        elif not stack and val == ')':
            continue
        elif stack and val == ')':
            idx = stack.pop()
            cur_len = indx - idx + 1 + (dp[idx-1] if idx-1 >= 0 else 0)
            dp[indx] = cur_len
            if max_length < cur_len:
                 max_length = cur_len
    return max_length
assert Grow_With_Data('(()') == 2
assert Grow_With_Data(')()())') == 4
assert Grow_With_Data('()(()') == 2
assert Grow_With_Data('()(())') == 6
assert Grow_With_Data('((())') == 4                      
print('\n Passed!')

# *** Approach 2: Shorter version *** 
def Grow_With_Data(s):
    stack = [-1]
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length
assert Grow_With_Data('(()') == 2
assert Grow_With_Data(')()())') == 4
assert Grow_With_Data('()(()') == 2
assert Grow_With_Data('()(())') == 6
assert Grow_With_Data('((())') == 4   
print('\n Passed!')
