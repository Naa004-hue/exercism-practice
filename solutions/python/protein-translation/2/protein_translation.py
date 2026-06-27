def proteins(strand):
    co_a={'AUG':'Methionine','UUU':'Phenylalanine', 'UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','UCU':'Serine','UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine','UAU':'Tyrosine', 'UAC':'Tyrosine','UGU':'Cysteine','UGC':'Cysteine','UGG':'Tryptophan','UAA':'STOP', 'UAG':'STOP','UGA':'STOP'}
    sli=[]
    result=[]
    for i in range(0,len(strand),3):
        new=strand[i:i+3]
        sli.append(new)

    for codon in sli :
        if co_a.get(codon) =='STOP':
            break
        else :
           result.append(co_a.get(codon))
    
    return result
        
    
    
        
        
