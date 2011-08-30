#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # =========== tuple is immutable =================
    t = 1, 2, 3, 4
    print( type( t ), t )

    t2 = tuple( range( 25 ) )
    print( type( t2 ), t2 )
    # tuple() constructor only takes one argument which must be iterable

    print( t[0] )
    print( t[-1] )

    print( len( t ) )
    print( max( t ) )
    print( min( t ) )

    print( type( ( 1 ) ) )
    print( type( ( 1, ) ) )
    print( type( ( 1, 2 ) ) )

    #============ list is mutable ===================
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    l[3] = 'a'
    print( l )

    print( 3 in l )
    print( 'c' in l )

    for i in l: print( i, end=' ' )
    print()

    l[5] = 'a'
    print( l.count( 'a' ) )
    print( l.index( 5 ) )

    l.append( 'gg' )
    print( l )

    l.extend( range( 10 ) )
    print( l )

    l.insert( 4, 'b' )
    print( l )

    l.remove( 'gg' )
    print( l )

    del l[-1]
    print( l )

    l.pop()
    print( l )

    l.pop( 0 )
    print( l )
if __name__ == '__main__': main()
