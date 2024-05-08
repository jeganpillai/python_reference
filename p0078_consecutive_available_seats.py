# Question: Find the length of the longest consecutive sequence of available seats in the cinema

# English Video: 
# Tamil Video: 

def Grow_With_Data(cinema):
    max_length = 0
    max_start_seat = None
    max_end_seat = None
    
    current_length = 0
    start_seat = None
    end_seat = None
    
    for seat_id, free in cinema:
        if free == 1:
            if current_length == 0:
                start_seat = seat_id
            current_length += 1
            end_seat = seat_id
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_seat = start_seat
                max_end_seat = end_seat
            current_length = 0
    
    if current_length > max_length:
        max_length = current_length
        max_start_seat = start_seat
        max_end_seat = end_seat
    
    return (max_start_seat, max_end_seat, max_length)


assert Grow_With_Data([(1, 1),(2, 0),(3, 1),(4, 1),(5, 1)]) == (3,5,3)
assert Grow_With_Data([(1, 1),(2, 0),(3, 1),(4, 1),(5, 1),(6,0),(7,0),(8,0),(9,1),(10,1),(11,1),(12,1)]) == (9,12,4)
print('Passed!')
