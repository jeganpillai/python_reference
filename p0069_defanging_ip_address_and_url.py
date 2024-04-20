# Question: Defanging an IP Address or URL

# English Video: 
# Tamil Video: 

# Approach 1: Using FOR loop 
def Grow_With_Data(address):
    result = ''
    for i in address:
        if i == '.':
            result += '[.]'
        else:
            result += i
    return result
assert Grow_With_Data('240.20.100.60') == '240[.]20[.]100[.]60'
assert Grow_With_Data('www.growwithdata.co') == 'www[.]growwithdata[.]co'
print('Passed!')

# Approach 2: List Comprehension 
def Grow_With_Data(address):
    return ''.join(['[.]' if i == '.' else i for i in address])
assert Grow_With_Data('240.20.100.60') == '240[.]20[.]100[.]60'
assert Grow_With_Data('www.growwithdata.co') == 'www[.]growwithdata[.]co'
print('Passed!')

# Approach 3: Using REPLACE() function 
def Grow_With_Data(address):
    return address.replace('.','[.]')
assert Grow_With_Data('240.20.100.60') == '240[.]20[.]100[.]60'
assert Grow_With_Data('www.growwithdata.co') == 'www[.]growwithdata[.]co'
print('Passed!')
