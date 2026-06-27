import re, string
class PhoneNumber:
    def __init__(self, number):
        self.number=self.valid(number)
    def valid(self,number):
        new=list(re.sub(r"[()\-. +]", "", number))
        if len(new) < 10 :
            raise ValueError("must not be fewer than 10 digits")
        if len(new) == 11 and new[0] != '1' :
            raise ValueError("11 digits must start with 1")
        if len(new) > 11 :
            raise ValueError("must not be greater than 11 digits")
        if len(new) == 11 and new[0] == '1' :
            new.pop(0)
        if new[0] == '1' :
            raise ValueError("area code cannot start with one")
        if new[0] == '0' :
            raise ValueError("area code cannot start with zero")
        if new[3] == '1' :
            raise ValueError("exchange code cannot start with one")
        if new[3] == '0' :
            raise ValueError("exchange code cannot start with zero")
        if any(ch.isalpha() for ch in new):
           raise ValueError("letters not permitted")
        if any( ch in string.punctuation for ch in new):
            raise ValueError("punctuations not permitted")
        return ''.join(new)
    @property
    def area_code (self) :
        num= self.number
        return num[:3]
    def pretty (self) :
        num= self.number
        return f"({num[:3]})-{num[3:6]}-{num[6:]}"
        
        
        
        
        
        
