from package.maths.terms import Point, Circle

def workspace():
    point_1 = Point(5, 6)
    print(f'Distancia da origem = {point_1.distance()}')
    
    circle_1 = Circle(2,3,6)
    circle_1.print()
    

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')