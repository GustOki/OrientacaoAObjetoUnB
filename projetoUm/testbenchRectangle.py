from package.maths.terms import Rectangle

def workspace():
    rectBase = int(input("Digite o número da base do retângulo: "))
    rectAlt = int(input("Digite o número da altura do retângulo: "))
    rectObj = Rectangle(rectBase, rectAlt)
    area = rectObj.areaRectangle()
    perimetro = rectObj.perimetroRectangle()

    rectObj.showRectangle(area, perimetro)

if __name__ == "__main__":

    print("O arquivo 'testbenchRectangle.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchRectangle.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')