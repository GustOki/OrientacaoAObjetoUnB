from package.maths.terms import TriangleEquil

def workspace():
    x = int(input("Digite o valor do lado x: "))
    y = float(input("Digite o valor do lado y: "))
    z = float(input("Digite o valor do lado z: "))

    triEquilObj = TriangleEquil(x, y, z)
    area = triEquilObj.areaTriEquil()
    altura = triEquilObj.alturaTriEquil()
    perimetro = triEquilObj.perimetroTriEquil()

    print(f'Area: {area}')
    print(f'Altura: {altura}')
    print(f'Perimetro: {perimetro}')

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleEquil.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleEquil.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')