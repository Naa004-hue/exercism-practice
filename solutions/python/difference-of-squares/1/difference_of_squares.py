def square_of_sum(number):
    sums=0
    for num in range(1,number+1):
        sums+=num
    return sums**2
    
def sum_of_squares(number):
    sums_s=0
    for num in range(1,number+1):
        sums_s+=num**2
    return sums_s

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
