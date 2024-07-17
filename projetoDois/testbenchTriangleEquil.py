from package.maths.terms import TriangleEquil

def workspace():
    lado = int(input("Digite o lado do triângulo equilátero: "))
    
    triEquilObj = TriangleEquil(lado)

    triEquilObj.showTriEquil()

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleEquil.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleEquil.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')