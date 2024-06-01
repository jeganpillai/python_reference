# Question: Find the Number of Segments in a String

# English Video: https://www.youtube.com/watch?v=9pHxrihHmz4
# Tamil Video: https://www.youtube.com/watch?v=_MCSMbRAJDg

# Approach 1: Looping logic 
def Grow_With_Data(s):
    cnt = 0
    chk = ''
    for indx, val in enumerate(s):
        if val == ' ':
            if chk:
                cnt += 1
                chk = ''
            else:
                continue
        else:
            chk += val
    return cnt + 1 if chk else cnt
assert Grow_With_Data(', , , ,        a, eaefa') == 6
assert Grow_With_Data('') == 0
assert Grow_With_Data('Of all the gin joints in all the towns in all the world,   ') == 13
assert Grow_With_Data('Hello, my name is John') == 5
assert Grow_With_Data('Hello') == 1
print('Passed!')

# Approach 2: Using inbuilt function split()
def Grow_With_Data(s):
    return len(s.split())
assert Grow_With_Data(', , , ,        a, eaefa') == 6
assert Grow_With_Data('') == 0
assert Grow_With_Data('Of all the gin joints in all the towns in all the world,   ') == 13
assert Grow_With_Data('Hello, my name is John') == 5
assert Grow_With_Data('Hello') == 1
print('Passed!')

