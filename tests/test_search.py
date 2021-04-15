import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import search

def test_betwixt():
    l = [1,5,3,43,35,3,1116]
    l.sort()
    assert( ( search.betwixt( l, 0 ) == None ) )
    assert( ( search.betwixt( l, 4 ) != None ) )
    assert( ( search.betwixt( l, 3 ) == None ) )
    assert( ( search.betwixt( l, 2 ) != None ) )
    assert( ( search.betwixt( l, 3.3 ) != None ) )
    assert( ( search.betwixt( l, 1116 ) == None ) )
    assert( ( search.betwixt( l, 1117 ) == None ) )
    
def main():
    test_betwixt()



if __name__ == '__main__':
    main()
