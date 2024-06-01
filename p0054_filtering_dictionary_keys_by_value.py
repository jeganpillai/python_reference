# Question: filtering dictionary keys by value

# English Video: https://www.youtube.com/watch?v=13cHR4ucRYg
# Tamil Video: https://www.youtube.com/watch?v=VfpZVSp5avU

# *** Approach 1: Simple looping option *** 
d = {'Apple':'Fruit', 'Strawberry':'Fruit', 'Peas':'Veggie', 'Tomato':'Veggie', 'Lettuce':'Veggie'}
value = 'Fruit'
def Grow_With_Data(d, value):
    result = []
    for key, val in d.items():
        if val == value:
            result.append(key)
    return result
Grow_With_Data(d, value)

# *** Approach 2: Using List Comprehension process *** 
d = {'Apple':'Fruit', 'Strawberry':'Fruit', 'Peas':'Veggie', 'Tomato':'Veggie', 'Lettuce':'Veggie'}
value = 'Fruit'
def Grow_With_Data(d, value):
    result = [key for key, val in d.items() if val == value]
    return result
Grow_With_Data(d, value)
