# Question: Find the product of array except self
# Video: https://www.youtube.com/watch?v=u9rIXMfFlf8

# Approach 0: (Wrong code) Wrong code for arrays with Zero element 
def Grow_With_Data(N):
    total_product = 1 
    for i in N:
        total_product *= i
    result = []
    for num in N:
        result.append(round(total_product/num))
    return result

assert Grow_With_Data([5, 6, 10]) == [60, 50, 30]
assert Grow_With_Data([1, 2, 3, 4]) == [24, 12, 8, 6]
# assert Grow_With_Data([5, 6, 10, 0]) == [0, 0, 0, 300] # fails 
print('\n(Passed!)')

# Approach 1: Split and find product 
def Grow_With_Data(N):
    res = []
    for i in range(len(N)):
        sub_N = N[:i] + N[i+1:]
        a = 1 
        for j in sub_N:
            a *= j
        res.append(a)
    return res
assert Grow_With_Data([5, 6, 10]) == [60, 50, 30]
assert Grow_With_Data([1,2,3,4]) == [24,12,8,6]
assert Grow_With_Data([5, 6, 10, 0]) == [0, 0, 0, 300]
print('Passed!')

# Approach 2: Code with time complexity O(n) 
def Grow_With_Data(N):
    length = len(N)
    L, R, result = [0] * length, [0] * length, [0] * length
    L[0] = 1
    for i in range(1, length):
        L[i] = L[i-1] * N[i-1]
    print('First set: ', L)
    R[length-1] = 1
    for i in reversed(range(length - 1)):
        R[i] = R[i+1] * N[i+1]
    print('Second set: ', R)
    for i in range(length):
        result[i] = L[i] * R[i]
    return result
assert Grow_With_Data([5, 6, 10]) == [60, 50, 30]
assert Grow_With_Data([1,2,3,4]) == [24,12,8,6]
assert Grow_With_Data([5, 6, 10, 0]) == [0, 0, 0, 300]
print('Passed!')

# Approach 3: Finetune approach-3 with one array and one integer variable 
def Grow_With_Data(N):
    length = len(N)
    result = [0] * length
    result[0] = 1
    for i in range(1, length):
        result[i] = result[i-1] * N[i-1]
    # print('First set: ', answer)

    R = 1
    for i in reversed(range(length)):
        result[i] = result[i] * R
        R *= N[i]
    return result
assert Grow_With_Data([5, 6, 10]) == [60, 50, 30]
assert Grow_With_Data([1,2,3,4]) == [24,12,8,6]
print('Passed!')
