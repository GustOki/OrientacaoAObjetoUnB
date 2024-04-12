class Reta():

    def __init__(self,a,b):

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: a={self.a}, b={self.b}')


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
        return(self._x**2 + self._y**2)**(0.5)
    
    def print(self):
        print(f'Eu sou um ponto e minhas coordenadas são: x = {self._x} e y = {self._y}')

class Circle(Point):
    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self._raio = raio

    def print(self):
        print(f'Eu sou um círculo e minhas coordenadas são: x = {self._x} e y = {self._y}. O meu raio é {self._raio}')

#segundo modelo
class Circle_2():
    def __init__(self, x, y, raio):
        self._origem = Point(x, y)
        self._raio = raio

    def print(self):
        print(f'Eu sou um segundo modelo para o circulo. Minhas coordenadas são: x = {self._origem.getX()} e y = {self._origem.getY()}. Meu raio é {self._raio}')


# MEU CODIGO RASCUNHO
# class Circle():
#     def __init__(self, r, x, y, color):
#         self.r = r
#         self.x = x
#         self.y = y
#         self.color = color


#     def circunferencia(self):
#         circunferencia = (2 * 3.14) * self.r
#         return circunferencia

#     def area(self):
#         area = 3.14 * pow(self.r, 2)
#         return area

#     def diametro(self):
#         diametro = self.r * 2
#         return diametro

#     def model(self):
#         print(f'Os parâmetros do meu modelo de circulo são: r={self.r}, x={self.x}, y={self.y} e cor={self.color}.')