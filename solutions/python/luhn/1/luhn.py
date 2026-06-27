class Luhn:
    def __init__(self, card_num):
        self.card_num=list(reversed(card_num.replace(' ','')))

    def valid(self):
        for d in self.card_num:
            if not d.isdigit():
                return False
        new_card = [int(d) for d in self.card_num] 
        if len(new_card)<= 1 :
            return False
        for k in range(1,len(new_card),2):
            num=new_card[k]*2
            if num > 9 :
                num -= 9
            new_card[k]=num
            
        total=sum(new_card)
        if total % 10 == 0 :
             return True
        else : 
             return False
