def is_triangle(sides):
    a,b,c=sorted(sides)
    if a + b >= c and b + c >= a and a + c >= b and all(x > 0 for x in sides) :
        return True
    return False

def equilateral(sides):
    a,b,c=sorted(sides)
    if is_triangle(sides):
        if a==b==c :
            return True
        return False
    return False

def isosceles(sides):
    a,b,c=sorted(sides)
    if is_triangle(sides):
        if a==b or a==c or b==c :
            return True
        return False
    return False

def scalene(sides):
    a,b,c=sorted(sides)
    if is_triangle(sides):
        if a!=b and b!=c:
            return True
        return False
    return False
 