from package.maths.terms import Circle, coordCircle

def workspace():
    coord = coordCircle()
    raio = float(input("Digite o raio: "))

    circleObj = Circle(coord.coordenadaX(),coord.coordenadaY(), raio)
    circunf = circleObj.circunferenciaCircle()
    print(f"Circunferencia: {circunf}")
    
    area = circleObj.areaCircle()
    print(f"Area: {area}")
    
    diametro = circleObj.diametroCircle()
    print(f"Diametro: {diametro}")

if __name__ == "__main__":

    print("O arquivo 'testbenchCircle.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchCircle.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')
