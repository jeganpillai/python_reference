# Question: Reverse prefix of words 

# English Video: https://www.youtube.com/watch?v=XqAQZSMzeY0
# Tamil Video: https://www.youtube.com/watch?v=mgqrE-vs7SI

# Approach 1: Using find() and String Slicing 
def Grow_With_Data(word, ch):
    slice = word.find(ch)
    if slice == -1:
        return word
    else:
        return word[: word.find(ch) + 1][::-1]+ word[word.find(ch) + 1:]
assert Grow_With_Data('abcdefd', 'd') == 'dcbaefd'
assert Grow_With_Data('xyxzxe', 'z') == 'zxyxxe'
assert Grow_With_Data('abcd', 'z') == 'abcd'
print('Passed!')

# Approach 2: Using index() and reversed() Function
def Grow_With_Data(word, ch):
    if ch in word:
        pos = word.index(ch)
        return ''.join(list((reversed(word[: pos + 1])))) + word[pos + 1:]
    else:
        return word
        
assert Grow_With_Data('abcdefd', 'd') == 'dcbaefd'
assert Grow_With_Data('xyxzxe', 'z') == 'zxyxxe'
assert Grow_With_Data('abcd', 'z') == 'abcd'
print('Passed!')
