import math

#Classe Ponto
class Point():
    def __init__(self, color = None, coord = None):
        self.color = color
        self.coord = coord

    def setColorPoint(self):
        self.color = input("Digite a cor do seu ponto: ")
        
        return self.color

    def setCoordPoint(self):
        x = int(input("Digite a coordenada de X: "))
        y = int(input("Digite a coordenada de Y: "))
        self.coord = (x, y)
        
        return self.coord

    def getCoordPoint(self):
        return self.coord

    def getColorPoint(self):
        return self.color

    def returnPointX(self):
        return self.coord[0] if self.coord else None

    def returnPointY(self):
        return self.coord[1] if self.coord else None

    def showPoint(self):
        if self.coord and self.color:
            print(f"O ponto criado tem a coordenada {self.coord} e cor {self.color}!")
        else:
            print("O ponto não foi definido completamente.")

    def identif(self):
        return '_ponto'
    
    def distanciaOrigem(self):
        if self.coord:
            return math.sqrt(self.coord[0]**2 + self.coord[1]**2)
        
        return None
    
    def distanciaPoint(self, other):
        if self.coord and other.coord:
            return math.sqrt((self.coord[0] - other.coord[0])**2 + (self.coord[1] - other.coord[1])**2)
        
        return None

    @staticmethod
    def criarPontos():
        pontos = []
        while True:
            ponto_temp = Point()
            ponto_temp.setColorPoint()
            ponto_temp.setCoordPoint()
            pontos.append(ponto_temp)
            continuar = input("Deseja criar outro ponto? (s/n): ")
            if continuar.lower() != 's':
                break
        
        return pontos

    def calcularDistancias(pontos):
        if len(pontos) < 2:
            print("Você precisa criar pelo menos dois pontos para calcular a distância entre eles.")
            return

        for i in range(len(pontos)):
            for j in range(i + 1, len(pontos)):
                dist = pontos[i].distanciaPoint(pontos[j])
                print(f"A distância entre o ponto {i+1} {pontos[i].coord} e o ponto {j+1} {pontos[j].coord} é: {dist}")

#Classe Reta
class Line():
    def __init__(self, points, color):
        self.points = points
        self.color = color

    def lenghtLine(self): 
        if len(self.points) >= 2:
            p1, p2 = self.points[0].getCoordPoint(), self.points[1].getCoordPoint()
            deltaX = p2[0] - p1[0]
            deltaY = p2[1] - p1[1]
            tamanho = math.sqrt(deltaX**2 + deltaY**2)
            
            return tamanho
        else:
            return "Não há pontos suficientes para formar uma linha."

    def inclinacaoLine(self):
        if len(self.points) >= 2:
            p1, p2 = self.points[0].getCoordPoint(), self.points[1].getCoordPoint()
            deltaX = p2[0] - p1[0]
            deltaY = p2[1] - p1[1]
            if deltaX != 0:
                inclinacao = deltaY / deltaX
                return inclinacao
            else:
                return 'O seu deltaX é = 0, tente outro caso!'
        
        elif len(self.points) == 1:
            p1 = self.points[0].getCoordPoint()
            inclinacao = p1[1] / p1[0] if p1[0] != 0 else 'Indefinido'
            
            return inclinacao

    def coefLinear(self, coefAng):
        if isinstance(coefAng, float):
            p1 = self.points[0].getCoordPoint()
            coefLinear = p1[1] - p1[0] * coefAng
            
            return coefLinear
        else:
            return "Coeficiente angular inválido."

    def interpolar(self, coefAng, coefLinear, x):
        y = coefAng * x + coefLinear
        return y
    
    def showLine(self):
        lenght = self.lenghtLine()
        inclinacao = self.inclinacaoLine()
        coefAng = inclinacao if isinstance(inclinacao, float) else "Indefinida"
        coefLinear = self.coefLinear(coefAng) if isinstance(coefAng, float) else "Indefinido"
        interpolacao = self.interpolar(coefAng, coefLinear, 0) if isinstance(coefAng, float) else "Indefinida"

        return print(f"\nA sua reta foi criada com {lenght} de tamanho e de cor {self.color}! Tendo como coeficiente angular: {coefAng}, coeficiente linear: {coefLinear} e com interpolação: {interpolacao}.\n")

    def identif(self):
        return '_reta'
    
    def distanciaPoint(self, point):
        if len(self.points) >= 2 and point.coord:
            x0, y0 = point.coord
            p1, p2 = self.points[0].getCoordPoint(), self.points[1].getCoordPoint()
            x1, y1 = p1
            x2, y2 = p2
            num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
            den = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
            
            return num / den
        
        return None

    def segmPointProx(self, point, tolerance=1e-6):
        if len(self.points) >= 2 and point.coord:
            x0, y0 = point.coord
            p1, p2 = self.points[0].getCoordPoint(), self.points[1].getCoordPoint()
            x1, y1 = p1
            x2, y2 = p2
            
            if x1 == x2:
                return min(y1, y2) - tolerance <= y0 <= max(y1, y2) + tolerance
            elif y1 == y2:
                return min(x1, x2) - tolerance <= x0 <= max(x1, x2) + tolerance
            else:
                lambda1 = (x0 - x1) / (x2 - x1)
                lambda2 = (y0 - y1) / (y2 - y1)
                
                return abs(lambda1 - lambda2) <= tolerance and 0 <= lambda1 <= 1 and 0 <= lambda2 <= 1
       
        return False

#Classe Circulo
class Circle():
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio
        self.color = None
        self.circunf = None
        self.diametro = None
        self.area = None

    def colorCircle(self):
        self.color = str(input(f"Digite a cor do círculo: "))
        return self.color

    def calcCircunferenciaCircle(self):
        self.circunf = 2 * math.pi * self.raio
        return self.circunf

    def calcDiametroCircle(self):
        self.diametro = 2 * self.raio
        return self.diametro

    def calcAreaCircle(self):
        self.area = math.pi * (self.raio ** 2)
        return self.area
    
    def showCircle(self):
        if self.color is None:
            self.colorCircle()
        if self.circunf is None:
            self.calcCircunferenciaCircle()
        if self.diametro is None:
            self.calcDiametroCircle()
        if self.area is None:
            self.calcAreaCircle()
        
        print(f"\nO seu círculo foi criado com {self.circunf:.2f} de circunferência e de cor {self.color}, com um diâmetro de {self.diametro:.2f} e uma área de {self.area:.2f}!\n")

    def identif(self):
        return '_circulo'
    
    def pointDentro(self, point):
        if point.coord:
            dist = math.sqrt((point.coord[0] - self.x)**2 + (point.coord[1] - self.y)**2)
            return dist <= self.raio
        
        return False

#Classe Quadrado
class Square():
    def __init__(self, __lado):
        self.__lado = self._validaLado(__lado)
        self.color = None
        self.area = None
        self.perimetro = None

    def colorSquare(self):
        self.color = str(input(f"Digite a cor do quadrado: "))

    def _validaLado(self, lado):
        if lado <= 0:
            raise ValueError("Atenção, o lado do quadrado deve ser maior que zero!")
        
        return lado

    def calcAreaSquare(self):
        self.area = self.__lado ** 2

    def calcPerimetroSquare(self):
        self.perimetro = self.__lado * 4

    def showSquare(self):
        if self.color is None or self.area is None or self.perimetro is None:
            self.colorSquare()
            self.calcAreaSquare()
            self.calcPerimetroSquare()
        
        print(f'\nO seu quadrado foi criado com cor {self.color} e com os lados de comprimento {self.__lado}, com área de {self.area} e perímetro de {self.perimetro}!\n')

    def identif(self):
        return '_quadrado'
    
#Classe Retangulo
class Rectangle():
    def __init__(self, rectBase, rectAlt):
        self.rectBase = self._validaLado(rectBase)
        self.rectAlt = self._validaLado(rectAlt)
        self.color = None
        self.area = None
        self.perimetro = None

    def colorRectangle(self):
        self.color = str(input(f"Digite a cor do retângulo: "))

    def _validaLado(self, lado):
        if lado <= 0:
            raise ValueError("Atenção, o lado do retângulo deve ser maior que zero!")
        
        return lado

    def areaRectangle(self):
        self.area = self.rectBase * self.rectAlt

    def perimetroRectangle(self):
        self.perimetro = 2 * (self.rectBase + self.rectAlt)

    def showRectangle(self):
        if self.color is None or self.area is None or self.perimetro is None:
            self.colorRectangle()
            self.areaRectangle()
            self.perimetroRectangle()

        print(f'\nO seu retângulo foi criado com cor {self.color} e com base de comprimento {self.rectBase} e altura de {self.rectAlt}, com área de {self.area} e perímetro de {self.perimetro}!\n')

    def identif(self):
        return '_retangulo'
    
    def pointDentro(self, point):
        if point.coord:
            x, y = point.coord
            return self.x <= x <= self.x + self.rectBase and self.y <= y <= self.y + self.rectAlt
        
        return False
    

#Classe Losango
class Losango(Square):
    def __init__(self, __lado, diagMaior, diagMenor):
        super().__init__(__lado)
        self.diagMaior = self._validaDiag(diagMaior)
        self.diagMenor = self._validaDiag(diagMenor)
        self.color = self.colorLosango()

    def colorLosango(self):
        color = input("Digite a cor do losango: ")
        return color

    def areaLosango(self):
        area = (self.diagMaior * self.diagMenor) / 2
        return area

    def _validaDiag(self, diag):
        if diag <= 0:
            raise ValueError("Atenção, a diagonal deve ser maior que zero!")
        
        return diag

    def showLosango(self):
        area = self.areaLosango()
        print(f'\nO seu losango foi criado com cor {self.color} e área de {area}!\n')

    def identif(self):
        return '_losango'
    
#Classe Triângulo Equilatero
class TriangleEquil():
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        
        self.lado = lado
        self.color = self.colorTriEquil()

    def colorTriEquil(self):
        color = input("Digite a cor do triângulo equilátero: ")
        return color
    
    def triEquilEhValido(self):
        return self.lado > 0
    
    def ehEquil(self):
        return True

    def alturaTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            altura = (self.lado * (3 ** 0.5)) / 2
            return altura
        else:
            return "As entradas não são válidas!"

    def areaTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            area = ((self.lado ** 2) * (3 ** 0.5)) / 4
            return area
        else:
            return "As entradas não são válidas!"

    def perimetroTriEquil(self):
        if self.triEquilEhValido() and self.ehEquil():
            perimetro = self.lado * 3
            return perimetro
        else:
            return "As entradas não são válidas!"
        
    def showTriEquil(self):
        altura = self.alturaTriEquil()
        area = self.areaTriEquil()
        perimetro = self.perimetroTriEquil()
        
        print(f"\nO seu triângulo equilátero foi criado com cor {self.color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!\n")

    def identif(self):
        return '_trianguloEquilatero'

class TriangleIsos(TriangleEquil):
    def __init__(self, ladoIgual, base):
        super().__init__(ladoIgual)
        self.base = self._validaBase(base)
        self.color = self.colorTriIsos()

    def colorTriIsos(self):
        color = input("Digite a cor do triângulo isósceles: ")
        return color

    def _validaBase(self, base):
        if base <= 0 or base >= 2 * self.lado:
            raise ValueError("A base do triângulo isósceles deve ser maior que zero e menor que duas vezes o lado igual.")
        
        return base

    def alturaTriIsos(self):
        altura = (self.lado ** 2 - (self.base ** 2 / 4)) ** 0.5
        return altura

    def areaTriIsos(self):
        area = (self.base * self.alturaTriIsos()) / 2
        return area
    
    def perimetroTriIsos(self):
        perimetro = self.lado * 2 + self.base
        return perimetro
    
    def showTriIsos(self):
        altura = self.alturaTriIsos()
        area = self.areaTriIsos()
        perimetro = self.perimetroTriIsos()
        
        print(f"\nO seu triângulo isósceles foi criado com cor {self.color}, com uma altura de {altura:.2f}, uma área de {area:.2f} e um perímetro de {perimetro:.2f}.\n")

    def identif(self):
        return '_trianguloIsosceles'
        
#Classe Triangulo Escaleno
class TriangleEscaleno():
    def __init__(self, x, y, z):
        self.x = self._verificaLado(x)
        self.y = self._verificaLado(y)
        self.z = self._verificaLado(z)
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
        return (self.x + self.y > self.z and 
                self.y + self.z > self.x and 
                self.z + self.x > self.y and 
                self.x != self.y and 
                self.y != self.z and 
                self.x != self.z)
        
    def _menorAngulo(self):
        m = min(self.x, self.y, self.z)
        aux = 180 / (self.x + self.y + self.z)
        menorTeta = aux * m
        
        return menorTeta
        
    def _maiorAngulo(self):
        m = max(self.x, self.y, self.z)
        aux = 180 / (self.x + self.y + self.z)
        maiorTeta = aux * m
        
        return maiorTeta

    def angulosInternos(self):
        menorTeta = self._menorAngulo()
        maiorTeta = self._maiorAngulo()
        TetaMeio = 180 - menorTeta - maiorTeta
        
        print(f"{maiorTeta:.2f}, {menorTeta:.2f}, {TetaMeio:.2f}")

    def alturaTriEsc(self): 
        if self._verificaDiferenca():
            a = math.radians(self._menorAngulo())
            altura = self.z * math.sin(a)
            return altura
        else:
            return "As entradas não são válidas!"

    def areaTriEsc(self):
        if self._verificaDiferenca():
            altura = self.alturaTriEsc()
            area = (self.z * altura) / 2
            return area
        else:
            return "As entradas não são válidas!"

    def perimetroTriEsc(self):
        if self._verificaDiferenca():
            perimetro = self.x + self.y + self.z
            return perimetro
        else: 
            return "As entradas não são válidas!"
        
    def showTriEsc(self):
        altura = self.alturaTriEsc()
        area = self.areaTriEsc()
        perimetro = self.perimetroTriEsc()
        
        print(f"\nO seu triângulo escaleno foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!\n")

    def identif(self):
        return '_trianguloEscaleno'


from abc import ABC, abstractmethod
#Classe Poligono        
class Polygon(ABC):
    def __init__(self, n, tamanhoLado):
        self.n = self._validaLado(n)
        self.lado = self._validaTamanhoLado(tamanhoLado)

    @staticmethod
    def _validaLado(n):
        if n < 3:
            raise ValueError("O polígono deve ter pelo menos 3 lados!")
        
        return n

    @staticmethod
    def _validaTamanhoLado(tamanhoLado):
        if tamanhoLado <= 0:
            raise ValueError("O comprimento do lado deve ser maior que zero!")
        
        return tamanhoLado

    @abstractmethod
    def areaPolygon(self):
        pass

    def perimetroPolygon(self):
        return self.n * self.lado
    
    def identif(self):
        return '_poligono'

#Classe Pentagono 
class Pentagon(Polygon):
    def __init__(self, tamanhoLado):
        super().__init__(5, tamanhoLado)

    def areaPolygon(self):
        apotema = self.lado / (2 * math.tan(math.pi / 5))
        area = (self.perimetroPolygon() * apotema) / 2
        
        return area

    def showPentagon(self):
        print(f"\nO seu pentágono foi criado com lados de comprimento {self.lado}, com área de {self.areaPolygon()} e perímetro de {self.perimetroPolygon()}!\n")

    def identif(self):
        return '_pentagono'

#Classe Hexagono
class Hexagon(Polygon):
    def __init__(self, tamanhoLado):
        super().__init__(6, tamanhoLado)

    def areaPolygon(self):
        area = (3 * math.sqrt(3) * self.lado ** 2) / 2
        return area
    
    def showHexagon(self):
        print(f"\nO seu hexágono foi criado com lados de comprimento {self.lado}, com área de {self.areaPolygon()} e perímetro de {self.perimetroPolygon()}!\n")

    def identif(self):
        return '_hexagono'
    
#Classe Trapézio Isosceles
class TrapezioIsosceles():
    def __init__(self, baseMenor, baseMaior, altura):
        self.baseMenor = self._validaBase(baseMenor)
        self.baseMaior = self._validaBase(baseMaior)
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
        area = ((self.baseMenor + self.baseMaior) * self._altura) / 2
        return area
    
    @property
    def ladoTrapIsos(self):
        aux = (self.baseMaior - self.baseMenor) / 2
        lado = (self._altura ** 2 + aux ** 2) ** 0.5
        
        return lado
    
    @property
    def perimetroTrapIsos(self):
        lado = self.ladoTrapIsos
        perimetro = lado * 2 + self.baseMenor + self.baseMaior
        
        return perimetro
    
    @property
    def alturaTrapIsos(self):
        return self._altura
    
    def showTrapIsos(self):
        altura = self.alturaTrapIsos
        area = self.areaTrapIsos
        perimetro = self.perimetroTrapIsos
        
        print(f"\nO seu trapézio isósceles foi criado com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!\n")

    def identif(self):
        return '_trapezioIsosceles'

class TrapezioRetangulo(TrapezioIsosceles): 
    def __init__(self, baseMenor, baseMaior, altura):
        super().__init__(baseMenor, baseMaior, altura)
        self._color = self.colorTrapRet()

    def colorTrapRet(self):
        color = input("Digite a cor do trapézio retângulo: ")
        return color

    def __ladoTrapRet(self):
        aux = self.baseMaior - self.baseMenor
        lado = math.sqrt(aux ** 2 + self._altura ** 2)
        
        return lado

    def perimetroTrapRet(self):
        lado = self.__ladoTrapRet()
        perimetro = self.baseMaior + self.baseMenor + lado + self._altura
        
        return perimetro

    def showTrapRet(self):
        altura = self.alturaTrapIsos
        area = self.areaTrapIsos
        perimetro = self.perimetroTrapRet()
        
        print(f"\nO seu trapézio retângulo foi criado com cor {self._color}, com uma altura de {altura}, com {area} de área e {perimetro} de perímetro!\n")

    def identif(self):
        return '_trapezioRetangulo'


class FigsGeom():
    def __init__(self):
        self.forms = {}
        self.count = 0
    
    def setForma(self, instancia):
        self.count += 1
        self.forms[self.count] = instancia
    
    def removeForma(self, key):
        if key in self.forms:
            del self.forms[key]
            return True
        else:
            return False

    def listFormas(self):
        if not self.forms:
            print("Ops, nenhuma forma geométrica foi criada ainda...")
        else:
            for key, form in self.forms.items():
                print(f"{key}: {form.identif()}")
    
    def returnForma(self, key):
        return self.forms.get(key, None)
