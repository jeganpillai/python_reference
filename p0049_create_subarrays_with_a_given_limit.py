# Question: create subarrays with a given limit
# Video: https://www.youtube.com/watch?v=ItHn2pW0KE4
# Approach 1: basic FOR loop 
arr = [1,2,3,4,5]; limit = 2
arr = [1,2,3,4,5,6,7,8,9]; limit = 3
arr = [1,2,3]; limit = 6
def Grow_With_Data(arr, limit):
    cnt = 0
    result = []
    chk = []
    
    for i in arr:
        if cnt < limit:
            chk.append(i)
            cnt += 1 
        else:
            result.append(chk)
            chk = [i]
            cnt = 1
    if chk:
        result.append(chk)
    return result
assert Grow_With_Data([1,2,3,4,5], 2) ==  [[1, 2], [3, 4], [5]]
assert Grow_With_Data([1,2,3,4,5,6,7,8,9], 3) ==  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert Grow_With_Data([1,2,3], 6) ==  [[1,2,3]]
print('Passed!')


# Approach 2: simplified FOR loop 
def Grow_With_Data(arr, limit):
    result = []
    chk = []
    for i in arr:
        chk.append(i)
        if len(chk) == limit:
            result.append(chk)
            chk = []
    if chk:
        result.append(chk)
    print(result)
    return result
assert Grow_With_Data([1,2,3,4,5], 2) ==  [[1, 2], [3, 4], [5]]
assert Grow_With_Data([1,2,3,4,5,6,7,8,9], 3) ==  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert Grow_With_Data([1,2,3], 6) ==  [[1,2,3]]
print('Passed!')

# Approach 3: using RANGE() function 
arr = [1,2,3,4,5]
limit = 2
def Grow_With_Data(arr, limit):
    result = []
    for i in range(0,len(arr),limit):
        result.append(arr[i:i+limit])
    return result
assert Grow_With_Data([1,2,3,4,5], 2) ==  [[1, 2], [3, 4], [5]]
assert Grow_With_Data([1,2,3,4,5,6,7,8,9], 3) ==  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert Grow_With_Data([1,2,3], 6) ==  [[1,2,3]]
print('Passed!')

# One liner 
def Grow_With_Data(arr, limit):
    return [arr[i:i+limit] for i in range(0,len(arr),limit)]
