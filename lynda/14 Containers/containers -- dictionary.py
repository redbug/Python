#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = {'one':1, 'two':2, 'three':3}
    print( type( d ), d )

    d2 = dict( one=1, two=2, three=3 )
    print( type( d2 ), d2 )

    d3 = dict( a=1, b=2, c=3, **d )
    print( type( d3 ), d3 )

    print( d3.keys() )
    print( d3.values() )
    print( 'a' in d3 )
    print( 'z' in d3 )

    for k, v in d.items():
        print( k, v, end=';' )

    print()
    print( d3['a'] )
    print( d3.get( 'z', 'default value' ) )

    del d3['a']
    print( d3 )

    d3.pop( 'b' )
    print( d3 )

    d3.popitem()
    print( d3 )

    d3.popitem()
    print( d3 )


if __name__ == "__main__": main()
