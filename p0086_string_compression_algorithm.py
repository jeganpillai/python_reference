# Question: String Compression Algorithm

# English Video: 
# Tamil Video: 

# Scope 1: Concatenate the Number of Occurrences Followed by the Character
word = 'abcde'           # '1a1b1c1d1e'
def Grow_With_Data(word):
    d = {}
    for i in word:
        d[i] = d.get(i,0) + 1
    
    output = ''
    for key, val in d.items():
        output += str(val)+key
    return output
Grow_With_Data(word)

# scope 2: Limit Repetitions to at Most 9 Times
word = 'aaaaaaaaaaaaaabb'    # '9a5a2b'
def Grow_With_Data(word):
    d = {}
    for i in word:
        d[i] = d.get(i,0) + 1
    
    output = ''
    for key, val in d.items():
        while val > 0:
            output += str(min(val,9))+key
            val -= 9       
    return output

# scope 3: Maintain the Order of Characters
word = 'mrm'                  # '1m1r1m'
def Grow_With_Data(word):
    result = ''
    i = 0
    while i < len(word):
        c = word[i]
        count = 0
        while i < len(word) and word[i] == c and count < 9:
            count += 1
            i += 1
        result += str(count) + c
    return result
assert Grow_With_Data('aaaaaaaaaaaaaabb') == '9a5a2b'
assert Grow_With_Data('abcde') == '1a1b1c1d1e'
assert Grow_With_Data('mrm') == '1m1r1m'
print('Passed!')
