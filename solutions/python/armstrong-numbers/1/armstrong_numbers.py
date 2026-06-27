def is_armstrong_number(number):
    make= list(str(number))
    summ=0
    power=len(make)
    for digit in range(0,len(make)):
         summ+=int(make[digit])**power
    return summ == number 
