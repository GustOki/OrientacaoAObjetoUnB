import math
from abc import ABC, abstractmethod

#Classe Ponto
class Point():
    def __init__(self, n, x, y):
        self._n = n
        self._x = x
        self._y = y

    def setN(self, n):
        self._n = n

    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y
    
    def getN(self):
        return self._n

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def distance(self):
        distance = math.sqrt(self._x**2 + self._y**2)
        return distance
    
    def model(self):
        print(f'As coordenadas do ponto {self._n} são: x = {self._x} e y = {self._y}')


#Classe Reta
class Line():

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
    def __init__(self, n, x, y, raio):
        super().__init__(n ,x, y)
        self._raio = raio
        self._diametro = (self._raio)*2

    def model(self):
        print(f'As coordenadas do círculo {self._n} são: x = {self._x} e y = {self._y}. O seu raio é {self._raio} e seu diâmetro é {self._diametro}')


#Classe Quadrado
class Square():
    def __init__(self, n, lado):
        self._n = n
        self._lado = lado

    def area(self):
        area = self._lado**2
        return area
    
    def perimetro(self):
        perimetro = self._lado*4
        return perimetro
    

#Classe Retangulo
class Rectangle(Square):
    def __init__(self, n, lado, altura): #neste caso, o lado será a base do retângulo
        super().__init__(n, lado)
        self._n = n
        self._altura = altura

    def area(self):
        area = self._lado * self._altura
        return area
    
    def perimetro(self):
        perimetro = 2*(self._lado + self._altura)
        return perimetro

