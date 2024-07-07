from package.maths.terms import Rectangle

def workspace():
    rectNum = int(input("Digite o número do retângulo: "))
    rectBase = int(input("Digite o número da base do retângulo: "))
    rectAlt = int(input("Digite o número da altura do retângulo:"))
    rectObj = Rectangle(rectNum, rectBase, rectAlt)

    area = rectObj.area()
    perimetro = rectObj.perimetro()

    print(f'O retângulo nº {rectNum} possui {rectBase} de base e {rectAlt} de altura, com área {area} de área e {perimetro} de perímetro.')

if __name__ == "__main__":

    print("O arquivo 'testbenchRectangle.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchRectangle.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')