alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    index = alphabet.index(letter)
    row=[]
    for i in range(0,index+1):
        outer_s= ' '*(index-i)
        inner_s= ' '*0 if i==0 else ' '*((i*2)-1)
        char=alphabet[i]
        if char=='A' :
            row.append(outer_s+char+outer_s)
        else :
            row.append(outer_s+char+inner_s+char+outer_s)
    if index> 0 :
        row.extend(row[-2::-1])
    return row


