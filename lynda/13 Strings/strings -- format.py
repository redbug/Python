#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 10, 20
    print( "this is {}, that is {}".format( a, b ) )
    print( "this is %d, that is %d" % ( a, b ) )
    print( "this is {1}, that is {0}".format( a, b ) )
    print( "this is {1}, that is {0}, this too is {1}".format( a, b ) )
    print( "this is {sean}, that is {gage}".format( gage=a, sean=b ) )

    d = dict( gage=a, sean=b )
    print( "this is {sean}, that is {gage}".format( **d ) )
if __name__ == "__main__": main()
