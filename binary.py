
def binary_search( p_list:list, p_elem ):
    low = 0
    high = len(p_list)-1
    mid_index = len(p_list) // 2

    while( low <= high ):
        if p_list[mid_index] == p_elem:
            return mid_index
        elif p_elem > p_list[mid_index]:
            low = mid_index + 1
            mid_index = (low + high) // 2
        elif p_elem < p_list[mid_index]:
            high = mid_index - 1
            mid_index = (low + high) // 2
    return -1
    

def recursive_binary_search( p_list:list, p_elem, low=None, high=None ):
    if low == None:
        low = 0
    if high == None:
        high = len(p_list)-1

    mid_index = (low + high) // 2

    if low > high:
        return -1
    if p_list[mid_index] == p_elem:
        return mid_index
    elif p_elem > p_list[mid_index]:
        #low = mid_index + 1 
        return recursive_binary_search(p_list, p_elem, mid_index + 1, high)
    else:
        #high = mid_index - 1
        return recursive_binary_search(p_list, p_elem, low, mid_index - 1)





