#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack( self ):
        print( 'Quaaack!' )

    def walk( self ):
        print( 'Walks like a duck.' )

    def bark( self ):
        print( 'Duck can\'t bark.' )

    def fur( self ):
        print( "Duck has feather." )

class Dog:
    def quack( self ):
        print( "Dog can't quack!" )

    def walk( self ):
        print( "Walks like a dog." )

    def bark( self ):
        print( "Woof!" )

    def fur( self ):
        print( "Dog has white fur." )


def main():
    donald = Duck()
    fido = Dog()

    #polymorphism
    for o in ( donald, fido ):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

if __name__ == "__main__": main()
