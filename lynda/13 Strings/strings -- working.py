#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = '    This is a string 1   \n'
    print( s.capitalize() )
    print( s.title() )
    print( s.upper() )
    print( s.swapcase() )
    print( s.find( 'is' ) )
    print( s.replace( 'This', 'That' ) )
    print( s.strip() ) #Return a copy of the string with leading and trailing characters removed.
    print( s.strip( '\n' ) )
    print( s.lstrip() )
    print( s.rstrip() )
    print( s.isalnum() )    #alpha & number but no whitespace
    print( "Redbug0314".isalnum() )
    print( s.isalpha() )
    print( "Redbug".isalpha() )
    print( s.isdigit() )
    print( "12345".isdigit() )
    print( s.isprintable() )
    print( s.strip( '\n' ).isprintable() )
    print( "Hello World".center( 80 ) )


if __name__ == "__main__": main()
