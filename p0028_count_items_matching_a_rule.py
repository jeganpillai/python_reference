# Question: Count items matching a rule
# Video: https://www.youtube.com/watch?v=VKDVd8U40_Q

def Grow_With_Data(items, ruleKey, ruleValue):
    item_dict = {'type': 0, 'color':1, 'name':2}
    indx = item_dict[ruleKey]
    cnt = 0
    for item in items:
        if item[indx] == ruleValue:
            cnt += 1 
    return cnt
assert Grow_With_Data([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver") == 1
assert Grow_With_Data([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone") == 2
print('\n Pass')
