import os
import sys
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import strings

def test_wrap_string():
    test_string='this string is very long and needs to be wrapped to the column width of {0}'
    test_cols = [ 5, 7, 10, 15, 18, 20, 25, 30, 35, 40, 75, 80, 100 ]
    for col in test_cols:
        print( '#' + '-' * col )
        print( '# Test case {0}'.format( col ) )
        print( '#' + '-' * col )
        s = test_string.format( col )
        result = strings.wrap_string( s, col )
        assert result
        for i in range( col ):
            sys.stdout.write( str(i%10) )
        sys.stdout.write( '\n' )
        print( result )

def main():
    test_wrap_string()


if __name__ == '__main__':
    main()
