# Question: Return missing balanced numbers
# Video: https://www.youtube.com/watch?v=w0Pk2SbfN2g

# Approach 1: simple FOR loop 
def return_missing_balanced_numbers(input):
  # Write your code here
  d = {}
  for i in input:
    d[i] = d.get(i,0) + 1 
  max_val = max(d.values())
  result = {}
  for indx, val in d.items():
    if not val == max_val:
      result[indx] = max_val - val
  
  return result

# Approach 2: simplified version
def Grow_With_Data(elements):
    d = {}
    for i in elements:
        d[i] = d.get(i,0) + 1 
    max_val = max(d.values())
    
    result = {element:max_val - count for element, count in d.items() if not max_val == count}
    return result

assert Grow_With_Data(["a", "b", "abc", "c", "a"]) == {"b":1, "abc":1, "c":1}
assert Grow_With_Data([1,3,4,2,1,4,1]) == {2:2, 3:2, 4:1}
assert Grow_With_Data([4,5,11,5,6,11]) == {4:1,6:1}
print("\nPassed!")
