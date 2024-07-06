from package.maths.terms import Line

def workspace():

    segmento_1 = Line(3, 7, "verde")
    segmento_1.model()
    print(f'Interpolando o valor 4: y = {segmento_1.interpolar(4)}')



if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')