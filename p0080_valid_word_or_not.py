# Question: Find the given word is valid or not

# English Video: https://www.youtube.com/watch?v=N9hfhcGMJUY
# Tamil Video: https://www.youtube.com/watch?v=6IjqzM2Gt5U

# Approach 1: Check individual condition
def Grow_With_Data(word):
    if len(word) < 3:
        return False
    if not word.isalnum():
        return False
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if not any(char.lower() in vowels for char in word):
        return False
    consonants = set('bcdfghjklmnpqrstvwxyz')
    if not any(char.lower() in consonants for char in word):
        return False
    return True
assert Grow_With_Data('234Adas') == True
assert Grow_With_Data('b3') == False
assert Grow_With_Data('a3$e') == False
assert Grow_With_Data('AhI') == True
assert Grow_With_Data('UuE6') == False
print('Passed!') 

# Approach 2: General looping logic 
def Grow_With_Data(word):
    count = 0
    has_vowel = False
    has_consonant = False
    vowels = ('a','e','i','o','u')
    
    for chr in word:
        if chr.isalnum():
            count += 1
            if chr.lower() in vowels:
                has_vowel = True
            elif chr.isalpha():
                has_consonant = True
        else:
            return False
    print(count, has_vowel , has_consonant)
    return count >= 3 and has_vowel and has_consonant
assert Grow_With_Data('234Adas') == True
assert Grow_With_Data('b3') == False
assert Grow_With_Data('a3$e') == False
assert Grow_With_Data('AhI') == True
assert Grow_With_Data('UuE6') == False
print('Passed!') 

# Approach 3: Using regular expression 
import re
def Grow_With_Data(word):
    vowel_regex = r'[aeiouAEIOU]'
    consonant_regex = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
    alphanumeric_regex = r'[a-zA-Z0-9]'

    has_vowel = re.search(vowel_regex, word) is not None
    has_consonant = re.search(consonant_regex, word) is not None
    has_enough_chars = len(re.findall(alphanumeric_regex, word)) >= 3

    return has_vowel and has_consonant and has_enough_chars
assert Grow_With_Data('234Adas') == True
assert Grow_With_Data('b3') == False
assert Grow_With_Data('a3$e') == False
assert Grow_With_Data('AhI') == True
assert Grow_With_Data('UuE6') == False
print('Passed!') 

# Approach4: Using regular expression compile
import re

def is_valid_word(word):
    if len(word) < 3:
        return False
    
    alphanumeric_pattern = re.compile(r'^[a-zA-Z0-9]+$')
    if not alphanumeric_pattern.match(word):
        return False
    
    vowel_pattern = re.compile(r'[aeiouAEIOU]')
    if not vowel_pattern.search(word):
        return False
    
    consonant_pattern = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    if not consonant_pattern.search(word):
        return False
    
    return True
