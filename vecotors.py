class Vect:
    elems = []
    def __init__(self,*args):
        for elem in args:
            if type(elem) is int:
                self.elems.append(elem)
                self.elems.sort()
    def __str__(self):
        if len(self.elems)>0:

            return f'Vector:{tuple(self.elems)}'
        else:
            return f'Empty Vector'

v= Vect(8,7,1,2,3,4,'a','b',6)

print(v)

class Vector:
    def __init__(self,*args):
        self.values = sorted(args)

    def __str__(self):
        if self.values:
            return f'Vector: {" ".join(map(str,self.values))}'
        else:
            return f'Empty Vector'

    def __add__(self, other):
        if isinstance(other,int):
            return Vector(*map(lambda x:x+other, self.values))
        elif isinstance(other,Vector):
            if len(other.values) == len(self.values):
                b = [sum(i) for i in zip(self.values,other.values)]
                return Vector(*b)
            else:
                print('Vectors must have same length')
        else:
            print(f'Vector could not summ with {other}')


    def __mul__(self, other):
        if isinstance(other,int):
            return Vector(*map(lambda x:x*other, self.values))
        elif isinstance(other,Vector):
            if len(other.values) == len(self.values):
                b = [i[0]*i[1] for i in zip(self.values,other.values)]
                return Vector(*b)
            else:
                print('Vectors must have same length')
        else:
            print(f'Vector could not multiplay with {other}')


c = Vector(1,2,3,4)
print(c)

b = Vector()
print(b)
print(c+3)
z = c+c
print(c*c)
