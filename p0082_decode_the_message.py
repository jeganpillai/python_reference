# Question: Decode a message

# English Video: https://www.youtube.com/watch?v=-aPTMm-JM7c
# Tamil Video: 

-- Approach 1: Basic looping logic
def Grow_With_Data(key, message):
    dict_key = {}
    cnt = 0
    for val in key:
        if val not in dict_key and not val == ' ':
            dict_key[val] = chr(97 + cnt)
            cnt += 1
    result = []
    for m in message:
        if m == ' ':
            result.append(m)
        else:
            result.append(dict_key[m])
    return ''.join(result)
assert Grow_With_Data('thequickbrownfxjmpsvlazydg', 'vkbs bs t suepuv') == 'this is a secret'
assert Grow_With_Data('eljuxhpwnyrdgtqkviszcfmabo','zwx hnfx lqantp mnoeius ycgk vcnjrdb') == 'the five boxing wizards jump quickly'
print('Passed!')


-- Approach 2: Smarter coding 
def Grow_With_Data(key, message):
    dict_key = {}
    cnt = 0
    for val in key:
        if val not in dict_key and not val == ' ':
            dict_key[val] = chr(97 + cnt)
            cnt += 1
    result = []
    for m in message:
        result.append(m if m == ' ' else dict_key[m])
    return ''.join(result)
assert Grow_With_Data('thequickbrownfxjmpsvlazydg', 'vkbs bs t suepuv') == 'this is a secret'
assert Grow_With_Data('eljuxhpwnyrdgtqkviszcfmabo','zwx hnfx lqantp mnoeius ycgk vcnjrdb') == 'the five boxing wizards jump quickly'
print('Passed!')
