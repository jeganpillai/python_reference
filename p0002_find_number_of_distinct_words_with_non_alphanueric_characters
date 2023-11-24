# brute force method 
source = "You have to find the number of words in this sentence, and you' going to print the number of words in the sentence."
def helper(source):
    words = source.lower().split()
    target = []
    for word in words:
        chk = []
        for char in word:
            if char.isalnum():
                chk.append(char)
        # print(''.join(chk))
        target.append(''.join(chk))
    return len(set(target))
helper(source)

# better approach 
source1 = "You have to find the number of words in this sentence, and you' going to print the number of words in the sentence."
source2 = "You can test you' python skill" 
source3 = " "
def helper(source):
    # print(source, ' and ', len(set([''.join(char for char in word if char.isalnum()) for word in source.lower().split() ])))
    return len(set([''.join(char for char in word.strip() if char.isalnum()) for word in source.lower().split() ]))

assert helper(source1) == 14
assert helper(source2) == 5
assert helper(source3) == 0
print("\n Pass")
