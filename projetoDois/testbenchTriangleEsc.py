from package.maths.terms import TriangleEscaleno

def workspace():
    x = int(input("Digite o valor do lado x do triângulo escaleno: "))
    y = int(input("Digite o valor do lado y do triângulo escaleno: "))
    z = int(input("Digite o valor do lado z do triângulo escaleno: "))

    triEscObj = TriangleEscaleno(x, y, z)

    triEscObj.showTriEsc()

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleEsc.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleEsc.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')