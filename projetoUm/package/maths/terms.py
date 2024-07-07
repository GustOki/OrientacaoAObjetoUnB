import math
from abc import ABC, abstractmethod

#Classe Ponto
class Point():
    def __init__(self, n):
        self._n = n
        
    def color(self):
        colorPoint = []
        for i in range(0, self._n):
            color = str(input(f"Digite a cor do ponto nº{i}: "))
            colorPoint.append(color)
        return colorPoint

    def coordenada(self):
        coordPoint = []
        for i in range(0, self._n):
            x = int(input(f"Digite a coordenada X do ponto nº{i}: "))
            y = int(input(f"Digite a coordenada Y do ponto nº{i}: "))
            vetorCoord = []
            vetorCoord.append(x)
            vetorCoord.append(y)
            coordPoint.append(vetorCoord)
        return coordPoint
    
    def returnPointX(self, point):
        self._point = point
        vetorX = {}
        for i in range(0, self._n):
            vetorX[f'x{i}'] = self._point[i][0]
        return vetorX
    
    def returnPointY(self, point):
        self._point = point
        vetorY = {}
        for i in range(0, self._n):
            vetorY[f'y{i}'] = self._point[i][1]
        return (vetorY)
    
    def setPointX(self, point):
        self._point = point
        for i in range(0, self._n):
            numX = int(input(f'Digite o novo valor do ponto x nº{i}: '))
            point[i].pop(0)
            point[i].insert(0, numX)

    def setPointY(self, point):
        self._point = point
        for i in range(0, self._n):
            numY = int(input(f'Digite o novo valor do ponto y nº{i}: '))
            point[i].pop(0)
            point[i].insert(0, numY)

    def distance(self):
        distance = math.sqrt(self._x**2 + self._y**2)
        return distance
    
    def returnPoint(self, point, color):
        infoPoint = int(input(f"Dado os pontos: {point}\n. Digite qual index queira acessar para obter informações do ponto: "))
        print(f"Informação: {point[infoPoint]}\ncor: {color[infoPoint]}")


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

