# Question: Find the intersection of two arrays 

# English Video: https://www.youtube.com/watch?v=7JYcOcZlllY
# Tamil Video: https://www.youtube.com/watch?v=KvnYLbJuTA0

a1 = [1,3,4,7,11,107]
a2 = [2,3,11,19]

# Approach 1: General looping logic 
def Grow_With_Data(a1, a2):
    result = []
    for a in a1:
        if a in a2:
            result.append(a)
    return result
Grow_With_Data(a1, a2)

# Approach 2: Using Sort and compare elements 
def Grow_With_Data(a1, a2):
    a1 = sorted(a1)
    a2 = sorted(a2)
    result = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            result.append(a1[i])
            i += 1 
            j += 1 
        elif a1[i] < a2[j]:
            i += 1 
        else:
            j += 1
    return result
Grow_With_Data(a1, a2)

