# Question : count the unique messages to from the country.
# Video: https://www.youtube.com/watch?v=OnacKSU2As0 

# Approach 1: General FOR loop
def Grow_With_Data(groupMsgs):
    d = {}

    for key, val in groupMsgs.items():
        from_cntry = key.split(',')[0]
        to_cntry = key.split(',')[1]
        d[from_cntry] = d.get(from_cntry,0) + val
        if from_cntry != to_cntry:
            d[to_cntry] = d.get(to_cntry,0) + val
    return d
assert Grow_With_Data({'US,US': 840,'US,CA': 470,'CA,US': 213,'IN,US': 198,'IN,IN': 194}) == {'US': 1721,'CA': 683,'IN': 392}
print("Passed!")

# Approach 2: Using SET() function and reduce duplicate work 
def Grow_With_Data(groupMsgs):
    d = {}

    for key, val in groupMsgs.items():
        from_cntry = key.split(',')[0]
        unique_cntry = set(key.split(','))
        for cntry in unique_cntry:
            d[cntry] = d.get(cntry,0) + val
    return d
assert Grow_With_Data({'US,US': 840,'US,CA': 470,'CA,US': 213,'IN,US': 198,'IN,IN': 194}) == {'US': 1721,'CA': 683,'IN': 392}
print("Passed!")
