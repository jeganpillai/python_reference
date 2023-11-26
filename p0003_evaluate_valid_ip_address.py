# Question: 
# Evaluate the given IP Address and return True, if its valid IP address and False, if not. 

# checks
# must have 4 set of numbers separated by period '.'
# numbers must be between 0 to 255 
# no negative numbers, must be greater than zero and less than or equal to 255 
# no alphabets or special characters
# must not start with Zero, if its more than one digit in a set

# brute force method 
ip = '25.0.0.1'
target = []
for i in ip.split('.'):
    if i.isdigit() and 0 <= int(i) <= 255 and (len(i) == 1 or i[0] != '0'):
        target.append(i)
print(target)
len(target) == 4

# elegant way of coding
ip = '25.0.0.1'

def helper(ip):
    return len([i for i in ip.split('.') if i.isdigit() and 0 <= int(i) <= 255 and (len(i) == 1 or i[0] != '0')]) == 4
helper(ip)

# practice with multiple outputs 
def is_valid_IP(ip):
    return sum([True for i in ip.split('.') if i.isdigit() and 0 <= int(i) <= 255 and (len(i) == 1 or i[0] != '0')]) == 4

assert is_valid_IP('') == False
assert is_valid_IP('127.0.0.1') == True
assert is_valid_IP('127.0.0.100') == True
assert is_valid_IP('192.34.0.0.1') == False
assert is_valid_IP('192.3.0.1') == True
assert is_valid_IP('192.289.25.10') == False
assert is_valid_IP('192.289.25') == False
assert is_valid_IP('a12.A.29.5') == False
assert is_valid_IP('127.0.0.1999') == False
assert is_valid_IP('02.0.0.19') == False
assert is_valid_IP('-7.0.0.99') == False
print("\n(Passed!)")

