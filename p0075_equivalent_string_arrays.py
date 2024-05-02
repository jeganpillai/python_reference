-- Question: Find the three Longest Incoming and Outgoing Calls

-- English Video: 
-- Tamil Video: 

# Approach 1: Brute force method of Iterative Comparison with Concatenation
def Grow_With_Data(word1, word2):
    chk1 = ''
    chk2 = ''
    for char in word1:
        chk1 += char
    
    for char in word2:
        chk2 += char
    min_loop = min(len(chk1), len(chk2))
    for i in range(min_loop):
        if chk1[i] != chk2[i]:
            return False
    return True
assert Grow_With_Data(["ab", "c", ], ["a", "bc" ] ) == True 
assert Grow_With_Data(["a", "cb"], ["ab", "c" ]) == False
assert Grow_With_Data(["abc", "d", "defg"], ["abcddefg"])  == True
print('Passed!')

# Approach 2: Utilizing Python's join() Function for Concatenation
def Grow_With_Data(word1, word2):
    chk1 = ''.join(word1)
    chk2 = ''.join(word2)
    print(chk1, chk2)
    if chk1 != chk2:
        return False
    return True
assert Grow_with_Data(["ab", "c"],["a", "bc" ]) == True
assert Grow_with_Data(["a", "cb"],["ab", "c" ]) == False
assert Grow_with_Data(["abc", "d", "defg"],["abcddefg"]) == True
print('Passed!')

# Approach 3: Concise Comparison Using Built-in Functions
def Grow_With_Data(word1, word2):
    return ''.join(word1) == ''.join(word2)
assert Grow_with_Data(["ab", "c"],["a", "bc" ]) == True
assert Grow_with_Data(["a", "cb"],["ab", "c" ]) == False
assert Grow_with_Data(["abc", "d", "defg"],["abcddefg"]) == True
print('Passed!')
