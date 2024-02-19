# Question: Return key with smallest value.
# Video: https://www.youtube.com/watch?v=tnCuUM8DZog

# General looping logic: 
def Grow_With_Data(inputDict, n):
    pos_val = sorted(list(set(inputDict.values())))
    if n == 0 or n > len(pos_val):
        return None
    pos_val = pos_val[n-1]

    result = []
    for key, val in inputDict.items():
        if val == pos_val:
            result.append(key)
    return sorted(result)[0]
Grow_With_Data(inputDict, n)

# simpler version
def Grow_With_Data(inputDict, n):
    if n <= 0 or len(sorted(list(set(inputDict.values())))) < n:
        return None
    return sorted(inputDict.items(), key = lambda x: (x[1], x[0]))[n-1][0]
assert Grow_With_Data({'laptop': 999,'smartphone': 999,'smart tv': 500,'smart watch': 300,'smart home': 9999999}, 2) == 'smart tv' 
assert Grow_With_Data({'a': 10,'b': 20}, 0) == None
assert Grow_With_Data({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}, 6) == None
assert Grow_With_Data({'a': 10,'b': 20,'c': 3,'d': 2,'e': 9}, 1) == 'd'
print('Passed!')
