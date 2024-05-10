# Question: Find the number of special characters in a given string.

# English Video: 
# Tamil Video: 

# Scenario 1: Consider only distinct pairs 
def count_special_letters(word):
    small_set = set()
    upper_set = set()
    cnt = 0
    for i in word:
        if i.islower():
            small_set.add(i)
    for j in word:
        if j.isupper() and j.lower() in small_set and not j in upper_set:
            cnt += 1
            upper_set.add(j)
    return cnt
assert count_special_letters("aaAbcBC") ==  3 
assert count_special_letters("abc") ==  0
assert count_special_letters("abBCab") ==  1 
assert count_special_letters("CCcCc") ==  1
assert count_special_letters("BBbab") == 1
print('Passed!')

# Scenario 2: Consider Duplicate pairs
def count_special_letters(word):
    small_set = []
    cnt = 0
    for i in word:
        if i.islower():
            small_set.append(i)
    for j in word:
        if j.isupper() and j.lower() in small_set:
            cnt += 1
            small_set.remove(j.lower())
    return cnt
assert count_special_letters("aaAbcBC") ==  3 
assert count_special_letters("abc") ==  0
assert count_special_letters("abBCab") ==  1 
assert count_special_letters("CCcCc") ==  2
assert count_special_letters("BBbab") == 2
print('Passed!')
