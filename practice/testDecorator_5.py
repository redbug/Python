'''
Created on Jul 21, 2011

@author: redbug
'''

class decorator_with_args(object):
    
    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        
    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called once,
        as part of the decoration process! You can only give it a single
        argument, which is the function object.
        """
        
        print "Inside __call__()"
        
        def wrapped_f(*args):
            """
            wrapped_f() is the actual replacement function.
            """
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f

    
@decorator_with_args("hello", "world", "42")    
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4
    
print "After decoration"


print "Preparing to sayHello()"
sayHello("say", "hello", "argument", "list")
print "After first sayHello() call"
sayHello("a", "different", "set of", "arguements")
print "After second sayHello() call"



"""
Now the process of decoration calls the constructor and then immediately invokes __call__(), 
which can only take a single argument (the function object) and must return the decorated function object that replaces the original. 
Notice that __call__() is now only invoked once, during decoration, and after that the decorated function that you return from __call__() 
is used for the actual calls.
"""


