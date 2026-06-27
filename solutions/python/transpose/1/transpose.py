from itertools import zip_longest
def transpose(text):
    if text == "":
        return ""
    if '\n' in text :
        parts=text.split('\n')
        width = max(len(row) for row in parts) 
        padded = [list(row) for row in parts]
        cols = zip_longest(*padded, fillvalue=None)
        lines = []
        for col in cols:
            j = len(col)
            while j > 0 and col[j-1] is None:
                j -= 1
            line = ''.join(ch if ch is not None else ' ' for ch in col[:j])
            lines.append(line)
        return '\n'.join(lines)
    else :
        return '\n'.join(list(text))
