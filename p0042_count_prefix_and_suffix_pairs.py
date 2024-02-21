# Question: count prefix and suffix pairs in a given array
# Video: https://www.youtube.com/watch?v=lAoJU-Nloi8

# Approach 1: Basic code 
def Grow_With_Data(words):
    result = 0 
    for indx, word in enumerate(words):
        for sub_indx, sub_word in enumerate(words):
            if indx < sub_indx:
                if len(word) > len(sub_word):
                    continue 
                if word == sub_word[:len(word)] and word == sub_word[-len(word):]:
                    result += 1 
    return result
assert Grow_With_Data(["pa","papa","ma","mama"]) == 2
assert Grow_With_Data(["a","aba","ababa","aa"]) == 4
assert Grow_With_Data(["abab","ab"]) == 0
assert Grow_With_Data(["aba", "ababa"]) == 1
print('Passed!')

# Approach 2: Use sub array for the second loop 
def Grow_With_Data(words):
    result = 0 
    for indx, word in enumerate(words):
        for sub_indx, sub_word in enumerate(words[indx+1:]):
            if len(word) > len(sub_word):
                continue 
            if word == sub_word[:len(word)] and word == sub_word[-len(word):]:
                result += 1 
    return result

assert Grow_With_Data(["pa","papa","ma","mama"]) == 2
assert Grow_With_Data(["a","aba","ababa","aa"]) == 4
assert Grow_With_Data(["abab","ab"]) == 0
assert Grow_With_Data(["aba", "ababa"]) == 1
print('Passed!')

# Approach 3: use startswith() and endswith() functions 
def Grow_With_Data(words):
    result = 0 
    for indx, word in enumerate(words):
        for sub_indx, sub_word in enumerate(words[indx+1:]):
            if sub_word.startswith(word) and sub_word.endswith(word):
                result += 1 
    return result

assert Grow_With_Data(["pa","papa","ma","mama"]) == 2
assert Grow_With_Data(["a","aba","ababa","aa"]) == 4
assert Grow_With_Data(["abab","ab"]) == 0
assert Grow_With_Data(["aba", "ababa"]) == 1
print('Passed!')
