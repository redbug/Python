#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk( self ):
        print( 'I have something to say!' )

    def walk( self ):
        print( "Hey, I'm walking here!" )

    def clothes( self ):
        print( "I love nice clothes" )

class Duck( Animal ):
    def quack( self ):
        print( 'Quaaack!' )

    def walk( self ):
        print( 'Walks like a duck.' )

class Dog( Animal ):
    pass


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.talk()
    donald.clothes()

    fido = Dog()
    fido.clothes()
    fido.talk()

if __name__ == "__main__": main()
