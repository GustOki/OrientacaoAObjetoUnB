from package.maths.terms import Point, Circle

def workspace():
    ponto_1 = Point(5, 6)
    print(f'Distancia da origem = {ponto_1.distance()}')
    ponto_1.model()
    

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')