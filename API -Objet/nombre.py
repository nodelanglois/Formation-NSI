# Nomre

class API_Nombre():
    def __init__(self, num, den): # On attend des entiers
        pass
    def add(self, b):
        return 0  # to be implemented

    def sub(self, b):
        return 0 # to be implemented

    def mult(self, b):
        return 0 # to be implemented

    def div(self, b):
        return 0 # to be implemented

    def neg(self):
        return 0 # to be implemented

    def __str__(self):
        return "0"


class Nombre(API_Nombre):  # héritage de API_Nombre
    def __init__(self, num, den): # 
        self.num = num
        self.den = den
        
    def add(self, b):
        return Nombre(self.num*b.den+self.den*b.num, self.den*b.den)

    def __add__(self, b):
        return self.add(b)

    def neg(self):
        return Nombre(-self.num, self.den)

    def sub(self, b):
        return self.add(b.neg())

    def mult(self, b):
        return Nombre(self.num*b.num, self.den*b.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


#if __name__=='main':
a = Nombre(1, 10)
b = Nombre(2, 15)
print(a.add(b))
print(a+b)
print(a.mult(b))


    

    
        
        
