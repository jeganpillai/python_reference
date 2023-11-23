# brute force method 
def helper1(source):
    target = []
    for i in source.split():
        if i.lower() in target: 
            continue
        else:
            target.append(i.lower())
    return len(target)

assert helper1(source1) == 13
assert helper1(source2) == 4
assert helper1(source3) == 0
print("\n Pass")

# simple method 
def helper(source):
    return len(set(source.lower().split()))

assert helper(source1) == 13
assert helper(source2) == 4
assert helper(source3) == 0
print("\n Pass")

