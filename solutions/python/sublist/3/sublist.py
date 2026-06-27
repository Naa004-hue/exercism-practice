"""This exercise stub and the test suite contain several enumerated constants."""


SUBLIST = 'sublist '
SUPERLIST  = 'superlist' 
EQUAL = 'equal'
UNEQUAL = 'unequal'

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(list_1,list_2):
    for i in range(len(list_2) - len(list_1) + 1):
        if  list_2[i:len(list_1)+i] == list_1 :
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two :
        return 3
    elif is_sublist(list_one,list_two):
        return 1
    elif is_sublist(list_two,list_one):
        return 2
    else :
        return 4
    
        
