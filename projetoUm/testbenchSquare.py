from package.maths.terms import Square

def workspace():
    lado = int(input("Digite o número para o comprimento do lado do quadrado: "))
    squareObj = Square(lado)
    
    color = squareObj.colorSquare()
    area = squareObj.areaSquare()
    perimetro = squareObj.perimetroSquare()

    squareObj.showSquare(lado, color, area, perimetro)


if __name__ == "__main__":

    print("O arquivo 'testbenchSquare.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchSquare.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')