from package.maths.terms import Circle

def workspace():
    circulo_1 = Circle(3, 7, 5, "vermelho")
    circulo_1.model()
    print(f'circunferencia: {circulo_1.circunferencia()}')
    print(f'area: {circulo_1.area()}')
    print(f'diametro: {circulo_1.diametro()}')

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

    

