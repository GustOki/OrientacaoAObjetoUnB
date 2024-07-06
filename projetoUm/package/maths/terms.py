import math

#Classe Reta
class Line():

    def __init__(self,a,b, color):

        self.a = a
        self.b = b
        self.color = color


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: a={self.a}, b={self.b} e de cor {self.color}!')

#Classe Ponto
class Point():
    def __init__(self, x, y):
        self.setX(x)
        self._x = self.getX()

        self.setY(y)
        self._y = self.getY()

    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def distance(self):
        return(self._x**2 + self._y**2)**(0.5)
    
    def model(self):
        print(f'Eu sou um ponto e minhas coordenadas são: x = {self._x} e y = {self._y}')

#Classe Circulo
class Circle(Point):
    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self._raio = raio
        self._diametro = (self._raio)*2

    def model(self):
        print(f'Eu sou um círculo e minhas coordenadas são: x = {self._x} e y = {self._y}. O meu raio é {self._raio} e meu diâmetro é {self._diametro}')

#Classe Triangulo
class Triangle(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

