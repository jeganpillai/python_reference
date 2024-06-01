# Question: Find the maximum number of words that appear in a single sentence

# English Video: https://www.youtube.com/watch?v=ayVaaMFl9F8
# Tamil Video: https://www.youtube.com/watch?v=XiB_qgAUbFI

# Approach 1: Using Brute Force method 
def Grow_With_Data(sentences):
    max_length = 0
    for sentence in sentences:
        cnt = 0
        for word in sentence.split():
            cnt += 1
        if cnt > max_length:
            max_length = cnt
    return max_length
assert Grow_With_Data(["Ram Rahim and Antony love Grow With Data","i think so too","this is great thanks very much"]) == 8
assert Grow_With_Data(["please wait", "continue to fight", "continue to win"]) == 3
print('Passed!')

# Approach 2: Simplified FOR loop and IF filter 
def Grow_With_Data(sentences):
    max_len = 0
    for sentence in sentences:
        if len(sentence.split()) > max_len:
            max_len = len(sentence.split())
    return max_len
assert Grow_With_Data(["Ram Rahim and Antony love Grow With Data","i think so too","this is great thanks very much"]) == 8
assert Grow_With_Data(["please wait", "continue to fight", "continue to win"]) == 3
print('Passed!')

# Approach 3: Simplify further using FOR loop and MAX() function 
def Grow_With_Data(sentences):
    max_len = 0
    for sentence in sentences:
        max_len = max(max_len,len(sentence.split()))
    return max_len
assert Grow_With_Data(["Ram Rahim and Antony love Grow With Data","i think so too","this is great thanks very much"]) == 8
assert Grow_With_Data(["please wait", "continue to fight", "continue to win"]) == 3
print('Passed!')

# Approach 4: List comprehension with split the sentence and count the words 
def Grow_With_Data(sentences):
    return max([len(i.split()) for i in sentences])
assert Grow_With_Data(["Ram Rahim and Antony love Grow With Data","i think so too","this is great thanks very much"]) == 8
assert Grow_With_Data(["please wait", "continue to fight", "continue to win"]) == 3
print('Passed!')

# Approach 5: List comprehension using space count 
def Grow_With_Data(sentences):
    return max([i.count(' ')+1 for i in sentences])
assert Grow_With_Data(["Ram Rahim and Antony love Grow With Data","i think so too","this is great thanks very much"]) == 8
assert Grow_With_Data(["please wait", "continue to fight", "continue to win"]) == 3
print('Passed!')
