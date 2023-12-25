# Question: Return list containing all the mismatched words from the given two strings 
# Video: https://www.youtube.com/watch?v=CJRG4QsCbPo

# Approach 1: General approach 
def Grow_With_Data(str1, str2):
    if not str1 or not str2:
        return str1.split() + str2.split()
    lst1 = str1.split()
    lst2 = []
    for val in str2.split():
        if val in lst1:
            lst1.remove(val)
        else:
            lst2.append(val)
    return lst1+lst2

def cmp_lst(l1,l2):
    return sorted(l1) == sorted(l2)

assert cmp_lst(Grow_With_Data("",""), []) == True
assert cmp_lst(Grow_With_Data("","This is the second string"), ['This','is','the','second','string']) == True
assert cmp_lst(Grow_With_Data("This is the first string",""), ['This','is','the','first','string']) == True
assert cmp_lst(Grow_With_Data("This is the first string","This is the second string"),['first', 'second']) == True
assert cmp_lst(Grow_With_Data("This is the first string extra","This is the second string"),['first', 'second', 'extra']) == True
assert cmp_lst(Grow_With_Data("This is the first text","This is the second string"),['first', 'text', 'second', 'string']) == True
assert cmp_lst(Grow_With_Data("Firstly this is the first string","Next is the second string"), ['Firstly', 'this', 'first', 'Next', 'second']) == True
print('\n(passed!)')

# Approach 2: using SET 
def Grow_With_Data(str1, str2):
    if not str1 or not str2:
        return str1.split() + str2.split()
    lst1 = set(str1.split())
    lst2 = []
    for val in str2.split():
        if val in lst1:
            lst1.remove(val)
        else:
            if not val in lst2:
                lst2.append(val)
    return list(lst1)+lst2

# Approach 3: using SET operations 
str1, str2 = "This is the first and first string","This is the second string"

def Grow_With_Data(str1, str2):
    if not str1 or not str2:
        return str1.split() + str2.split()
    set1 = set(str1.split())
    set2 = set(str2.split())
    
    return (set1 - set2).union(set2 - set1)
Grow_With_Data(str1, str2)
