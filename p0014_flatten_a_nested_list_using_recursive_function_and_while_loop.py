# Question: Given a nested list, how to convert it into a simple flatten list using recursive function and while loop

# approach 1: WHILE loop 
nested_lst = [1, 2, [3, 4, [5, 6]], 7]
def Grow_With_Data(nested_lst):
    flattened_lst = []
    stack = [nested_lst]
    while stack:
        current = stack.pop()
        # print('Current val: ', current)
        for val in reversed(current):
            # print('Value is: ', val)
            if type(val) == list:
                stack.append(val)
            else:
                flattened_lst.append(val)
    return flattened_lst
Grow_With_Data(nested_lst)


# approach 2: nested loop
nested_lst = [1, 2, [3, 4, [5, 6]], 7]
def Grow_With_Data(nested_lst):
    flattened_lst = []
    def helper(nested_lst):
        for val in nested_lst:
            if type(val) == list:
                helper(val)
            else:
                flattened_lst.append(val)
    helper(nested_lst)
    return flattened_lst
Grow_With_Data(nested_lst)

# practice work 
def Grow_With_Data(nested_lst):
    flattened_lst = []
    def helper(nested_lst):
        for val in nested_lst:
            if type(val) == list:
                helper(val)
            else:
                flattened_lst.append(val)
    helper(nested_lst)
    return flattened_lst

def cmp_lst(l1,l2):
    return sorted(l1) == sorted(l2)

assert cmp_lst(Grow_With_Data([1, 2, [3, 4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7]) == True
assert cmp_lst(Grow_With_Data([[],[[]]]) , []) == True
assert cmp_lst(Grow_With_Data([[[1]]]) , [1]) == True
assert cmp_lst(Grow_With_Data([[100, 99], [1, 2, 3], []]) , [1, 2, 3, 99, 100]) == True
print("\n(Passed!)")
