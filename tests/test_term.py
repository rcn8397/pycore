import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import term

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
    yn_test()

if __name__ == '__main__':
    main()
