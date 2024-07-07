from package.maths.terms import TriangleIsos

def workspace():
    x = int(input("Digite o valor do lado x: "))
    y = int(input("Digite o valor do lado y: "))
    z = int(input("Digite o valor do lado z: "))

    triIsosObj = TriangleIsos(x, y, z)
    
    area = triIsosObj.areaTriIsos()
    altura = triIsosObj._alturaTriIsos()
    perimetro = triIsosObj.perimetroTriEquil()

    print(f'Area: {area}')
    print(f'Altura: {altura}')
    print(f'Perimetro: {perimetro}')

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleIsos.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleIsos.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')