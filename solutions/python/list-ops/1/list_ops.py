def append(list1, list2):
    return list1 + list2

def concat(lists):
    empty=[]
    for lil in lists :
        empty.extend(lil)
    return empty


def filter(function, list):
    new_l=[]
    for item in list :
        if function(item):
            new_l.append(item)
    return new_l
            
def length(list):
    leng=0
    for item in list :
        leng+=1
    return leng
    
def map(function, list):
    new_l=[]
    for item in list :
        new_l.append(function(item))
    return new_l


def foldl(function, list, initial):
    for item in list :
        initial = function(initial,item)
    return initial

def foldr(function, list, initial):
    list.reverse()
    for item in list:
        initial = function(initial,item)
    return initial
    
def reverse(list):
    new_l=[]
    for index in range( len(list)-1,-1,-1):
        new_l.append(list[index])
    return new_l
        
        




    
