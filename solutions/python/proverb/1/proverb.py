def proverb(*words, qualifier=None):
    inputs=list(words)
    the_stuff='For want of a word the another was lost.'
    empty=[]
    if inputs == [] :
        return empty
    empty=[the_stuff.replace('word', inputs[i]).replace('another', inputs[i+1])for i in range(0,len(inputs)-1)]
    if qualifier== None:
        empty.append(f'And all for the want of a {inputs[0]}.')
    if qualifier!= None:
        empty.append(f'And all for the want of a {qualifier} {inputs[0]}.')
            
    return empty

