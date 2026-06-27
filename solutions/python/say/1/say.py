tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
num_di = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",14: "fourteen", 15: "fifteen", 16: "sixteen",17: "seventeen", 18: "eighteen", 19: "nineteen"}
def tenss(number):
    if number<20 :
        return num_di[number]
    ten_d=(number//10)*10
    one_d=number%10
    if number>=20 and number%10 != 0:
        return tens[ten_d]+'-'+num_di[one_d]
    if number>=20 and number%10 == 0:
        return tens[ten_d]

def hundreds(number):
    hun_d=(number//100)
    no_hun=number-(hun_d*100)
    if number %100 == 0 :
        return num_di[hun_d]+' '+'hundred'
    if number %100 != 0 :
        return num_di[hun_d]+' '+'hundred'+' ' +tenss(no_hun)
    
def thousands(number):
    thou_d=(number//1000)
    no_thou=number-(thou_d*1000)
    if number %1000 == 0 :
        return say(thou_d)+' '+'thousand'
    else :
        return say(thou_d)+' '+'thousand'+' '+say(no_thou)
        
def millions(number):
    mill_d=(number//1000000)
    no_mill=number-(mill_d*1000000)
    if number %1000000 == 0 :
        return say(mill_d)+' '+'million'
    else :
        return say(mill_d)+' '+'million'+' '+say(no_mill)

def billions(number):
    bill_d=(number//1000000000)
    no_bill=number-(bill_d*1000000000)
    if number %1000000000 == 0 :
        return say(bill_d)+' '+'billion'
    else :
        return say(bill_d)+' '+'billion'+' '+say(no_bill)
        
def say(number):
    if number < 0 or number > 999_999_999_999 :
        raise ValueError("input out of range")
    if number<100 :
        return tenss(number)
    if number<1000 :
        return hundreds(number)
    if number<1000000:
        return thousands(number)
    if number<1000000000:
        return millions(number)
    if number<1000000000000:
        return billions(number)
            
                
            
            
            
