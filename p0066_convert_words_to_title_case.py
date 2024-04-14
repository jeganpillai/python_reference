# Question: Convert Words to Title Case

# English Video: https://www.youtube.com/watch?v=nbaqzc509Tw
# Tamil Video: https://www.youtube.com/watch?v=QDakRDgerKg

# Approach 1: Brute Force method using FOR loop
def Grow_With_Data(s):
    output = ''
    capitalize_next = True

    for char in s:
        if capitalize_next:
            output += char.upper()
        else:
            output += char.lower()
        if char == ' ':
            capitalize_next = True
        else:
            capitalize_next = False
    return output
assert Grow_With_Data('ITS our GROW wiTH data') == 'Its Our Grow With Data'
assert Grow_With_Data('ALWayS space FOR Improvement') == 'Always Space For Improvement'
print('Passed!')

# Approach 2: Simplified version and smart coding 
def Grow_With_Data(s):
    output = ''
    capitalize_next = True

    for char in s:
        if capitalize_next:
            output += char.upper()
        else:
            output += char.lower()
        capitalize_next = char == ' '
    return output
assert Grow_With_Data('ITS our GROW wiTH data') == 'Its Our Grow With Data'
assert Grow_With_Data('ALWayS space FOR Improvement') == 'Always Space For Improvement'
print('Passed!')

# Approach 3: Simplify code using list comprehension 
def Grow_With_Data(s):
    return ' '.join([char.capitalize() for char in s.split()])
assert Grow_With_Data('ITS our GROW wiTH data') == 'Its Our Grow With Data'
assert Grow_With_Data('ALWayS space FOR Improvement') == 'Always Space For Improvement'
print('Passed!')

# Approach 4: Using inbuilt function for strings 
def Grow_With_Data(s):
    return s.title()
assert Grow_With_Data('ITS our GROW wiTH data') == 'Its Our Grow With Data'
assert Grow_With_Data('ALWayS space FOR Improvement') == 'Always Space For Improvement'
print('Passed!')


