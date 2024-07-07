from package.maths.terms import TrapezioIsosceles

def workspace():
    baseMenor = int(input("Digite a base menor do trapézio isosceles: "))
    baseMaior = int(input("Digite a base maior do trapézio isosceles: "))
    altura = int(input("Digite a altura do trapézio isosceles: "))

    trapIsosObj = TrapezioIsosceles(baseMenor, baseMaior, altura)
    areaTrapIsos = trapIsosObj.areaTrapIsos()
    perimetroTrapIsos = trapIsosObj.perimetroTrapIsos()
    getAlturaTrapIsos= trapIsosObj.getAltura()

    print(f"Área: {areaTrapIsos}")
    print(f"Perímetro: {perimetroTrapIsos}")
    print(f"Altura: {getAlturaTrapIsos}")

if __name__ == "__main__":

    print("O arquivo 'testbenchTrapezioIsos.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchTrapezioIsos.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')