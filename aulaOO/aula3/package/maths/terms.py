class Reta():

    def __init__(self,a,b):

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: a={self.a}, b={self.b}')

class Circle():
    def __init__(self, r, x, y, color):
        self.r = r
        self.x = x
        self.y = y
        self.color = color


    def circunferencia(self):
        circunferencia = (2 * 3.14) * self.r
        return circunferencia

    def area(self):
        area = 3.14 * pow(self.r, 2)
        return area

    def diametro(self):
        diametro = self.r * 2
        return diametro

    def model(self):
        print(f'Os parâmetros do meu modelo de circulo são: r={self.r}, x={self.x}, y={self.y} e cor={self.color}.')

class Point():
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
    
    def model(self):
        print(f'Os parâmetros do meu modelo de ponto são: coordenada=({self.x}, {self.y}), cor {self.color} e com o nome de P{self.name}')
        