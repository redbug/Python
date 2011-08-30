#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__( self, **kwargs ):
        self.properties = kwargs

    def quack( self ):
        print( 'Quaaack!' )

    def walk( self ):
        print( 'Walks like a duck.' )

    def get_properties( self ):
        return self.properties

    def get_property( self, key ):
        return self.properties.get( key, None )

    def set_property( self, k, v ):
        self.properties[k] = v

    #getter 
    @property
    def color( self ):
        return self.get_property( 'color' )

    #setter
    @color.setter
    def color( self, value ):
        self.set_property( 'color', value )

    #destructor?
    @color.deleter
    def color( self ):
        del self.properties['color']

def main():
    donald = Duck()
    donald.color = 'blue'
    print( donald.color )

if __name__ == "__main__": main()
