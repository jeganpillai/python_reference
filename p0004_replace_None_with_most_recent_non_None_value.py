# Question: In a given list, replace None with most recent non None value

# basic code: 
input_lst =  [1,None,2,3,None,None,5,None]
input_lst = [None,8,None] 

def helper(input_lst):
    if input_lst is None or input_lst == []:
        return input_lst
    output_lst = []
    chk = None 

    for i in input_lst:
        if i is not None:
            chk = i
        output_lst.append(chk)            
    return output_lst
helper(input_lst)

# better coding with practice template
def helper(input_lst):
    if input_lst is None or input_lst == []:
        return input_lst
        
    output_lst = []
    chk = None 

    for i in input_lst:
        if i is not None:
            chk = i
        output_lst.append(chk)
    return output_lst
assert helper(None) == None
assert helper([]) == []
assert helper([None,8,None]) == [None,8,8]
assert helper([1,None,2]) == [1,1,2]
assert helper([5,None,None]) == [5,5,5]
assert helper([1,None,2,3,None,None,5,None]) == [1,1,2,3,3,3,5,5]
print('\n(passed!)')

# how about list comprehension and walrus operator
def helper(input_lst):
    if input_lst is None or input_lst == []:
        return input_lst
    output_lst = []
    chk = None 
    output_lst = [chk if item is None else (chk := item) for item in input_lst]
    return output_lst

assert helper(None) == None
assert helper([]) == []
assert helper([None,8,None]) == [None,8,8]
assert helper([1,None,2]) == [1,1,2]
assert helper([5,None,None]) == [5,5,5]
assert helper([1,None,2,3,None,None,5,None]) == [1,1,2,3,3,3,5,5]
print('\n(passed!)')
