def classify(number):
    """ A perfect number equals the sum of its positive divisors."""
    aliquot  = 0
    if number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    for num in range(1,number):
        if number % num == 0:
           aliquot  += num
    if aliquot  == number:
        return  "perfect" 
    if aliquot  > number :
        return "abundant"
    if aliquot  < number :
        return "deficient"
        
