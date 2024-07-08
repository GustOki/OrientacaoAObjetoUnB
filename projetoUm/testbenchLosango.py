from package.maths.terms import Losango

def workspace():
    lado = int(input("Digite o lado do losango: "))
    diagMaior = int(input("Digite a diagonal maior do losango: "))
    diagMenor = int(input("Digite a diagonal menor do losango: "))

    losangoObj = Losango(lado, diagMaior, diagMenor)
    losangoObj.showLosango()

if __name__ == "__main__":

    print("O arquivo 'testbenchLosango.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchLosango.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')