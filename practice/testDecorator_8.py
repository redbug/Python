class decorator_with_instance(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, class_type):
        def wrapper(*args):
            print "instance: %s" % instance
            print "class_type: %s" % class_type
            print "MyClass.s: %s" % instance.x
            return self.f(instance, *args)
        return wrapper

class MyClass(object):
    def __init__(self):
        self.x = "MyClass.x"

    @decorator_with_instance
    def decorated_method(self):
        print "This is inside decorated_method()"

a = MyClass()
a.decorated_method()


"""
output:
instance: <__main__.MyClass object at 0x10c742910>
class_type: <class '__main__.MyClass'>
MyClass.s: MyClass.x
This is inside decorated_method()
"""