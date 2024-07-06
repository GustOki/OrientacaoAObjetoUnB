from package.maths.terms import Point

def workspace():
    point_1 = Point(5, 6)
    point_1.model()
    print(f'Distancia da origem = {point_1.distance()}')

if __name__ == "__main__":

    print("O arquivo 'testbenchPoint.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchPoint.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')