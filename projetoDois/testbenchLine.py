from package.maths.terms import Line

def workspace():
    n = int(input(f"Digite o números de pontos para a sua reta: "))
    lineObjt = Line(n)
    lenght = lineObjt.lenghtLine()
    color = lineObjt.colorLine()

    coefAng = lineObjt.inclinacaoLine() 
    coefLinear = lineObjt.coefLinear(lineObjt.inclinacaoLine())

    print(f"\nCoeficiente Angular: {coefAng}")
    print(f"Coeficiente Linear: {coefLinear}\n")

    i = int(input("Quantidade de iterações: "))
    
    y = lineObjt.interpolar(lineObjt.inclinacaoLine(), coefAng, i)

    lineObjt.showLine(lenght, color, coefAng, coefLinear, y)


if __name__ == "__main__":

    print("O arquivo 'testbenchLine.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchLine.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')