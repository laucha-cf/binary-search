#This method ask each element if it is the target or not
#are you the one?
#-No, man
#Ah Okey, sorry. R you the one?...etc etc

def sequential_search( p_list:list, p_elem ):
    for i in range(len(p_list)):
        if p_elem == p_list[i]:
            return i
    return -1