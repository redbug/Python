#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    def __init__( self, **kgwargs ):
        self._variables = kgwargs

    def quack( self ):
        print( 'Quaaack!' )

    def walk( self ):
        print( 'Walks like a duck.' )

    def set_variable( self, k, v ):
        self._variables[k] = v

    def get_variable( self, k ):
        return self._variables.get( k, None )

def main():
    donald = Duck( feet=2, fur='white' )
    donald.quack()
    donald.walk()
    print( donald.get_variable( 'fur' ) )
    print( donald.get_variable( 'feet' ) )

    donald.set_variable( 'fur', 'black' )

    print( donald.get_variable( 'fur' ) )

if __name__ == "__main__": main()
