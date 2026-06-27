def commands(binary_str):
    binary_l=list(binary_str)
    result=[]
    if binary_l[4]=='1':
        result.append('wink')
    if binary_l[3]=='1':
        result.append('double blink')
    if binary_l[2]=='1':
        result.append('close your eyes')
    if binary_l[1]=='1':
        result.append('jump')
    if binary_l[0]=='1':
        result.reverse()
    return result
    
