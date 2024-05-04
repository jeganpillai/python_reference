# Question: Find the total number of lines and width of last line in pixel

# English Video: https://www.youtube.com/watch?v=s9nSJSgGCxE
# Tamil Video: https://www.youtube.com/watch?v=aTm-mX1infI

# Approach 1: Simple approach to find the value 
def Grow_With_Data(widths, s):
    lines = 1
    cnt = 0
    for i in s:
        if cnt + widths[ord(i) - ord('a')] > 100:
            lines += 1
            cnt = widths[ord(i) - ord('a')]
        else:
            cnt += widths[ord(i) - ord('a')]
    return [lines, cnt]
assert Grow_With_Data([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'abcdefghijklmnopqrstuvwxyz') == [3,60]
assert Grow_With_Data([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'bbbcccdddaaa') == [2,4]
print('Passed!')

# Approach 2: Simplified version 
def Grow_With_Data(widths, s):
    lines = 1
    cnt = 0
    for i in s:
        chk = ord(i) - ord('a')
        if cnt + widths[chk] > 100:
            lines += 1
            cnt = widths[chk]
        else:
            cnt += widths[chk]
    return [lines, cnt]
assert Grow_With_Data([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'abcdefghijklmnopqrstuvwxyz') == [3,60]
assert Grow_With_Data([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'bbbcccdddaaa') == [2,4]
print('Passed!')
