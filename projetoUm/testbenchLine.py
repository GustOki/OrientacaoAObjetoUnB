from package.maths.terms import Line

def workspace():
    n = int(input("digite a qtd de pontos na reta: "))

    obj_Reta = Line(n) 
    m = obj_Reta.inclinacaoLine() #
    b = obj_Reta.coefLinear(obj_Reta.inclinacaoLine()) #associação.

    print(f"m: {m}")
    print(f"b: {b}")

    i = int(input("quantidade de iterações:"))
    obj_Reta.montarTabela(m,b,i)
    
    y = obj_Reta.interpolar(obj_Reta.inclinacaoLine(),b,i) #associação, pois usa a inclinação, mas não chega a possui-la
    print(f'interpolar, y = {y}')


if __name__ == "__main__":

    print("O arquivo 'testbenchLine.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbenchLine.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')