from package.maths.terms import Hexagon

def workspace():
    lado = int(input("Digite o lado do hexagono: "))
    hexagonObj = Hexagon(lado)

    hexagonObj.showHexagon()

if __name__ == "__main__":

    print("O arquivo 'testbenchHexagon.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchHexagon.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')