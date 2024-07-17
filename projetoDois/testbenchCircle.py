from package.maths.terms import Circle, coordCircle

def workspace():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    coord = coordCircle(x, y)
    raio = int(input("Digite o raio: "))
    circleObj = Circle(coord.coordenadaX(), coord.coordenadaY(), raio)
    color = circleObj.colorCircle()
    circunf = circleObj.circunferenciaCircle()
    area = circleObj.areaCircle()
    diametro = circleObj.diametroCircle()

    circleObj.showCircle(color, circunf, diametro, area)


if __name__ == "__main__":

    print("O arquivo 'testbenchCircle.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchCircle.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')
