class Reta():


    def __init__(self,a,b):

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')
