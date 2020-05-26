# -*- coding: utf-8 -*-
'''
File system utilities
'''
import errno
import os
import fnmatch

def mkdir_p( path ):
    '''
    mkdir -p functional equivalent
    '''
    try:
        os.makedirs( path )
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir( path ):
            pass
        else:
            raise

is_ext = lambda f, ext : any( f.endswith( e ) for e in ext )

class FileWalker( object ):
    def __init__( self, root ):
        '''
        File system walker
        '''
        self.root = root
        if not os.path.exists( root ):
            sys.exit( 'Path does not exist: %s' % root )

        self.followlinks = False

    def find( self, patterns = [] ):
        '''
        Find all files with ext patterns
        '''
        matches = []
        for root, dirs, files in os.walk( self.root, topdown=True ):
            for filename in files:
                if is_ext( filename.lower(), patterns ):
                    match = os.path.join( root, filename )
                    matches.append( match )
        return matches

    def find_obj( self, patterns, obj = str ):
        matches = []
        for root, dirs, files in os.walk( self.root, topdown=True ):
            for filename in files:
                if is_ext( filename.lower(), patterns ):
                    match = os.path.join( root, filename )
                    try:
                        o = obj( match )
                    except Exception as e:
                        print( str( e ) )
                        sys.exit( 'Failure to create {0} as {1}'.format( match, obj ) )
                    matches.append( o )
        return matches

    def findall( self, pattern ):
        matches = []
        for root, dirs, files in os.walk( self.root, topdown=True ):
            for filename in fnmatch.filter( files, pattern ):
                match = os.path.join( root, filename )
                matches.append( match )
        return matches

    def walk( self ):
        for root, dirs, files in os.walk( self.root,
                                          topdown=True,
                                          followlinks = self.followlinks ):
            for name in files:
                print( os.path.join( root, name ) )
            for name in dirs:
                print( os.path.join( root, name ) )
