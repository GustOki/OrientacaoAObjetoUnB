from package.maths.terms import TriangleIsos

def workspace():
    ladosIguais = int(input("Digite os lados iguais do triângulo isósceles: "))
    base = int(input("Digite a base do triângulo isósceles: "))
    triIsosObj = TriangleIsos(ladosIguais, base)

    triIsosObj.showTriIsos()

if __name__ == "__main__":

    print("O arquivo 'testbenchTriangleIsos.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTriangleIsos.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')