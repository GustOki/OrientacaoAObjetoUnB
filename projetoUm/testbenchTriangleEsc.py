from package.maths.terms import TriangleEscaleno

def workspace():
    x = int(input("Digite o valor do lado x: "))
    y = int(input("Digite o valor do lado y: "))
    z = int(input("Digite o valor do lado z: "))

    triEscObj = TriangleEscaleno(x, y, z)
    
    triEscObj.angulosInternos()
    area = triEscObj.areaTriEsc()
    altura = triEscObj.alturaTriEsc()
    perimetro = triEscObj.perimetroTriEsc()

    print(f'Area: {area}')
    print(f'Altura: {altura}')
    print(f'Perimetro: {perimetro}')

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleEsc.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleEsc.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')