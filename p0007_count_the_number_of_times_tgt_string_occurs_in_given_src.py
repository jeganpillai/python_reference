# Question: Given a source and target strings, count the number of times target string occurs in the source string.

# approach 1: basic looping process 
def grow_with_data(src, tgt):
    cnt = 0
    for i in range(len(src)-len(tgt)+1):
        if src[i:i+len(tgt)] == tgt:
            cnt += 1
    return cnt
  
assert grow_with_data('000123041123343412131234342','123') == 3
assert grow_with_data('000123041123343412131234342','') == 0
assert grow_with_data('','123') == 0
assert grow_with_data('123','12345') == 0
print("\n(Passed!)")  

# approach 2 with edge case: simple format 
def grow_with_data(src, tgt):
    if len(tgt) == 0 or len(tgt) == 0 or len(tgt) > len(src):
        return 0  
    return sum(1 for i in range(len(src)-len(tgt)+1) if src[i:i+len(tgt)] == tgt)
  
assert grow_with_data('000123041123343412131234342','123') == 3
assert grow_with_data('000123041123343412131234342','') == 0
assert grow_with_data('','123') == 0
assert grow_with_data('123','12345') == 0
print("\n(Passed!)")  

# approach 3: using inbuilt function 
def grow_with_data(src, tgt):
    if len(tgt) == 0 or len(tgt) == 0 or len(tgt) > len(src):
        return 0
    return src.count(tgt)

assert grow_with_data('000123041123343412131234342','123') == 3
assert grow_with_data('000123041123343412131234342','') == 0
assert grow_with_data('','123') == 0
assert grow_with_data('123','12345') == 0
print("\n(Passed!)")

