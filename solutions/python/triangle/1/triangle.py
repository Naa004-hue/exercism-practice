def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b == c and a>0 and (a + b >= c and b + c >= a and a + c >= b):
        return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ( a == b or a == c or b == c ) and (a + b >= c and b + c >= a and a + c >= b):
       return True
    return False
    
def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ( a != b and a != c and b != c ) and (a + b >= c and b + c >= a and a + c >= b):
        return True
    return False