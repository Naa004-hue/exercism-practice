def sum_of_multiples(limit, multiples):
    mul_s=set()
    for value in multiples :
        for num in range(1,limit):
            if value * num < limit :
                mul_s.add(value*num)
    return sum(mul_s)
            
