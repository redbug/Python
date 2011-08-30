#!/usr/bin/python2.6
'''
Created on Apr 7, 2011

@author: redbug
'''

import sys


def gen(n):
    for i in range(n):
        yield i*2

g = ( i * 2 for i in range(10) )
print "g is a %s" % g

for p in g:
    sys.stdout.write( str(p) )    

print "\ngen(10) is a %s" % gen(10)

for p in gen(10):
    sys.stdout.write( str(p) )