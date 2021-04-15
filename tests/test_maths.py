import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.maths import *

def test_interpolate():
    pt0 = ( 4500, 150 )
    pt1 = ( 7500, 141 )
    print( interpolate( pt0, pt1, 6000 ) )

def test_betwixt():
    l = [1,5,3,43,35,3,1116]
    l.sort()
    assert( ( betwixt( l, 0 ) == None ) )
    assert( ( betwixt( l, 4 ) != None ) )
    assert( ( betwixt( l, 3 ) == None ) )
    assert( ( betwixt( l, 2 ) != None ) )
    assert( ( betwixt( l, 3.3 ) != None ) )
    assert( ( betwixt( l, 1116 ) == None ) )
    assert( ( betwixt( l, 1117 ) == None ) )
    
def main():
    test_betwixt()
    test_interpolate()


if __name__ == '__main__':
    main()
