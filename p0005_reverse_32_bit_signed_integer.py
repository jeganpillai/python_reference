# Question: Given a 32-bit signed integer, reverse digits of that integer

# Clarifications 
/*
1. signed integer, means Negative numbers and positive numbers, right? 
   if its -123, then the output should be -321 
2. 32-bit signed integer, means? 
   the reversed integer must be between [−2**31,  2**31 − 1], [-2147483648, 2147483648]
   that is input between [-8463847412 , 8463847412] is accepted
3. what if the integer has zero at the end, like 120? 
   ignore the leading zeros, so output will be 21. if its -120, then output is -21
*/
# approach 1: loop method
input_value = -123 
def helper(input_value):
    input_string = str(abs(input_value))
    reversed_output = ''
    for i in input_string:
        reversed_output = i + reversed_output
    reverse_output = int(reversed_output.lstrip('0')) * (-1 if input_value < 0 else 1)
    
    return  reverse_output if -2**31 <= reverse_output <= 2**31 else 0
    
helper(input_value)

# approach 2: simple code 
input_value = -1230
def helper(input_value):
    output_data = int(str(abs(input_value))[::-1].lstrip('0')) * (-1 if input_value < 0 else 1 )
    return output_data if -2147483648 <= output_data <= output_data else 0 
    
helper(input_value)

# approach 3: reverse without converting to string 
input_data = -8463847412
def helper(input_data):
    output_data = 0
    chk = abs(input_data)
    for i in range(len(str(chk))):
        output_data = output_data*10 + chk%10
        chk = chk//10
    output_data = output_data * (-1 if input_data < 0 else 1)
    return output_data if -2147483648 <= output_data <= output_data else 0
helper(input_data)
