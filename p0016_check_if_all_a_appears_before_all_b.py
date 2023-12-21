# Question: Given a string comprising solely of "a" and "b" characters, the task is to determine whether every "a" precedes every "b" in the string. Return True if this condition holds, otherwise return False.

# Approach 1: Looping function with Time complexity of O(n^2)
def Grow_With_Data(s):
    if s[0] == 'b' and 'a' in s: # 'baaab'
        return False 
    if 'a' in s and not 'b' in s: # 'aaaaa'
        return True 
    if s[0] == 'b' and not 'a' in s: # 'bbbbb'
        return True
    c = s[0]
    for indx, val in enumerate(s):
        if c == val:
            continue
        elif c in s[indx+1:]:
            return False 
    return True

# Approach 2: Loop in the string and track the position of a and b with time complexity O(n)
def Grow_With_Data(s):
    pos_a = -1 
    pos_b = -1 
    for indx, val in enumerate(s):
        if val == 'a':
            pos_a = indx
        else:
            if pos_b == -1:
                pos_b = indx
    return (pos_a == -1 and pos_b > 0) or pos_b == -1 or pos_a < pos_b

# Approach 3: Simple one liner 
def Grow_With_Data(s):
    return not 'ba' in s
assert Grow_With_Data("aaabbb") == True 
assert Grow_With_Data("abab") == False
assert Grow_With_Data("bbb") == True 
assert Grow_With_Data("a") == True 
assert Grow_With_Data("aaa") == True 
assert Grow_With_Data("ba") == False
print("\n Pass")
