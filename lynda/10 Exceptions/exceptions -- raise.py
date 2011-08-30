#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readFile( 'xlines.doc' ): print( line.strip() )
    except IOError as err:
        print( "Can't open the file:", err )
    except ValueError as err:
        print( "Bad filename:", err )

def readFile( filename ):

    if filename.endswith( '.txt' ):
        fh = open( filename )
        return fh.readlines()

    else: raise ValueError( 'Filename must ends with .txt' )

if __name__ == "__main__": main()
