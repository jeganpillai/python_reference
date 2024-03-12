# Question: Check if the sentence is pangram.
# Video: https://www.youtube.com/watch?v=rSRkiDKfbNY

*** Approach 1: convert to list and set then compare the length *** 
def Grow_With_Data(sentence):
    return len(set(list(sentence))) == 26

*** Approach 2: convert directly to set and then compare the length *** 
def Grow_With_Data(sentence):
    return len(set(sentence)) == 26

*** Approach 3: using dictionary *** 
def Grow_With_Data(sentence):
    d = {}
    for i in sentence:
        d[i] = d.get(i,0) + 1
    return len(d) == 26

*** Approach 4: using list and loop *** 
def Grow_With_Data(sentence):
    result = []
    for i in sentence:
        if not i in result:
            result.append(i)
    return len(result) == 26

*** Approach 5: sorted list option *** 
def Grow_With_Data(sentence):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = sorted(list(set(sentence)))
    return s == alpha
