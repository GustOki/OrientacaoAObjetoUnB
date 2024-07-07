from package.maths.terms import TrapezioRetangulo

def workspace():
    baseMenor = int(input("Digite a base menor do trapézio retângulo: "))
    baseMaior = int(input("Digite a base maior do trapézio retângulo: "))
    altura = int(input("Digite a altura do trapézio retângulo: "))

    trapRetObj = TrapezioRetangulo(baseMenor, baseMaior, altura)
    areaTrapRet = trapRetObj.areaTrapIsos()
    perimetroTrapRet = trapRetObj.perimetroTrapRet()
    getAlturaTrapRet = trapRetObj.getAltura()

    print(f"Área: {areaTrapRet}")
    print(f"Perímetro: {perimetroTrapRet}")
    print(f"Altura: {getAlturaTrapRet}")

if __name__ == "__main__":

    print("O arquivo 'testbenchTrapezioRet.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTrapezioRet.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')