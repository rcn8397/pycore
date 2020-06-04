import os
import sys
import time
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import term

def test_progressbar( capsys ):
    p = term.ProgressBar()
    assert isinstance( p, term.ProgressBar )
    for i in range( 0, 101 ):
        p.update( i/100.0, prefix = 'prefix', suffix = 'suffix' )
        if capsys is not None:
            capture = capsys.readouterr()
            terminal = capture.out.split( ' ' )
            assert terminal[  0 ] == '\rprefix'
            assert terminal[ -2 ] == '{0}%'.format( ( i/100.0 ) * 100 )
            assert terminal[ -1 ] == 'suffix'
        time.sleep( 0.125 )
    sys.stdout.write( '\n' )


def test_yn(monkeypatch):
    '''
https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    '''
    questions = [
        'Does this work'
        ]
    defaults = [
        'y', 'n', None
        ]

    answers = { 'y' : True, 'n' : False, '' : None }

    for d in defaults:
        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "y" in the terminal:
        monkeypatch.setattr('builtins.input', lambda msg: 'y')
        q = term.Yn( 'Does this work?', default = d )
        assert q
        r = q.Ask()
        assert r

    for d in defaults:
        monkeypatch.setattr('builtins.input', lambda msg: 'n')
        q = term.Yn( 'Does this work?', default = d )
        assert q
        r = q.Ask()
        assert ( r == False )

def yn_test():
    questions = [
        'Does this work'
        ]
    defaults = [
        'y', 'n', None
        ]

    for d in defaults:
        q = term.Yn( 'Does this work?', default = d )
        q.Ask()

def main():
    test_progressbar( None )
    yn_test()

if __name__ == '__main__':
    main()
