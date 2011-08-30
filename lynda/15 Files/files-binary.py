#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    infile = open( 'olives.jpg', 'rb' )
    outfile = open( 'new.jpg', 'wb' )
    buffer_size = 50000

    buffer = infile.read( buffer_size )

    while len( buffer ):
        outfile.write( buffer )
        print( '.', end='' )
        buffer = infile.read( buffer_size )

    print( 'done.' )

if __name__ == "__main__": main()
