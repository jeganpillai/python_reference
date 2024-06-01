# Question: Find the first smallest and largest words in the string.

# English Video: https://www.youtube.com/watch?v=ICjtXh_XonA
# Tamil Video: https://www.youtube.com/watch?v=hLm2vd_uxgA

# *** Approach 1: Using Variables and Check *** 
def Grow_With_Data(input_string):
    words = input_string.split()
    if not words:
        return {'smallest': None, 'largest':None}
    
    smallest = words[0]
    largest = words[0]
    
    for word in words:
        if len(word) < len(smallest):
            smallest = word
        if len(word) > len(largest):
            largest = word
    return {'smallest': smallest, 'largest': largest}

assert Grow_With_Data("This is a test string") == {'smallest': 'a', 'largest': 'string'}
assert Grow_With_Data("") == {'smallest': None, 'largest': None}
assert Grow_With_Data("the quick brown fox jumps over the lazy dog") == {'smallest': 'the', 'largest': 'quick'}
assert Grow_With_Data("Facebook connects the world") ==  {'smallest': 'the', 'largest': 'Facebook'}
assert Grow_With_Data("There are some great examples of social good") == {'smallest': 'of', 'largest': 'examples'}
print('Passed!')


# *** Approach 2: Using Dictionary and Check *** 
def Grow_With_Data(input_string):
    words = input_string.split()
    if not words:
        return {'smallest': None, 'largest': None}
    
    result = {'smallest': words[0], 'largest': words[0]}
    
    for word in words:
        if len(word) < len(result['smallest']):
            result['smallest'] = word
        if len(word) > len(result['largest']):
            result['largest'] = word
    return result

assert Grow_With_Data("This is a test string") == {'smallest': 'a', 'largest': 'string'}
assert Grow_With_Data("") == {'smallest': None, 'largest': None}
assert Grow_With_Data("the quick brown fox jumps over the lazy dog") == {'smallest': 'the', 'largest': 'quick'}
assert Grow_With_Data("Facebook connects the world") ==  {'smallest': 'the', 'largest': 'Facebook'}
assert Grow_With_Data("There are some great examples of social good") == {'smallest': 'of', 'largest': 'examples'}
print('Passed!')
