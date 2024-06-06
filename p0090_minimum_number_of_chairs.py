# Question: Minimum Number of Chairs

# English Video: 
# Tamil Video: 

# Approach 1: Basic loopig logic 
def Grow_With_Data(s):
    cnt = 0
    max_cnt = 0
    for i in s:
        if i == 'E':
            cnt += 1
        else:
            cnt -= 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt
Grow_With_Data(s)
assert Grow_With_Data('ELEELEELLL') == 3
assert Grow_With_Data('EEEEEEE')    == 7
assert Grow_With_Data('ELELEEL')    == 2 
print('Passed!!')

# Approach 2: Fine tuned code 
def Grow_With_Data(s):
    cnt, max_cnt = 0, 0
    for i in s:
        cnt += 1 if i == 'E' else -1
        max_cnt = max(max_cnt,cnt)
    return max_cnt
Grow_With_Data(s)
assert Grow_With_Data('ELEELEELLL') == 3
assert Grow_With_Data('EEEEEEE')    == 7
assert Grow_With_Data('ELELEEL')    == 2 
print('Passed!!')
