from package.maths.terms import Point

def workspace():
    numPoints = int(input("Digite o número de pontos: "))
    pointObj = Point(numPoints)

    color = pointObj.colorPoint()
    coord = pointObj.coordPoint()
    print(f"\nCores: {color}")
    print(f"Coordenadas: {coord}\n") 

    vetorPointX = pointObj.returnPointX(coord)
    vetorPointY = pointObj.returnPointY(coord)
    print(f"{vetorPointX}")
    print(f"{(vetorPointY)}\n")

    pointObj.showPoint(coord, color)

if __name__ == "__main__":

    print("O arquivo 'testbenchPoint.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchPoint.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')