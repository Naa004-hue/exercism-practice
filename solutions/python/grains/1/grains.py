def square(number):
    if number in range(1,65):
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")
    
def total():
    Llistt=[]
    for n in range(1,65):
        idk= square(n)
        Llistt.append(idk)
    return sum(Llistt)
        
