def square_root(number):
    sqrt_root=0
    for root in range(1,number+1):
        if root*root == number :
            sqrt_root+=root
    return sqrt_root
        
