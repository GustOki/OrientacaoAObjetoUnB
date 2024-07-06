import math


#Classe Ponto
class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def distance(self):
        distance = math.sqrt(self._x**2 + self._y**2)
        return distance
    
    def model(self):
        print(f'Eu sou um ponto e minhas coordenadas são: x = {self._x} e y = {self._y}')


#Classe Reta
class Line(Point):

    def __init__(self, pointOrigem, pointFim, color):

        self._pointOrigem = pointOrigem
        self._pointFim = pointFim
        self._color = color


    def interpolar(self, x):

        y = self._pointOrigem * x + self._pointFim
        return y
    
    def comprimento(self):
        comprimento = math.sqrt((self._pointFim.x - self._pointOrigem.x)**2 + (self._pointFim.y - self._pointOrigem.y)**2)
        return comprimento

    
    def model(self):

        print(f'As coordenadas da minha reta tem um ponto de origem em: {self._pointOrigem} e ponto final em: {self._pointFim}, de cor {self._color}!')


#Classe Circulo
class Circle(Point):
    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self._raio = raio
        self._diametro = (self._raio)*2

    def model(self):
        print(f'Eu sou um círculo e minhas coordenadas são: x = {self._x} e y = {self._y}. O meu raio é {self._raio} e meu diâmetro é {self._diametro}')

