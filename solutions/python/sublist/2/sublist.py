"""This exercise stub and the test suite contain several enumerated constants."""


SUBLIST = 'sublist '
SUPERLIST  = 'superlist' 
EQUAL = 'equal'
UNEQUAL = 'unequal'

def sublist(list_one, list_two):
    
    if list_one == list_two:
        return EQUAL
    if not list_one : 
        return SUBLIST
    if not list_two :
        return SUPERLIST 
 
    if any(list_two[i:len(list_one)+i]==list_one for i in range(len(list_two)-len(list_one)+1)):
        return SUBLIST
    if any(list_one[i:len(list_two)+i]==list_two for i in range(len(list_one)-len(list_two)+1)):
        return SUPERLIST
    else :
        return UNEQUAL
    
        
