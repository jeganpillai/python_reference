# Question: Given an array of sorted integers without duplicates, and two indices, i and j. Write a function to calculate the number of missing integers between these two indices.

# looping logic 
src = [2,7,8,9,15]
i = 0
j = 1
def Grow_With_Data(src, i,j):
    target = []
    start = src[i]
    end = src[j]
    for k in range(start+1, end):
        target.append(k)
    print('The missing values are: ', target)
    return len(target)


# simple algorithm 
src = [2,7,8,9,15]
i = 0
j = 1
def Grow_With_Data(src, i,j):
    return src[j] - src[i] - 1

Grow_With_Data(src, i,j)

# practice format
def Grow_With_Data(src, i,j):
    return src[j] - src[i] - 1

assert Grow_With_Data([2,7,8,9,15],0,1) == 4 
assert Grow_With_Data([2,7,8,9,15],0,2) == 5 
assert Grow_With_Data([2,7,8,9,15],1,2) == 0
print('\n(Passed!)')

