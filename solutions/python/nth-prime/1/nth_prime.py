def prime(number):
    num= 2
    new_list=[]
    if number==0 :
        raise ValueError('there is no zeroth prime')
    while len(new_list)<number:
        is_prime=True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime=False 
                break
        if is_prime :
            new_list.append(num)
        num += 1
            
    return new_list[-1]
            
            
