from package.maths.terms import Pentagon

def workspace():
    lado = int(input("Digite o lado do pentagono: "))
    pentagonObj = Pentagon(lado)
    
    area = pentagonObj.areaPentagon()
    perimetro = pentagonObj.perimetroPolygon()
    
    print(f'Area {area}')
    print(f'Perimetro: {perimetro}')

if __name__ == "__main__":

    print("O arquivo 'testbenchPentagon.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchPentagon.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')