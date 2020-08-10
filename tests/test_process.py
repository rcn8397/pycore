import os
import sys
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.process import Process

def test_process():

    test_cmds = [
        'echo "Hello World"',
        'ls -al',
        'which python',
        ]

    for cmd in test_cmds:
        print( 'Running command: [{0}]'.format( cmd ) )
        proc = Process( cmd = cmd )
        assert len( proc.output )
        print( proc.output )

def main():
    test_process()

if __name__ == '__main__':
    main()
