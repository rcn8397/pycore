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

def test_filewalker():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    fw = fsutil.FileWalker( root )
    assert( fw )

    # Find all the python files
    results = fw.findall( '*.py' )
    print( results )
    assert results

    results = fw.find( [ '.py', '.md' ] )
    print( results )
    assert results

    results = fw.findobj( [ '.py', '.md' ] )
    print( results )
    assert results

def main():
    test_mkdir_p()
    test_filewalker()


if __name__ == '__main__':
    main()
