def to_rna(dna_strand):
    idk=list(dna_strand.upper())
    dna_strand_l=[]
    for nucleo in idk :
        if nucleo == 'A' :
            dna_strand_l.append('U')
        elif nucleo == 'G' :
            dna_strand_l.append('C')
        elif nucleo == 'T' :
            dna_strand_l.append('A')
        elif nucleo == 'C' :
            dna_strand_l.append('G')
    return ''.join(dna_strand_l)

print(to_rna('agtccgtattacgcatcagt'))
       
            