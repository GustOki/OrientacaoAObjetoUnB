from package.maths.terms import Line

def workspace():
    n = int(input("Digite o número de pontos na reta: "))

    lineObj = Line(n)
    m = lineObj.inclinacao()
    b = lineObj.CoefLinear(lineObj.inclinacao())

    print(f"O valor de m será: {m}")
    print(f"O valor de b será: {b}")

    i = int(input("Quantidade de iterações: "))
    lineObj.montarTabela(m, b, i)

    y = lineObj.interpolar(m, b, i)
    print(y)


if __name__ == "__main__":

    print("O arquivo 'testbenchLine.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchLine.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')