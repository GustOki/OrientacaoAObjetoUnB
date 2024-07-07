from package.maths.terms import Losango

def workspace():
    num = int(input("Digite o número do losango: "))
    lado = int(input("Digite o lado do losango: "))
    diagMaior = int(input("Digite a diagonal maior do losango: "))
    diagMenor = int(input("Digite a diagonal menor do losango: "))

    losangoObj = Losango(num ,lado, diagMaior, diagMenor)

    area = losangoObj.areaLosango()
    print(f"Area: {area}")

    perimetro = losangoObj.perimetro()
    print(f"Perimetro: {perimetro}")

if __name__ == "__main__":

    print("O arquivo 'testbenchLosango.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchLosango.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')