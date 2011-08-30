#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

try:
    fh = open( 'xlines.txt' )
    for line in fh.readlines():
        print( line )
except IOError as err:
    print( "Something bad happened: {}".format( err ) )

print ( "after exception!" )

