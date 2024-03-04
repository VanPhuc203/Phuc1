newTuple = ('a', 'b', 'c', 'd', 'e')
def seachTuple(p_Tuple, element):
    
    for i in range(0, len(p_Tuple)):
        if p_Tuple[i] == element:
            return f"The {element} is found at {i} index"
    return 'The element is not found'
      
    print(seachTuple(newTuple, 'b'))