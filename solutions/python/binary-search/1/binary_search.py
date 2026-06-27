def find(search_list, value):
    if len(search_list)==0:
        raise ValueError("value not in array")
    search_list.sort()
    left , right = 0 , len(search_list)-1
    while left<=right :
        mid=(right+left)//2
        if search_list[mid] == value:
            return mid
        if search_list[mid] > value :
            right = mid - 1
        if search_list[mid] < value :
            left = mid + 1
    else :
            raise ValueError("value not in array")
            