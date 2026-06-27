def slices(series, length):
    new=str(series)
    if len(new) == 0:
        raise ValueError("series cannot be empty")
    if length > len(new) :
        raise ValueError("slice length cannot be greater than series length")
    if length < 0 :
        raise ValueError("slice length cannot be negative")
    if length == 0 :
        raise ValueError("slice length cannot be zero")

    return [new[i:length+i] for i in range(len(new)-length+1)]