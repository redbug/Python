'''
Created on Jul 21, 2011

@author: redbug
'''


class MyDecorator:
    #===========================================================================
    # Entry Point
    #===========================================================================
    def __init__(self, f): 
        print "inside MyDecorator.__init__()"
        f()
        
    #===========================================================================
    # Exit Point
    #===========================================================================
    def __call__(self):
        print "inside MyDecorator.__call__()"

@MyDecorator
def aFunction():
    print "inside aFunction()"
    
def main():    
    aFunction()
    print "Finished decorating aFunction()"
    
if __name__ == '__main__':main()