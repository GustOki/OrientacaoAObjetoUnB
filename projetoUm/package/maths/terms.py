import math

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
        
        return vetorPointY
    
    def getCoordPoint(self):
        return self.coordPoint()

    def showPoint(self, point, color):
            num = int(input(f"Pontos criados: {point}. Digite a index que você quer consultar as informações de ponto: ")) 
            print(f"Ponto solicitado: coordenada{point[num]} e de cor {color[num]}!")
 

#Classe Reta
class Line():
    def __init__(self, n):
        self._n = n
        self._pointObj = Point(n)
        self._coord = self._pointObj.getCoordPoint()

    def lenghtLine(self): 
        if len(self._coord) >= 2:
            deltaX = self._coord[1][0] - self._coord[0][0]
            deltaY = self._coord[1][1] - self._coord[0][1]
            tamanho = math.sqrt(deltaX**2 + deltaY**2)
            
            return tamanho
        
        else:
            return "Não há pontos suficientes para formar uma linha."

    def colorLine(self):
        color = str(input(f"Digite a cor da reta: "))
        return color

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

    def coefLinear(self, coefAng):
        self._coefAng = coefAng
        if type(self._coefAng) == float:
            coefLinear = self._coord[0][1] - self._coord[0][0] * self._coefAng
            return coefLinear
        else:
            return "O seu deltaX é = 0, tente outro caso!"

    def interpolar(self, coefAng, coefLinear, x):
        y = coefAng * x + coefLinear
        return y
    
    def showLine(self, lenght, color, coefAng, coefLinear, interpolacao):
        lenght = self.lenghtLine()
        inclinacao = self.inclinacaoLine()
        coefAng = inclinacao if isinstance(inclinacao, float) else "Indefinida"
        coefLinear = self.coefLinear(coefAng) if isinstance(coefAng, float) else "Indefinido"
        interpolacao = self.interpolar(coefAng, coefLinear, 0) if isinstance(coefAng, float) else "Indefinida"
        
        print(f"A sua reta foi criada com {lenght} de tamanho e de cor {color}, com um coeficiente angular de {coefAng}, um coeficiente linear de {coefLinear} e uma interpolação de y = {interpolacao}!")

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

    def colorCircle(self):
        color = str(input(f"Digite a cor do círculo: "))
        return color

    def circunferenciaCircle(self):
        circunf = 2 * math.pi * self._raio
        return circunf

    def diametroCircle(self):
        diametro = 2 * self._raio
        return diametro

    def areaCircle(self):
        area = math.pi * (self._raio ** 2)
        return area
    
    def showCircle(self, color, circunf, diametro, area):
        circunf = self.circunferenciaCircle()
        diametro = self.diametroCircle()
        area = self.areaCircle()
        
        print(f"O seu círculo foi criado com {circunf} de circunferência e de cor {color}, com um diâmetro de {diametro} e uma área de {area}!")

#Classe Quadrado
class Square():
    def __init__(self, lado):
        self._lado = self._validaLado(lado)

    def colorSquare(self):
        color = str(input(f"Digite a cor do quadrado: "))
        return color

    def _validaLado(self, lado): #valida se o comprimento do lado é maior que zero
        if lado <= 0:
            raise ValueError("Atenção, o lado do quadrado deve ser maior que zero!")
        return lado

    def areaSquare(self):
        area = self._lado**2
        return area
    
    def perimetroSquare(self):
        perimetro = self._lado*4
        return perimetro
    
    def showSquare(self, lado, color, area, perimetro):
        area = self.areaSquare()
        perimetro = self.perimetroSquare()
        
        print(f'O seu quadrado foi criado com cor {color} e com os lados de comprimento {lado}, com área de {area} e perímetro de {perimetro}!')
    
#Classe Retangulo
class Rectangle():
    def __init__(self, rectBase, rectAlt):
        self._rectBase = self._validaLado(rectBase)
        self._rectAlt = self._validaLado(rectAlt)
        self._color = self.colorRectangle()

    def colorRectangle(self):
        color = input("Digite a cor do retângulo: ")
        return color

    def _validaLado(self, lado):
        if lado <= 0:
            raise ValueError("Atenção, o lado do retângulo deve ser maior que zero!")
        return lado

    def areaRectangle(self):
        return self._rectBase * self._rectAlt

    def perimetroRectangle(self):
        return 2 * (self._rectBase + self._rectAlt)

    def showRectangle(self, area, perimetro):
        area = self.areaRectangle()
        perimetro = self.perimetroRectangle()
        print(f'O seu retângulo foi criado com cor {self._color} e com base de comprimento {self._rectBase} e altura de {self._rectAlt}, com área de {area} e perímetro de {perimetro}!')
    

#Classe Losango
class Losango(Square):
    def __init__ (self, lado, diagMaior, diagMenor):
        super().__init__(lado)
        self._diagMaior = diagMaior
        self._diagMenor = self._validaDiag(diagMenor)
        self._color = self.colorLosango()

    def colorLosango(self):
        color = input("Digite a cor do losango: ")
        return color

    def areaLosango(self):
        area = (self._diagMaior * self._diagMenor) / 2
        return area
    
    def _validaDiag(self, diag):
        if diag <= 0:
            raise ValueError("Atenção, a diagonal deve ser maior que zero!")
        return diag
    
    def showLosango(self):
        area = self.areaLosango()
        print(f'O seu losango foi criado com cor {self._color} com área de {area}!')
    
#Classe Triângulo Equilatero
class TriangleEquil():
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        self._lado = lado
        self._color = self.colorTriEquil()

    def colorTriEquil(self):
        color = input("Digite a cor do triângulo equilátero: ")
        return color
    
    def triEquilEhValido(self):
        return self._lado > 0
    
    def ehEquil(self):
        return True

    def alturaTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            altura = (self._lado * (3 ** 0.5)) / 2
            return altura
        else:
            return "As entradas não são válidas!"

    def areaTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            area = ((self._lado ** 2) * (3 ** 0.5)) / 4
            return area
        else:
            return "As entradas não são válidas!"

    def perimetroTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            perimetro = self._lado * 3
            return perimetro
        else:
            return "As entradas não são válidas!"
        
    def showTriEquil(self):
        altura = self.alturaTriEquil()
        area = self.areaTriEquil()
        perimetro = self.perimetroTriEquil()
        
        print(f"O seu triângulo equilátero foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!")

class TriangleIsos(TriangleEquil):
    def __init__(self, ladoIgual, base):
        super().__init__(ladoIgual)
        self._base = self._validaBase(base)
        self._color = self.colorTriIsos()

    def colorTriIsos(self):
        color = input("Digite a cor do triângulo isósceles: ")
        return color

    def _validaBase(self, base):
        if base <= 0 or base >= 2 * self._lado:
            raise ValueError("A base do triângulo isósceles deve ser maior que zero e menor que dois vezes o lado igual.")
        return base

    def alturaTriIsos(self):
        altura = (self._lado ** 2 - (self._base ** 2 / 4)) ** 0.5
        return altura

    def areaTriIsos(self):
        area = (self._base * self.alturaTriIsos()) / 2
        return area
    
    def perimetroTriIsos(self):
        perimetro = self._lado * 2 + self._base
        return perimetro
    
    def showTriIsos(self):
        altura = self.alturaTriIsos()
        area = self.areaTriIsos()
        perimetro = self.perimetroTriIsos()
        
        print(f"O seu triângulo isósceles foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!")


        
#Classe Triangulo Escaleno
class TriangleEscaleno():
    def __init__(self, x, y, z):
        self._x = self._verificaLado(x)
        self._y = self._verificaLado(y)
        self._z = self._verificaLado(z)
        self._color = self.colorTriEsc()
        
        if not self._verificaDiferenca():
            raise ValueError("Os lados fornecidos não formam um triângulo escaleno!")

    def colorTriEsc(self):
        color = input("Digite a cor do triângulo escaleno: ")
        return color
    
    def _verificaLado(self, lado):
        if lado <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        return lado

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
        m = min(self._x, self._y, self._z)
        aux = 180 / (self._x + self._y + self._z)
        menorTeta = aux * m

        return menorTeta
        
    def _maiorAngulo(self):
        m = max(self._x, self._y, self._z)
        aux = 180 / (self._x + self._y + self._z)
        maiorTeta = aux * m

        return maiorTeta

    def angulosInternos(self):
        menorTeta = self._menorAngulo()
        maiorTeta = self._maiorAngulo()
        TetaMeio = 180 - menorTeta - maiorTeta
        
        print(f"{maiorTeta}, {menorTeta}, {TetaMeio}")

    def alturaTriEsc(self): 
        verificador = self._verificaDiferenca()

        if verificador:
            a = self._menorAngulo()
            aux = math.sin(a)
            altura = self._z * aux

            return altura
        
        else:
            return "As entradas não são válidas!"

    def areaTriEsc(self):
        verificador = self._verificaDiferenca()

        if verificador:
            altura =  self.alturaTriEsc()
            area = (self._z * altura) / 2

            return area
        
        else:
            return "As entradas não são válidas!"

    def perimetroTriEsc(self):
        verificador = self._verificaDiferenca()

        if verificador:
            perimetro = self._x + self._y + self._z

            return perimetro
        
        else: 
            return "As entradas não são válidas!"
        
    def showTriEsc(self):
        altura = self.alturaTriEsc()
        area = self.areaTriEsc()
        perimetro = self.perimetroTriEsc()
        
        print(f"O seu triângulo escaleno foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!")


from abc import ABC, abstractmethod
#Classe Poligono        
class Polygon(ABC): 
    def __init__(self, n, tamanhoLado):
        self._n = self._validaLado(n)
        self._lado = self._validaTamanhoLado(tamanhoLado)

    @abstractmethod
    def _validaLado(n):
        if n < 3:
            raise ValueError("O polígono deve ter pelo menos 3 lados!")
        return n

    @abstractmethod
    def _validaTamanhoLado(tamanhoLado):
        if tamanhoLado <= 0:
            raise ValueError("O comprimento do lado deve ser maior que zero!")
        return tamanhoLado

    def areaPolygon(self):
        pass

    def perimetroPolygon(self):
        perimetro = self._n * self._lado

        return perimetro

#Classe Pentagono 
class Pentagon(Polygon):
    def __init__(self, tamanhoLado):
        super().__init__(5, tamanhoLado)

    def _validaLado(self, n):
        if n != 5:
            raise ValueError("Um pentágono deve ter exatamente 5 lados!")
        return n

    def _validaTamanhoLado(self, tamanhoLado):
        if tamanhoLado <= 0:
            raise ValueError("O comprimento do lado deve ser maior que zero!")
        return tamanhoLado

    def areaPolygon(self):
        apotema = self._lado / (2 * math.tan(math.pi / 5))
        area = (self.perimetroPolygon() * apotema) / 2
        return area

    def showPentagon(self):
        print(f"O seu pentágono foi criado com lados de comprimento {self._lado}, com área de {self.areaPolygon()} e perímetro de {self.perimetroPolygon()}!")


#Classe Hexagono
class Hexagon(Polygon):
    def __init__(self, tamanhoLado):
        super().__init__(6, tamanhoLado)

    def _validaLado(self, n):
        if n != 6:
            raise ValueError("Um hexágono deve ter exatamente 6 lados!")
        return n

    def _validaTamanhoLado(self, tamanhoLado):
        if tamanhoLado <= 0:
            raise ValueError("O comprimento do lado do hexágono deve ser maior que zero!")
        return tamanhoLado

    def areaPolygon(self):
        area = (3 * math.sqrt(3) * self._lado ** 2) / 2
        return area
    
    def perimetroPolygon(self):
        perimetro = 6 * self._lado
        return perimetro
    
    def showHexagon(self):
        print(f"O seu hexágono foi criado com lados de comprimento {self._lado}, com área de {self.areaPolygon()} e perímetro de {self.perimetroPolygon()}!")
    
#Classe Trapézio Isosceles
class TrapezioIsosceles:
    def __init__(self, baseMenor, baseMaior, altura):
        self._baseMenor = self._validaBase(baseMenor)
        self._baseMaior = self._validaBase(baseMaior)
        self._altura = self._validaAltura(altura)

    @staticmethod
    def _validaBase(base):
        if base <= 0:
            raise ValueError("A base do trapézio deve ser maior que zero!")
        return base
    
    @staticmethod
    def _validaAltura(altura):
        if altura <= 0:
            raise ValueError("A altura do trapézio deve ser maior que zero!")
        return altura

    @property
    def areaTrapIsos(self):
        area = ((self._baseMenor + self._baseMaior) * self._altura) / 2
        return area
    
    @property
    def ladoTrapIsos(self):
        aux = (self._baseMaior - self._baseMenor) / 2
        lado = (self._altura ** 2 + aux ** 2) ** 0.5
        return lado
    
    @property
    def perimetroTrapIsos(self):
        lado = self.ladoTrapIsos
        perimetro = lado * 2 + self._baseMenor + self._baseMaior
        return perimetro
    
    @property
    def alturaTrapIsos(self):
        return self._altura
    
    def showTrapIsos(self):
        altura = self.alturaTrapIsos
        area = self.areaTrapIsos
        perimetro = self.perimetroTrapIsos
        
        print(f"O seu trapézio isósceles foi criado com com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!")

#Classe Trapézio Retângulo
class TrapezioRetangulo(TrapezioIsosceles): 
    def __init__(self, baseMenor, baseMaior, altura):
        super().__init__(baseMenor, baseMaior, altura)
        self._color = self.colorTrapRet()

    def colorTrapRet(self):
        color = input("Digite a cor do trapézio retângulo: ")
        return color

    def ladoTrapRet(self):
        aux = self._baseMaior - self._baseMenor
        lado = math.sqrt(aux ** 2 + self._altura ** 2)
        return lado

    def perimetroTrapRet(self):
        lado = self.ladoTrapRet()
        perimetro = self._baseMaior + self._baseMenor + lado + self._altura
        return perimetro

    def showTrapRet(self):
        altura = self.alturaTrapIsos
        area = self.areaTrapIsos
        perimetro = self.perimetroTrapRet
        
        print(f"O seu trapézio retângulo foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!")


