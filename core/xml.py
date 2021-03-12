# -*- coding: utf-8 -*-
'''
Xml objects utilties
'''

def el2dict( el ):
    '''
    Convert an lxml Element object to a dictionary recursively
    '''
    children = el.getchildren()
    values   = []

    if len( children ) == 1:
        values = el2dict( children[0] )
    else:
        for child in children:
            values.append( el2dict( child ) )

    if len( children ) > 0:
        d = { el.tag : values }
    else:
        d = { el.tag : el.attrib[ 'value' ] }
    return d
