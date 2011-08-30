'''
Created on Jul 21, 2011

@author: redbug
'''

class decorator_without_args(object):
    
    def __init__(self, f):
        """
        If there are no decorator arguments, the function 
        to be decorated is passed to the constructor. 
        """
        print "Insde __init__()"
        self.f = f
        
    def __call__(self, *args):
        """
        The __call__ method is not called until the decorated
        function is called.
        """
        print "Inside __call__()"
        self.f(*args)
        print "After self.f(*args)"
        
@decorator_without_args        
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4
    

print "After decoration"
sayHello("say", "hello", "argument", "list")
print "After first sayHello() call"
sayHello("a", "different", "set of", "arguements")
print "After second sayHello() call"

