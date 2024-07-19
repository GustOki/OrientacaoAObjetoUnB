from package.maths.terms import *

def workspace():
    formas = FigsGeom()

    while(True):
        print("\nSeja bem-vindo à interface de criação de formas geométricas!\n")
        print('\nDigite o número da forma geométrica que deseja criar ou opção:')
        print('1- Coordenada Única')
        print('2- Ponto')
        print('3- Reta')
        print('4- Círculo')
        print('5- Quadrado')
        print('6- Retângulo')
        print('7- Losango')
        print('8- Triângulo Escaleno')
        print('9- Triângulo Isósceles')
        print('10- Triângulo Equilátero')
        print('11- Polígono')
        print('12- Pentágono')
        print('13- Hexágono')
        print('14- Trapézio Isósceles')
        print('15- Trapézio Retângulo')
        print('16- Listar formas criadas')
        print('17- Remover forma criada')
        print('18- Sair')

        escolha = int(input("O que deseja fazer?: "))
        if escolha == 1:
            x = float(input("x: "))
            y = float(input("y: "))
            coord = coordUnique(x,y)
            formas.setForma(coord)
            escolha = 0
            
            print('\n[Coordenada única criada!!!] \n')

        elif escolha == 2:
            point = float(input("Ponto: "))
            ponto = Point(point)
            formas.setForma(ponto)
        
            print('\n[Ponto criado!!!] \n')
        
        elif escolha == 3:
            point = float(input("Pontos: "))
            reta = Line(point)
            formas.setForma(reta)
        
            print('\n[Reta criada!!!] \n')

        elif escolha == 4:
            pointX = float(input("Ponto X: "))
            pointY = float(input("Ponto Y: "))
            raio = float(input("Raio: "))
            circulo = Circle(pointX, pointY, raio)
            formas.setForma(circulo)
        
            print('\n[Círculo criado!!!] \n')
        
        elif escolha == 5:
            lado = float(input("Lado: "))
            quadrado = Square(lado)
            formas.setForma(quadrado)

            print('\n[Quadrado criado!!!] \n')

        elif escolha == 6:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            retangulo = Rectangle(base, altura)
            formas.setForma(retangulo)
            
            print('\n[Retangulo criado!!!] \n')

        elif escolha == 7:
            lado = float(input("Lado: "))
            diagMaior = float(input("Diagonal maior: "))
            diagMenor = float(input("Diagonal menor: "))
            losango = Losango(lado, diagMaior, diagMenor)
            formas.setForma(losango)
            
            print('\n[Losango criado!!!] \n')

        elif escolha == 8:
            pointX = float(input("Ponto x: "))
            pointY = float(input("Ponto y: "))
            pointZ = float(input("Ponto z: "))
            triEscaleno = TriangleEscaleno(pointX, pointY, pointZ)
            formas.setForma(triEscaleno)
            
            print('\n[Triângulo escaleno criado!!!] \n')

        elif escolha == 9:
            ladoIgual = float(input("Lados iguais: "))
            base = float(input("Base: "))
            triIsos = TriangleIsos(ladoIgual, base)
            formas.setForma(triIsos)
            
            print('\n[Triângulo isósceles criado!!!] \n')

        elif escolha == 10:
            lado = float(input("Lados: "))
            triEquil = TriangleEquil(lado)
            formas.setForma(triEquil)
            
            print('\n[Triângulo equilátero criado!!!] \n')

        elif escolha == 11:
            lados = float(input("Lados: "))
            tamanhoLado = float(input("Tamanho dos lados: "))
            poligono = Polygon(lados, tamanhoLado)
            formas.setForma(poligono)
            
            print('\n[Polígono criado!!!] \n')

        elif escolha == 12:
            tamanhoLado = float(input("Tamanho dos lados: "))
            pentagono = Pentagon(tamanhoLado)
            formas.setForma(pentagono)
            
            print('\n[Pentágono criado!!!] \n')

        elif escolha == 13:
            tamanhoLado = float(input("Tamanho dos lados: "))
            hexagono = Hexagon(tamanhoLado)
            formas.setForma(hexagono)
            
            print('\n[Hexágono criado!!!] \n')

        elif escolha == 14:
            baseMenor = float(input("Base menor: "))
            baseMaior = float(input("Base maior: "))
            altura = float(input("Altura: "))
            trapIsos = TrapezioIsosceles(baseMenor, baseMaior, altura)
            formas.setForma(trapIsos)
            
            print('\n[Trapézio isósceles criado!!!] \n')

        elif escolha == 15:
            baseMenor = float(input("Base menor: "))
            baseMaior = float(input("Base maior: "))
            altura = float(input("Altura: "))
            trapRet = TrapezioRetangulo(baseMenor, baseMaior, altura)
            formas.setForma(trapRet)
            
            print('\n[Trapézio isósceles criado!!!] \n')

        elif escolha == 16:
            formas.listFormas()
            print('\n')

        elif escolha == 17:
            key = input("Escolha a criação que você deseja apagar: ")
            formas.listFormas()
            formas.removeForma(key)
            print('\n')
        
        elif escolha == 18:
            print('\n Saindo... ')
            break

        
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando...")
            break
    
if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')