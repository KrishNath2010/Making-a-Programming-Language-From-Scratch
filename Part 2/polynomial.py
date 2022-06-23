class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def simplify(self):
        return self


class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def simplify(self):
        return self


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


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(0), Add( Mul(X(), X()), Int(1)))))
print(repr(poly))
# print(repr(poly.simplify()))

