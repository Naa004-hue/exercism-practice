def flatten(iterable):
    new_iterable=[]
    for item in iterable :
        if isinstance(item, (list, tuple)):
            new_iterable.extend(flatten(item))
        if not isinstance(item, (list, tuple)):
            new_iterable.append(item)
        if None in new_iterable:
            new_iterable.remove(None)
    return new_iterable
