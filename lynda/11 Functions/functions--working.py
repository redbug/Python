#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
#    func1( 1, 2, 3, 4, 5 )
    func2( 1, 2, one='1', two='2', three='3' )
    print()

    for i in inclusiveRange( 5, 25, 3 ):
        print( i, end=' ' )

def func1( arg1, arg2, *args ):
    print( arg1, arg2, args )
    for arg in args:
        print( arg, end=' ' )

def func2( arg1, arg2, **kwargs ):
    print( arg1, arg2, kwargs )
    for key in kwargs:
        print( key, kwargs[key], end=' ' )

def inclusiveRange( *args ):
    numArgs = len( args )
    if numArgs < 1: raise TypeError( 'requires at lease one argument' )
    elif numArgs == 1:
        stop = args[0]
        start = 1
        step = 1
    elif numArgs == 2:
        ( start, stop ) = args
        step = 1
    elif numArgs == 3:
        ( start, stop, step ) = args
    else: raise TypeError( 'inclusiveRange expected at most 3 arguments, got {}'.format( numArgs ) )

    n = start
    while( n <= stop ):
        yield n
        n += step

if __name__ == "__main__": main()
