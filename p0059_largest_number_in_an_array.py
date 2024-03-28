# Question: Find the largest number in an array
# English Video: 
# Tamil Video: 

# Approach 1: General FOR loop O(n)
def Grow_With_Data(numbers):
    result = float("-inf")
    for number in numbers:
        if number > result:
            result = number 
    return result
assert Grow_With_Data([100.4, 900.2, 900.3, -4, 60.2]) == 900.3
assert Grow_With_Data([-50, -60, -70]) == -50
print('Passed!')

# Approach 2: Using SORTED() function O(n log n)
def Grow_With_Data(numbers):
    return sorted(numbers)[-1] if numbers else []
assert Grow_With_Data([100.4, 900.2, 900.3, -4, 60.2]) == 900.3
assert Grow_With_Data([-50, -60, -70]) == -50
print('Passed!')

# Approach 3: Using Reversed SORTED() function O(n log n)
def Grow_With_Data(numbers):
    return sorted(numbers, reverse = True)[0] if numbers else []
assert Grow_With_Data([100.4, 900.2, 900.3, -4, 60.2]) == 900.3
assert Grow_With_Data([-50, -60, -70]) == -50
assert Grow_With_Data([]) == []
print('Passed!')

# Approach 4: Using MAX() function O(n)
def Grow_With_Data(numbers):
    return max(numbers) if numbers else []
assert Grow_With_Data([100.4, 900.2, 900.3, -4, 60.2]) == 900.3
assert Grow_With_Data([-50, -60, -70]) == -50
assert Grow_With_Data([]) == []
print('Passed!')
