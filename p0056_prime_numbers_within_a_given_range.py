# Question: create a new list that contains all the prime numbers from the given list that are less than the threshold given.
# Video: https://www.youtube.com/watch?v=_ZxJ6Hf187c

# Approach 1: Simple Looping Logic
def Grow_With_Data(input_list, num):
    result = []
    for i in input_list:
        if i < 2 or i >= num:
            continue
        chk = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                chk = False
                break
        if chk:
            result.append(i)
    print(result)
    return result
assert sorted(Grow_With_Data([2,3,4,6,7,8],1)) == []
assert sorted(Grow_With_Data([1,2,3,4,5,6,7,8,9,10],5)) == [2,3]
assert sorted(Grow_With_Data([1,2,3,4,6,7,11,14,18,37,50,66,67],100)) == [2,3,7,11,37,67]
print('Passed!')

# Approach 2: Creating a Prime Number Validation Function
def Grow_With_Data(input_list, num):
    def is_prime(n):
        if n < 2 or n >= num:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    result = []
    for i in input_list:
        if is_prime(i):
            result.append(i)
    return result
assert sorted(Grow_With_Data([2,3,4,6,7,8],1)) == []
assert sorted(Grow_With_Data([1,2,3,4,5,6,7,8,9,10],5)) == [2,3]
assert sorted(Grow_With_Data([1,2,3,4,6,7,11,14,18,37,50,66,67],100)) == [2,3,7,11,37,67]
print('Passed!')

# Approach 3: Leveraging List Comprehension
def Grow_With_Data(input_list, num):
    def is_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    result = [i for i in input_list if is_prime(i) and i > 1 and i < num]
    return result
assert sorted(Grow_With_Data([2,3,4,6,7,8],1)) == []
assert sorted(Grow_With_Data([1,2,3,4,5,6,7,8,9,10],5)) == [2,3]
assert sorted(Grow_With_Data([1,2,3,4,6,7,11,14,18,37,50,66,67],100)) == [2,3,7,11,37,67]
print('Passed!')
