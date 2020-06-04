# -*- coding: utf-8 -*-
'''
Terminal tools
'''
import os
import sys

def user_input( msg ):
    '''
    Manage input between python 2/3
    '''
    inp = None
    try:
        inp = raw_input( msg )
    except NameError:
        try:
            inp = input( msg )
        except NameError:
            raise
    return inp


class ProgressBar( object ):
    def __init__( self, clear_screen = False ):
        self.platform = os.uname()
        self.clear_screen = clear_screen
        self.clear()

    def pos( self, y, x ):
        return '\x1b[%d;%dH' % (y, x)

    def clear( self ):
        if not self.clear_screen:
            return

        try:
            clear = '\033[2J\033[H' # Ubuntu terminal
            sys.stdout.write( clear )
        except:
            if 'nt' in self.platform:
                clear = 'clear'
            else:
                clear = 'cls'
            os.system( clear )

    def update( self, percent, prefix = '', suffix = '' ):
        self.clear()
        bar = ( '=' * int( percent * 20 ) ).ljust( 20 )
        percent = str( percent * 100 )
        out = "\r%s [%s] %s%% %s" % ( prefix, bar, percent, suffix )
        sys.stdout.write( out )
        sys.stdout.flush()


def safe_key( k, d, err = None ):
    v = None
    try:
        v = d[ k ]
    except KeyError as e:
        if err is not None:
            print( '{0}; error= {1}'.format( err, e ) )
    return v

class Yn( object ):
    '''
    Yes/No question object

    Ask a yes/no question with an assumed default
    '''
    def __init__( self, question, default = None ):
        super( Yn, self ).__init__()
        self.default = None
        self.valid   = {
            'yes' : True,
            'y'   : True,
            'no'  : False,
            'n'   : False
        }
        self.preselect = {
            None  : 'y/n',
            True  : 'Y/n',
            False : 'y/N'
        }

        self.set_prompt( question, default )


    def set_prompt( self, question, default ):
        err   = 'Invalid default: [{0}]'.format( default )
        preselect = safe_key( default, self.valid )
        self.prompt = '{0} [{1}] '.format( question,
                                           safe_key( preselect, self.preselect ) )
        self.default = preselect

    def validate_response( self, response ):
        err = 'Please respond with (Y)es/(N)o'
        return safe_key( response.lower(),
                         self.valid,
                         err = err )

    def Ask( self ):
        while True:
            response = user_input( self.prompt )
            if '' == response and self.default is not None:
                return self.default
            else:
                valid = self.validate_response( response )
                if valid is not None:
                    return valid
