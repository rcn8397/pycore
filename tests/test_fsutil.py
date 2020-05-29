import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import fsutil

def test_mkdir_p():
    import shutil
    root  = './.tst'
    paths = [
        'one', 'two', 'three'
        ]
    for path in paths:
        test_path = os.path.join( root, path )
        print( 'Attempting to create {0}'.format( test_path ) )
        fsutil.mkdir_p( test_path )
        assert os.path.exists( test_path )

    print( 'Cleaning up' )
    shutil.rmtree( root )

def main():
    test_mkdir_p()


if __name__ == '__main__':
    main()
