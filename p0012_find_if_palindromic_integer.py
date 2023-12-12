# Question: Find If The Given Integer is Palindromic using String Conversion and use MOD and reverse methods 

# Approach 1: convert to string and reverse to check palindrome 
input_src = -121
def GrowWithData(input_src):
    if input_src%10 == 0:
        return False
    input_int = abs(input_src)
    output_int = int(str(input_int)[::-1]) * -1 if input_src < 0 else int(str(input_int)[::-1])
    return input_src ==  output_int
GrowWithData(input_src)

# Approach 2: Using MOD and reverse integer to check palindrome 
input_src = -121
def GrowWithData(input_src):
    if input_src%10 == 0:
        return False
    input_data = abs(input_src)
    output_data = 0
    for i in range(len(str(input_data))):
        output_data = output_data * 10 + input_data%10
        input_data = input_data // 10
    output_data = output_data * -1 if input_data < 0 else output_data 
    return input_src == output_data
GrowWithData(input_src)
