# Question: Ssort the characters by frequency
# Video: https://www.youtube.com/watch?v=PP4GgiBTpNQ

# Approach 1: Basic Looping 
def Grow_With_Data(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    result = ''
    for items in sorted(d.items(), key = lambda item: [item[1],item[0]], reverse=True):
        key = items[0]
        value = items[1]
        # print(items, key, value, key*value)
        result += key*value
    return result
Grow_With_Data('tree') == 'eetr'
Grow_With_Data('cccaaa') == 'aaaccc'
Grow_With_Data('Aabb') == 'bbAa'
print('\n Passed!')


# Approach 2: If we want to do the FOR loop in a better way, lets try it
def Grow_With_Data(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    # sorted_char = sorted(d.items(), key = lambda item: [item[1],item[0]], reverse=True)
    return ''.join(char * count for char, count in sorted(d.items(), key = lambda item: [item[1],item[0]], reverse=True))
Grow_With_Data('tree') == 'eetr'
Grow_With_Data('cccaaa') == 'aaaccc'
Grow_With_Data('Aabb') == 'bbAa'
print('\n Passed!')
