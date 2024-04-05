from package.maths.terms import Point

def workspace():
    ponto_1 = Point(5, 6, "vermelho", "A")
    ponto_1.model()

    ponto_2 = Point(12, 20, "verde", "B")
    ponto_2.model()

    distancia = pow((ponto_2.x - ponto_1.x), 2) + pow((ponto_2.y - ponto_1.y), 2)
    print(f'A distancia entre os pontos P{ponto_1.name} e P{ponto_2.name} é de {distancia}cm.')
    

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')