# -*- coding: utf-8 -*-
'''
Search utilities
'''

def betwixt( itemlist, value, start=0, end=None ):
    '''
    For a sorted list of items <itemlist>, given a <value>, find the pair of items 
    the value is betwixt. 

    Returns the a tuple containing the both lower and upper values.
    Returns None if the value matches an item value in the list.
    Returns None if the value is less than the smallest item in the list.
    Returns None if the value is greater than the largest item in the list.
    '''
    if end is None:
        end = len( itemlist )
        
    index = start+(end - start)/2

    # Special case: we are at or past the limits 
    if index >= len( itemlist )-1:
        return None
    
    val1  = itemlist[index+1]
    val0  = itemlist[index]

    if value == val0:
        # Special case 2, value is not betwixt any
        return None
    elif value < val1 and value > val0:
        return ( val0, val1 )
    elif value > val0:
        return betwixt( itemlist, value, index, end )
    else:
        if index == 0:
            # Special case: at limit
            return None
        else:
            return betwixt( itemlist, value, start, index )

