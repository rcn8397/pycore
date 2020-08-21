# -*- coding: utf-8 -*-
'''
String tools
'''

def wrap_string( s, col = 80, debug = False ):
    '''
    Wrap a string <s> at column <col>
    '''
    tmp   = ''
    start = 0
    prev  = 0
    for i,c in enumerate( s ):
        if debug: print( 'c: {0}, i: {1:02}, start: {2:02}, prev: {3:02}, s[ start:i ] = {4}'.format( c, i, start, prev, s[ start:i]  ) )
        if c == ' ':
            prev = i

        if i == 0:
            continue
        elif i % col == 0:
            if ( c != ' ' and s[ i-1: i ] == ' ' ) or (c == ' ' ):
                tmp = tmp + s[ start : i ].lstrip() + '\n'
                start = i
            elif c != ' ':
                tmp = tmp + s[ start:prev ].lstrip() + '\n'
                start = prev
            else:
                assert( False )
        elif i == len( s ) - 1:
            tmp = tmp + s[ start : ].lstrip()

    return tmp
