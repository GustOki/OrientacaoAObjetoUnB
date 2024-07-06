from package.maths.terms import Circle

def workspace():
    circulo_1 = Circle(3, 7, 5)
    circulo_1.print()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')
