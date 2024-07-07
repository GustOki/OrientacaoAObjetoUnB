from package.maths.terms import Square

def workspace():
    squareNum = int(input("Digite o número do quadrado: "))
    lado = int(input("Digite o número para o comprimento do lado do quadrado: "))
    squareObj = Square(squareNum, lado)
    
    area = squareObj.area()
    perimetro = squareObj.perimetro()

    print(f'O quadrado nº {squareNum} tem os lados de comprimento {lado}, com área de {area} e perímetro de {perimetro}')

if __name__ == "__main__":

    print("O arquivo 'testbenchSquare.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchSquare.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')