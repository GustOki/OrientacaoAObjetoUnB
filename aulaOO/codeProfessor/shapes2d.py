class Point():

    def __init__(self,n,x,y):
        self._n= n
        self._x= x
        self._y= y


    def updateCoord(self,x,y):
        self._x= x
        self._y= y

    
    def getType(self):
        return 'Point_'
        
        
    def getNumber(self):
        return self._n
    

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')        




class Circle(Point):
    
    """ O círculo herda do ponto suas funcionalidades e adiciona raio"""
    """ É necessário definir as funções membro para o círculo operar"""
    
    def __init__(self,n,x,y,radius):
        
        super().__init__(n, x, y)
        self.radius= radius
        
    
    def getType(self):
        """ Atencção!!! Polimorfismo aplicado"""
        return 'Circle_'
        
    
    def updateCoord(self,x,y,radius):
        
        super().updateCoord(x, y)
        self.radius= radius

    
    def printCoord(self):
        
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')
        
    
    def pointIn(self,pt):
        """ Verifica se o ponto está dentro deste círculo"""
        pass
    
    
    def area(self):
        """ calcula a área deste circulo e mostra no terminal"""
        pass
    
    
    def perimeter(self):
        """ calcula o perímetro deste círculo e mostra no terminal"""
        pass
    
    
    def my_function(self):
        """ defina mais funções de seu interesse aqui"""
        pass
    



class Line():
    
    """ implementar a linha com dois pontos internos"""     
    """ definir funções membro e quaisquer outros atributos da classe""" 
    pass




class SuaOutraForma():

    """ Defina quantas formas quiser utilizando as relações de herança"""
    pass
