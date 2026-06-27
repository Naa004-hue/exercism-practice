"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats. """
    seats=['A','B','C','D']
    for i in range(number):
        yield seats[i%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    count=0
    k=0
    while count < number :
        row = k // 4 + 1
        letter = ["A","B","C","D"][k % 4]
        k+=1
        if row==13 :
            continue 
        yield f'{row}{letter}'
        count+=1
    
def assign_seats(passengers):
    """Assign seats to passengers."""
    return  dict(zip(passengers,list(generate_seats(len(passengers)))))

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat in seat_numbers :
        yield seat + flight_id+('0'*(12-len(seat + flight_id)))
