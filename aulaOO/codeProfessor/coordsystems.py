from my_libraries.shapes2d import *


class CartesianBoard():
    
    """ Esta classe possui formas (objetos) aninhados"""
    """ Nela, o estudante deverá definir as operações de visualização
    das formas, interação, inserção, remoção e atualização das mesmas"""
    
    def __init__(self):
        
        self.shapes= {}
        
        
    def insertShape(self, shape):
        
        self.shapes[shape.getType() + str(shape.getNumber())]= shape
        
        
    def removeShape(self, shape):
        
        del self.shapes[shape.getType() + str(shape.getNumber())]
        
        
    def showShapes(self):
        
        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for shape in self.shapes.keys():
            print(shape)
    
    
    def printDetails(self):
        
        for key in self.shapes.keys():
            self.shapes[key].printCoord()
    
        
    def getShape(self,key):
        return self.shapes[key]
            
            
