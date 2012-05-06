#!/usr/bin/python

class Quaternions(object):
    def __init__(self, w=0, i=0, j=0, k=0):
        self._w = w 
        self._i = i
        self._j = j
        self._k = k
    
    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        self._i = value

    @property
    def j(self):
        return self._j

    @j.setter
    def j(self, value):
        self._j = value

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value

    def present_componet(self, prevs, comp, symbol):
        abs_comp = abs(comp)
        abs_comp = "" if abs_comp == 1 or abs_comp == 0 else abs_comp

        if comp > 0:
            if prevs != [0] * len(prevs):
                sign = "+"
            else:
                sign = ""
        elif comp == 0:
            sign = ""
            symbol=""
        else:
            sign = "-"

        return "%s%s%s" % (sign, abs_comp, symbol)

    def show(self):
        w = "" if self._w == 0 else self._w
        comps = map(self.present_componet, 
                [[self._w], [self._w, self._i], [self._w, self._i, self._j]], 
                [self._i, self._j, self._k], 
                ["i", "j", "k"])
        
        print str(w) + "".join(comps)

    def __add__(self, other):
        assert isinstance(other, Quaternions)
        result = Quaternions()
        result.w = self.w + other.w
        result.i = self.i + other.i
        result.j = self.j + other.j
        result.k = self.k + other.k 
        return result

    def __mul__(self, other):
        assert isinstance(other, Quaternions)
        result = Quaternions()
        result.w = (self.w * other.w) - (self.i * other.i) - (self.j * other.j) - (self.k * other.k)
        result.i = (self.w * other.i) + (self.i * other.w) + (self.j * other.k) - (self.k * other.j)
        result.j = (self.w * other.j) - (self.i * other.k) + (self.j * other.w) + (self.k * other.i)
        result.k = (self.w * other.k) + (self.i * other.j) - (self.j * other.i) + (self.k * other.w)
        return result

def main():
    a = Quaternions(0, 0, 0, 0)
    b = Quaternions(1, 0, 0, 0)
    c = Quaternions(1, 1, 0, 0)
    d = Quaternions(1, -1, 1, 0)
    e = Quaternions(1, 1, -1, 1)
    f = Quaternions(1, -2, 3, -4)
    ll = [a,b,c,d,e,f]
    [x.show() for x in ll]
    c.show()
    (c+d).show()
    (d*e).show()
    (d*e*f).show()
    
if __name__ == "__main__":main()
