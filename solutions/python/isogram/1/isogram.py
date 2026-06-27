def is_isogram(string):
    string=string.lower()
    exept=[' ','-']
    for index in range(0,len(string)):
        for i in range(1,len(string)):
            if (string[index]==string[i]) and (string[index] not in exept) and (i != index):
                return False
    return True
            