from package.maths.terms import Point

def workspace():
    qtd = int(input(f"Digite a quantidade de pontos: "))
    pointObj = Point(qtd)

    color = pointObj.color()
    coord = pointObj.coordenada()
    print(f"Cores: {color}\n")
    print(f"Coordenadas: {coord}\n")

    pointObj.setPointX(coord)
    pointObj.setPointY(coord)

    x = pointObj.returnPointX(coord)
    y = pointObj.returnPointY(coord)
    print(f'{x}')
    print(f'{y}')
    print(f"Novas coordenadas: {coord}")

if __name__ == "__main__":

    print("O arquivo 'testbenchPoint.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchPoint.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')