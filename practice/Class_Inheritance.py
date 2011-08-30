class A:
    
    def __init__(self):
        print "A"
    
    def hello(self):
        self.data = 'spam'
        
class B(A):
    
    def __init__(self):
        A.__init__(self)
        print "B"
        
    def hola(self):
        self.data2 = 'eggs'

def main():
    bb = B()
    print bb.__class__
    print B.__bases__
    print A.__bases__
    
    print bb.__dict__
    bb.hello()
    print bb.__dict__
    bb.hola()
    print bb.__dict__
    
    dir(B)
    
if __name__ == '__main__': main()
    