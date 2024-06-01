# Question: Check if two sentences are reversed

# English Video: https://www.youtube.com/watch?v=uX9-G8hJHak
# Tamil Video: https://www.youtube.com/watch?v=XIuZA3SS4vQ

# *** Approach 1: General FOR loop *** 
def Grow_With_Data(sentence1,sentence2):
    sentence1 = sentence1.split()
    sentence2 = sentence2.split()
    for indx, val in enumerate(sentence1):
        if sentence2[-(indx+1)] != val:
            return False
    return True
assert Grow_With_Data("This is a good example","example good a is This") == True
assert Grow_With_Data("Grow With Data","Data With Grow") == True
assert Grow_With_Data("2024 is awesome","Awesome is 2024") == False
print('Passed!')

# *** Approach 2: Using reversed() function 
def Grow_With_Data(sentence1,sentence2):
    new_sentence2 = ' '.join(list(reversed(sentence2.split())))
    return sentence1 == new_sentence2
assert Grow_With_Data("This is a good example","example good a is This") == True
assert Grow_With_Data("Grow With Data","Data With Grow") == True
assert Grow_With_Data("2024 is awesome","Awesome is 2024") == False
print('Passed!')
