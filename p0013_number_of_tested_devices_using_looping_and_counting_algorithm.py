# Question: find the number of tested devices after each test operations
""" 
The rules are : 
if batterypct[i] is greater than 0, 
     1. increment the count of tested devices 
     2. after testing, decrease the battery percentage of all devices by 1. 
     3. ensure the battery percentage never goes to zero. it must be always zero or more
     4. move to the next device
if batterypct[i] = 0, then move to the next device without performing any test 
"""

# Looping logic 
batteryPercentages = [1,1,2,1,3]
def Grow_With_Data(batteryPercentages):
    device_cnt = 0
    n = len(batteryPercentages)
    for indx in range(n):
        if batteryPercentages[indx] > 0: 
            device_cnt += 1 
            for sub_indx in range(indx+1,n):
                batteryPercentages[sub_indx] = max(0, batteryPercentages[sub_indx]-1)
    return device_cnt

Grow_With_Data(batteryPercentages)


# counting algorithm 
batteryPercentages = [1,8,8,8,3]
def Grow_With_Data(batteryPercentages):
    device_cnt = 0
    for indx in batteryPercentages:
        device_cnt = device_cnt + (indx > device_cnt)
    return device_cnt 
Grow_With_Data(batteryPercentages)

