class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def simplify(self):
        return self

    def evaluate(self, i):
        return Int(i)

    def max_degree(self):
        return 1


class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def simplify(self):
        return self
    
    def evaluate(self, i):
        return self
    
    def max_degree(self):
        return 0


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            if simp1.i == 1:
                return simp2
            if isinstance(simp2, Int):
                return Int(simp1.i * simp2.i)
            if isinstance(simp2, Mul):
                if isinstance(simp2.p1, Int):
                    return Mul(Int(simp1.i * simp2.p1.i), simp2.p2.simplify())
                if isinstance(simp2.p2, Int):
                    return Mul(Int(simp1.i * simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(0)
            if simp2.i == 1:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i * simp2.i)
            if isinstance(simp1, Mul):
                if isinstance(simp1.p1, Int):
                    return Mul(Int(simp2.i * simp1.p1.i), simp2.p2.simplify())
                if isinstance(simp1.p2, Int):
                    return Mul(Int(simp2.i * simp1.p2.i), simp2.p1.simplify())
        return Mul(simp1, simp2)

    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Mul(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return simp1.max_degree() + simp2.max_degree()


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return simp2
            if isinstance(simp2, Int):
                return Int(simp1.i + simp2.i)
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i + simp2.i)
        return Add(simp1, simp2)

    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Add(simp1.evaluate(i), simp2.evaluate(i)).simplify()

    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return max([simp1.max_degree(), simp2.max_degree()])


def equals(p1, p2):
    d1 = p1.max_degree()
    d2 = p2.max_degree()

    if d1 != d2:
        return False
    
    if d1 == 0:
        simp1 = p1.simplify()
        simp2 = p2.simplify()
        if isinstance(simp1, Int) and isinstance(simp2, Int):
            return simp1.i == simp2.i
        # We have a problem...
        raise ValueError
    
    new_p1 = Sub(p1, Pow(X(), d1))
    new_p2 = Sub(p2, Pow(X(), d2))
    return equals(new_p1, new_p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(repr(poly))
print(repr(poly.simplify()))
print(poly.evaluate(-1))
print(poly.max_degree())

