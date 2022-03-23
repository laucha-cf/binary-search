
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
        low = mid_index + 1
        return recursive_binary_search(p_list, p_elem, low, high)
    else:
        high = mid_index - 1
        return recursive_binary_search(p_list, p_elem, low, high)




lista = [1,2,3,4,5,6,7,8,9,10]
elem = 22
result = recursive_binary_search(lista, elem)
if result != -1:
    print(f'El elemento {elem} se encuentra en la posición {result}')
else:
    print('El elemento no se encuentra en la lista')



