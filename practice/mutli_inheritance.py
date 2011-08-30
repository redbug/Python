'''
Created on Jun 30, 2011

@author: redbug
'''

class A(object):
    
    def foo(self):
        print "This is A"
        
class B(object):
    
    def foo(self):
        print "This is B"

class C(A, B):
    
    def foo(self):
        super(C,self).foo()
        print "This is C"
a = C()
a.foo()