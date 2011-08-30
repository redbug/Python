#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    
    """
    from urllib import request
    page = request.urlopen('http://redbug0314.blogspot.com/2011/05/1337-leet-day.html')
    for line in page: 
         print( str(line, encoding='utf-8'), end='')
    """
    
    """
    import random
    x = list(range(1,25))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    """
    
    #bitstring module is a 3rd party library download from Python Package Index
    import bitstring
    a = bitstring.BitString(bin='01010101')
    print(a.hex, a.bin, a.uint)
    
        
if __name__ == "__main__": main()
