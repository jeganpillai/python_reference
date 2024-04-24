# Question: Perform Arithmetic Operation and report final value of input variable

# English Video: 
# Tamil Video: 

# Approach 1: Using OR function 
def Grow_With_Data(operations):
    result = 0 
    for val in operations:
        if val == '--X' or val == 'X--': 
            result -= 1
        else:
            result += 1
    return result
assert Grow_With_Data(["--X","X++","X++"]) == 1
assert Grow_With_Data(["++X","++X","X++"]) == 3
assert Grow_With_Data(["X++","++X","--X","X--"]) == 0
print('Passes!')

# Approach 2: Using IN function 
def Grow_With_Data(operations):
    result = 0 
    for val in operations:
        if val in ('--X','X--'): 
            result -= 1
        else:
            result += 1
    return result
assert Grow_With_Data(["--X","X++","X++"]) == 1
assert Grow_With_Data(["++X","++X","X++"]) == 3
assert Grow_With_Data(["X++","++X","--X","X--"]) == 0
print('Passed!')

# Approach 3: Using IN function in reverse check 
def Grow_With_Data(operations):
    result = 0 
    for val in operations:
        if '--' in val:
            result -= 1
        else:
            result += 1
    return result
assert Grow_With_Data(["--X","X++","X++"]) == 1
assert Grow_With_Data(["++X","++X","X++"]) == 3
assert Grow_With_Data(["X++","++X","--X","X--"]) == 0
print('Passes!')

# Approach 4: Using Inbuilt function count()
def Grow_With_Data(operations):
    neg = operations.count('--X') + operations.count('X--')
    pos = operations.count('++X') + operations.count('X++')
    return pos - neg
assert Grow_With_Data(["--X","X++","X++"]) == 1
assert Grow_With_Data(["++X","++X","X++"]) == 3
assert Grow_With_Data(["X++","++X","--X","X--"]) == 0
print('Passes!')

# Approach 5: Using List comprehension 
operations = ["--X","X++","X++"]
def Grow_With_Data(operations):
    return sum([1 if val[0] == '+' or val[-1] == '+' else -1 for val in operations])
assert Grow_With_Data(["--X","X++","X++"]) == 1
assert Grow_With_Data(["++X","++X","X++"]) == 3
assert Grow_With_Data(["X++","++X","--X","X--"]) == 0
print('Passes!')
