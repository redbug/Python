#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print( divmod( 5, 3 ) )
    b( 5 )

    #the end of range is not inclusive
    for num in range( 0, 10 ): print( num, end='' )
    print()

    myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #the end of slice is not inclusive
    print( myList[5:10] )

    myList[3:5] = range( 90, 100 )
    print( myList )
    print( type( myList ) )
    print( range( 90, 100 ) )

    myList[:] = range( 90, 10 )
    print( myList )

    myList[:] = range( 0, 100 )
    print( myList )

    #start:end:step
    print( myList[0:50:2] )

    myList[0:10:2] = ( 'x', 'x', 'x', 'x', 'x' )
    print( myList )

def b( n ):
    print( '{:08b}'.format( n ) )

if __name__ == "__main__": main()
