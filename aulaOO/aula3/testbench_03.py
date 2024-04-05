from package.maths.terms import Point, Circle, Circle_2

def workspace():
    point_1 = Point(5, 6)
    print(f'Distancia da origem = {point_1.distance()}')
    
    circle_1 = Circle(2,3,6)
    circle_1.print()

    circle_2 = Circle_2(1, 5, 9)
    circle_2.print()
    

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')