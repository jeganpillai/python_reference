# Question 1: we are given a list of numers, find if sum of any two numbers in the list gives the target value
lst = [1,2,3,4,5,6,7] 
tgt = 6
def grow_with_data(lst, tgt):
    output = []
    for i in range(len(lst)):
        if tgt - lst[i] in lst[i+1:]:
            output.append((lst[i], tgt-lst[i]))
    return output
grow_with_data(lst, tgt)

# Question 2: we are given a list of numers, find if sum of any two numbers in the list gives the target index (not the values)
def grow_with_data(lst, tgt):
    output = []
    for i in range(len(lst)):
        if tgt - lst[i] in lst[i+1:]:
            output.append((i, lst[i+1:].index(tgt-lst[i])+i+1))
    return output
grow_with_data(lst, tgt)

# write it in sigle return function 
def grow_with_data(lst, tgt):
    return [(i, lst[i+1:].index(tgt-lst[i])+i+1) for i in range(len(lst)) if tgt - lst[i] in lst[i+1:]]
grow_with_data(lst, tgt)
