# Question: Identifying Missing and Repeated Values in an Array
# Video: https://www.youtube.com/watch?v=Oa7TWJAQcpc

# Approach 1: Sort and Analyze
def Grow_With_Data(grid):
    grid = sorted([j for g in grid for j in g])
    seen =set()
    repeating = None
    missing = None 

    for i in range(1, len(grid)+1):
        actual = grid[i-1]  
        if actual in seen:
            repeating = actual
        seen.add(actual)

        if not i in grid:
            missing = i
    return [repeating,missing]
assert Grow_With_Data([[2,2],[3,4]]) == [2,1]
assert Grow_With_Data([[1,3],[2,2]]) == [2,4]
assert Grow_With_Data([[9,1,7],[8,9,2],[3,4,6]]) == [9,5]
assert Grow_With_Data([[1,1],[3,2]]) == [1,4]
print('\n Pass')

# Approach 2: Leveraging Arithmetic Series Sum
def Grow_With_Data(grid):
    seen = set()
    repeating = 0
    
    actual_sum = 0
    n = 0
    
    for lst in grid:
        for num in lst:
            if num in seen:
                repeating = num
            seen.add(num)
            actual_sum += num 
            n += 1 
    expected_sum = n * (n + 1)//2
    missing = expected_sum - actual_sum + repeating
    return [repeating, missing]
assert Grow_With_Data([[2,2],[3,4]]) == [2,1]
assert Grow_With_Data([[1,3],[2,2]]) == [2,4]
assert Grow_With_Data([[9,1,7],[8,9,2],[3,4,6]]) == [9,5]
assert Grow_With_Data([[1,1],[3,2]]) == [1,4]
print('\n Pass')
