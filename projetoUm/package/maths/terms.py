class Reta():

    def __init__(self,a,b, color):

        self.a = a
        self.b = b
        self.color = color


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: a={self.a}, b={self.b} e de cor {self.color}!')
