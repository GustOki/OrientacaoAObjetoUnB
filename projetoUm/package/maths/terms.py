import math
from abc import ABC, abstractmethod

#Classe Ponto
class Point():
    def __init__(self, n):
        self._n = n

    def colorPoint(self):
        vetorColorPoint = []
        for i in range(0, self._n):
            color = str(input(f"Digite a cor do seu ponto {i}: "))
            vetorColorPoint.append(color)
        
        return vetorColorPoint

    def coordPoint(self):
        vetorCoordPoint = []
        for i in range(0, self._n):
            x = int(input(f"Digite a coordenada de x({i}): "))
            y = int(input(f"Digite a coordenada de y({i}): "))

            vetor = []
            vetor.append(x)
            vetor.append(y)
            vetorCoordPoint.append(vetor)

        return vetorCoordPoint

    def returnPointX(self, point):
        self._point = point
        vetorPointX = {}
        for i in range(0, self._n):
            vetorPointX[f'x({i})'] = self._point[i][0]
        
        return vetorPointX

    def returnPointY(self, point): 
        self._point = point
        vetorPointY = {}
        for i in range(0, self._n):
            vetorPointY[f'y({i})'] = self._point[i][1]
        
        return(vetorPointY)

    def showPoint(self, point, color):
            num = int(input(f"Dados os pontos: {point}. Digite a index que você quer consultar as informações de ponto: ")) 
            print(f"Ponto solicitado: coordenada{point[num]} e de cor {color[num]}!")
 

#Classe Reta ARRUMAR AQUI DEPOIS
class Line():
    def __init__(self,n):
        self._n = n
        self._pointObj = Point(n)
        self._coord = self._pointObj.coordPoint()

    def inclinacaoLine(self):
        if len(self._coord) >= 2:
            deltaX = self._coord[1][0] - self._coord[0][0]
            deltaY = self._coord[1][1] - self._coord[0][1]
            
            if deltaX > 0:
                inclinacao = deltaY / deltaX
                return inclinacao
            
            else:
                return 'O seu deltaX é = 0, tente outro caso!'
            
        elif len(self._coord) == 1:
            inclinacao = self._coord[0][1] / self._coord[0][0]
            return inclinacao

    def coefLinear(self, m): #m = coeficiente angular
        self._m = m
        if type(self._m) == float:
            coefLinear = self._coord[0][1] - self._coord[0][0] * self._m
            return coefLinear
        else:
            return "O seu deltaX é = 0, tente outro caso!"
    

    def montarTabela(self, m, coefLinear, i): #assosiação    self-association
        print(f"__TABELA__\n  X | Y  ")
        for x in range(0, i):
            y = m * x + coefLinear
            print(f"  {x} | {y}  ")

    def interpolar(self, m, coefLinear, x): #associação   self-association
        y = m * x + coefLinear
        return y

#Classe de coordenada única
class coordCircle: 
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def coordenadaX(self):
        return self._x
    
    def coordenadaY(self):
        return self._y

#Classe Circulo
class Circle():
    def __init__(self, x, y, raio):
        self._x = x
        self._y = y
        self._raio = raio

    def circunferenciaCircle(self):
        circunf = 2*3.14*self._raio
        return circunf

    def diametroCircle(self):
        diametro = 2*self._raio
        return diametro

    def areaCircle(self):
        area = 3.14*(self._raio**2)
        return area

    def perimetroCircle(self, teta, circunf):
        perimetro = (teta/(2*3.14))*circunf
        return perimetro

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
        self._n = n
        self._altura = altura

        super().__init__(n, lado)

    def area(self):
        area = self._lado * self._altura
        return area
    
    def perimetro(self):
        perimetro = 2*(self._lado + self._altura)
        return perimetro
    

#Classe Losango
class Losango(Square):
    def __init__ (self, n, lado, diagMaior, diagMenor):
        self._diagMaior = diagMaior
        self._diagMenor = diagMenor
        
        super().__init__(n, lado)

    def areaLosango(self):
        area = (self._diagMaior * self._diagMenor)/2
        return area
    
#Classe Triângulo Equilatero
class TriangleEquil():
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def _verificaTriEquil(self):
        aux = False

        if(self._x + self._y) > self._z and (self._x + self._z) > self._z and (self._y + self._z) > self._x:
            aux = True
            return aux
        
        else:
            return aux

    def _verificaLados(self):
        aux = False
        
        if self._x == self._y == self._z:
            aux = True
            return aux
        
        else:
            return aux

    def alturaTriEquil(self):
        verificarTri = self._verificaTriEquil()
        verificarLado = self._verificaLados()
        
        if verificarTri == True and verificarLado == True:
            if self._x == self._y:
                altura = ((self._z/2)**2 +  self._x**2)**0.5
                return altura
            
            elif self._x == self._z:
                altura = ((self._y/2)**2 +  self._x**2)**0.5
                return altura
            
            elif self._y == self._z:
                altura = ((self._x/2)**2 +  self._y**2)**0.5
                return altura
            
        else:
            return "As entradas não são válidas!"

    def areaTriEquil(self):
        verificarTri = self._verificaTriEquil()
        verificarLado = self._verificaLados()

        if verificarTri == True and verificarLado:
            if self._x == self._y and self._y == self._z:
                area = ((self._x**2)*(3**0.5))/4
                return area
            
        else:
            return "As entradas não são válidas!"

    def perimetroTriEquil(self):
        verificarTri= self._verificaTriEquil()
        verificarLados = self._verificaLados()

        if verificarTri == True and verificarLados == True:
            perimetro = self._x + self._y + self._z
            return perimetro
        
        else:
            return "As entradas não são válidas!"

#Classe Triangulo Isosceles        
class TriangleIsos(TriangleEquil):
    # dois lados iguais

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def _verificaLados(self):
        if self._x == self._y and self._z != self._x:
            return True
        
        if self._x == self._z and self._y != self._x:
            return True
        
        if self._z == self._y and self._z != self._x:
            return True
        
        else: 
            return False
        
    def _alturaTriIsos(self):
        verificarTri = self._verificaTriEquil()
        verificarLados = self._verificaLados()
        
        if verificarTri == True and verificarLados == True:
            if self._x == self._y:
                altura = (self._x**2 - (self._z**2)/4)**0.5
                return altura
            
            elif self._x == self._z:
                altura = (self._x**2 - (self._y**2)/4)**0.5
                return altura
            
            elif self._y == self._z:
                altura = (self._y**2 - (self._x**2)/4)**0.5
                return altura
        
        else:
            return "As entradas não são válidas!"

    def _baseTriIsos(self):
        verificarTri = self._verificaTriEquil()
        verificarLados = self._verificaLados()
        
        if verificarTri == True and verificarLados == True:
            if self._x == self._y:
                return self._z
            
            elif self._x == self._z:
                return self._y
            
            elif self._y == self._z:
                return self._x
        
        else:
            return "As entradas não são válidas!"

    def areaTriIsos(self):
        verificarTri = self._verificaTriEquil()
        verificarLados = self._verificaLados()
        
        if verificarTri == True and verificarLados == True:
            altura = self._alturaTriIsos()
            base =  self._baseTriIsos()
            area = (base*altura)/2
        
            return area
        
        else:
            return "As entradas não são válidas!"
        
#Classe Triangulo Escaleno
class TriangleEscaleno():
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def _verificaDiferenca(self):
        aux = False

        if self._x + self._y > self._z and self._y + self._z > self._x and self._z + self._x > self._y:
            if self._x != self._y and self._y != self._z and self._x != self._z:
                aux = True
                return aux
            
            else:
                return aux
            
        else: 
            return aux
        
    def _menorAngulo(self):
        m = min(self._x,self._y,self._z)
        aux = 180/(self._x + self._y + self._z)
        menorTeta = aux*m

        return menorTeta
        
    def _maiorAngulo(self):
        m = max(self._x,self._y,self._z)
        aux = 180/(self._x + self._y + self._z)
        maiorTeta = aux*m

        return maiorTeta

    def angulosInternos(self):
        menorTeta = self._menorAngulo()
        maiorTeta = self._maiorAngulo()
        TetaMeio = 180 - menorTeta - maiorTeta
        
        print(f"{maiorTeta}, {menorTeta}, {TetaMeio}")

    def alturaTriEsc(self): 
        verificador = self._verificaDiferenca()

        if verificador == True:
            a = self._menorAngulo()
            aux = math.sin(a)
            altura = self._z*aux

            return altura
        
        else:
            return "As entradas não são válidas!"

    def areaTriEsc(self):
        verificador = self._verificaDiferenca()

        if verificador == True:
            altura =  self.alturaTriEsc()
            area = (self._z * altura)/2

            return area
        
        else:
            return "As entradas não são válidas!"

    def perimetroTriEsc(self):
        verificador = self._verificaDiferenca()

        if verificador == True:
            perimetro = self._x + self._y + self._z

            return perimetro
        
        else: 
            return "As entradas não são válidas!"

#Classe Poligono        
class Polygon(ABC): 
    def __init__(self, n):
        self._n = n
    @abstractmethod

    def areaPolygon(self):
        pass

    def perimetroPolygon(self):
        perimetro = self._i*self._n

        return perimetro

#Classe Pentagono    
class Pentagon(Polygon):
    def __init__(self, n):
        super().__init__(n)
        self._i = 5
    
    def areaPentagon(self):
        aux = math.tan(36)
        area = (5*self._n**2)/(4*aux)

        return area

#Classe Hexagono    
class Hexagon(Polygon):
    def __init__(self, n):
        super().__init__(n)
        self._i = 6

    def areaHexagon(self):
        area = ((3*self._n**2)*3**0.5)/2
        return area
    
#Classe Trapézio Isosceles
class TrapezioIsosceles():
    def __init__(self, baseMenor, baseMaior, altura):
        self._baseMenor = baseMenor
        self._altura = altura
        self._baseMaior = baseMaior

    def areaTrapIsos(self):
        area = ((self._baseMenor + self._baseMaior)*self._altura)/2
        return area
    
    def ladoTrapIsos(self):
        aux = (self._baseMaior - self._baseMenor)/2
        lado = (self._altura**2 + aux**2)**0.5
    
        return lado
    
    def perimetroTrapIsos(self):
        lado = self.ladoTrapIsos()
        perimetro = lado*2 + self._baseMenor + self._baseMaior
    
        return perimetro
    
    def getAltura(self):
        return self._altura

#Classe Trapézio Retângulo
class TrapezioRetangulo(TrapezioIsosceles):
    def ladoTrapRet(self): 
        aux = self._baseMaior - self._baseMenor
        lado = (aux**2 + self._altura**2)**0.5

        return lado
    
    def perimetroTrapRet(self):
        lado = self.ladoTrapRet()
        perimetro = self._baseMaior + self._baseMenor + lado + self._altura

        return perimetro