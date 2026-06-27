from itertools import zip_longest
def transpose(text):
    if text == "":
        return ""
    if '\n' in text :
        parts=text.splitlines()
        return '\n'.join(''.join(r).rstrip('ç').replace('ç',' ')for r in zip_longest(*parts, fillvalue='ç'))
    else :
        return '\n'.join(list(text))
