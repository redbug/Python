#!/usr/bin/python

class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag
    
    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, value):
        self._imag = value

    def show(self):
        abs_imag = abs(self._imag)
        abs_imag = "" if abs_imag == 1 or abs_imag == 0 else abs_imag
        i="i"
        if self._imag > 0:
            if self._real != 0:
                sign = "+"
            else:
                sign = ""
        elif self._imag == 0:
            sign = ""
            i=""
        else:
            sign = "-"

        real = "" if self._real == 0 else self._real

        print "%s%s%s%s" % (real, sign, abs_imag, i)

    def __add__(self, other):
        assert isinstance(other, ComplexNumber)
        result = ComplexNumber()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result

    def __mul__(self, other):
        assert isinstance(other, ComplexNumber)
        result = ComplexNumber()
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.real * other.imag + self.imag * other.real
        return result

def main():
    a = ComplexNumber(0, 0)
    b = ComplexNumber(0, 1)
    c = ComplexNumber(0, 2)
    d = ComplexNumber(0, -1)
    e = ComplexNumber(0, -2)
    f = ComplexNumber(1, 0)
    g = ComplexNumber(1, 1)
    h = ComplexNumber(-1,1)
    i = ComplexNumber(-1, -1)
    ll = [a,b,c,d,e,f,g,h,i]
    [x.show() for x in ll]
    
    print "==================="
    a = ComplexNumber(2, -1)
    b = ComplexNumber(0, 1)
    c = ComplexNumber(1, 1) 
    c.show()
    (a+b).show()
    (b*c).show()
    (a*b*c).show()

if __name__ == "__main__":main()
