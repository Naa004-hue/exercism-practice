def factors(value):
    values=[]
    num=2
    while value != 1 :
        is_prime=True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime=False 
                break
        if is_prime and value % num == 0 :
            values.append(num)
            value//=num
        else :
            num += 1
    return values
