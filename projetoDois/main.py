from package.maths.terms import *

def workspace():
    formas = FigsGeom()

    while(True):
        print("\nSeja bem-vindo à interface de criação de formas geométricas!\n")
        print('\nDigite o número da forma geométrica que deseja criar ou opção:')
        print('1- Ponto')
        print('2- Reta')
        print('3- Círculo')
        print('4- Quadrado')
        print('5- Retângulo')
        print('6- Losango')
        print('7- Triângulo Equilátero')
        print('8- Triângulo Isósceles')
        print('9- Triângulo Escaleno')
        print('10- Polígono')
        print('11- Pentágono')
        print('12- Hexágono')
        print('13- Trapézio Isósceles')
        print('14- Trapézio Retângulo')
        print('15- Listar formas criadas')
        print('16- Remover forma criada')
        print('17- Mostrar detalhes de uma forma criada')
        print('18- Verificar relação ponto-forma')
        print('19- Verificar relação ponto-reta')
        print('20- Sair')

        escolha = int(input("O que deseja fazer?: "))
        if escolha == 1: #Ponto
            pontos = Point.criarPontos()
            
            for ponto in pontos:
                formas.setForma(ponto)
            
            Point.calcularDistancias(pontos)
        
            print('\n[Ponto criado!!!] \n')

        elif escolha == 2: #Reta
            num_points = int(input("Quantos pontos você deseja criar para a linha? "))
            points = []

            for i in range(num_points):
                color = input(f"Digite a cor do ponto {i}: ")
                x = int(input(f"Digite a coordenada X do ponto {i}: "))
                y = int(input(f"Digite a coordenada Y do ponto {i}: "))

                point = Point(color, (x, y))
                points.append(point)

            reta_color = input("Digite a cor da reta: ")
            reta_temp = Line(points, reta_color)
            formas.setForma(reta_temp)

            print('\n[Reta criada!!!] \n')
        
        elif escolha == 3: #Círculo
            pointX = int(input("Ponto X: "))
            pointY = int(input("Ponto Y: "))
            raio = int(input("Raio: "))

            circulo_temp = Circle(pointX, pointY, raio)
            color = circulo_temp.colorCircle()  

            circulo_temp.calcCircunferenciaCircle()
            circulo_temp.calcDiametroCircle()
            circulo_temp.calcAreaCircle()

            formas.setForma(circulo_temp)
        
            print('\n[Círculo criado!!!] \n')

        elif escolha == 4: # Quadrado
            lado = int(input("Tamanho do lado: "))

            square_temp = Square(lado)
            square_temp.colorSquare()
            square_temp.calcAreaSquare()
            square_temp.calcPerimetroSquare()

            formas.setForma(square_temp)

            print('\n[Quadrado criado!!!] \n')
        
        elif escolha == 5: #Retângulo
            ladoRectBase = int(input("Digite o tamanho da base do retângulo: "))
            ladoRectAlt = int(input("Digite o tamanho da altura do retângulo: "))

            rect_temp = Rectangle(ladoRectBase, ladoRectAlt)
            rect_temp.colorRectangle()
            rect_temp.areaRectangle()
            rect_temp.perimetroRectangle()

            formas.setForma(rect_temp)
            
            print('\n[Retangulo criado!!!] \n')

        elif escolha == 6: #Losango
            lado = int(input("Tamanho do lado: "))
            diagMaior = int(input("Diagonal maior: "))
            diagMenor = int(input("Diagonal menor: "))
            losango = Losango(lado, diagMaior, diagMenor)
            formas.setForma(losango)
    
            print('\n[Losango criado!!!] \n')

        elif escolha == 7: # Triângulo Equilátero
            lado = int(input("Tamanho do lado: "))
            triEquil = TriangleEquil(lado)
            formas.setForma(triEquil)
    
            print('\n[Triângulo escaleno criado!!!] \n')

        elif escolha == 8:  # Triângulo Isósceles
            ladoIgual = int(input("Lados iguais: "))
            base = int(input("Base: "))
            triIsos = TriangleIsos(ladoIgual, base)
            formas.setForma(triIsos)
            
            print('\n[Triângulo isósceles criado!!!] \n')

        elif escolha == 9:  # Triângulo Escaleno
            x = int(input("Lado X: "))
            y = int(input("Lado Y: "))
            z = int(input("Lado Z: "))
            
            try:
                triEscal = TriangleEscaleno(x, y, z)
                formas.setForma(triEscal)
            except ValueError as e:
                print(e)

            print('\n[Triângulo escaleno criado!!!] \n')

        elif escolha == 10: #Polígono
            lados = int(input("Lados: "))
            tamanhoLado = int(input("Tamanho dos lados: "))
            if lados == 5:
                poligono = Pentagon(tamanhoLado)
            elif lados == 6:
                poligono = Hexagon(tamanhoLado)
            else:
                print("Apenas pentágonos (5 lados) e hexágonos (6 lados) são suportados no momento.")
            formas.setForma(poligono)
            print('\n[Polígono criado!!!] \n')

        elif escolha == 11: #Pentágono
            tamanhoLado = int(input("Tamanho dos lados: "))
            pentagono = Pentagon(tamanhoLado)
            formas.setForma(pentagono)
            print('\n[Pentágono criado!!!] \n')

        elif escolha == 12: #Hexágono
            tamanhoLado = int(input("Tamanho dos lados: "))
            hexagono = Hexagon(tamanhoLado)
            formas.setForma(hexagono)
            print('\n[Hexágono criado!!!] \n')

        elif escolha == 13: # Trapézio Isósceles
            baseMenor = int(input("Base menor: "))
            baseMaior = int(input("Base maior: "))
            altura = int(input("Altura: "))
            trapIsos = TrapezioIsosceles(baseMenor, baseMaior, altura)
            formas.setForma(trapIsos)

            print('\n[Trapézio isósceles criado!!!] \n')

        elif escolha == 14: # Trapézio Retângulo
            baseMenor = int(input("Base menor: "))
            baseMaior = int(input("Base maior: "))
            altura = int(input("Altura: "))
            trapRet = TrapezioRetangulo(baseMenor, baseMaior, altura)
            formas.setForma(trapRet)
            
            print('\n[Trapézio retângulo criado!!!] \n')

        elif escolha == 15: #Listagem
            formas.listFormas()
            print('\n')

        elif escolha == 16: #Remoção
            formas.listFormas()
            key = int(input("Insira a key da forma geométrica que você queira apagar: "))
            
            if formas.removeForma(key):
                print(f'\nForma {key} removida!!! \n')            
            else:
                print(f'\nA forma geométrica com a key {key} não foi encontrada.\n')

        elif escolha == 17: #Detalhes
            formas.listFormas()
            print('\n')
            
            key = int(input("Digite o número da forma para mostrar detalhes: "))
            form = formas.returnForma(key)
            
            if form:
                showDetails(form)
            else:
                print("\n[Erro: Forma não encontrada!]\n")

        elif escolha == 18: # Verificar relação ponto-forma
            key_ponto = int(input("Digite o número do ponto: "))
            key_forma = int(input("Digite o número da forma geométrica (círculo ou retângulo): "))
            
            ponto = formas.returnForma(key_ponto)
            forma = formas.returnForma(key_forma)
            
            if isinstance(forma, Circle):
                print(f"O ponto está dentro do círculo? {'Sim' if forma.pointDentro(ponto) else 'Não'}") 
            elif isinstance(forma, Rectangle):
                print(f"O ponto está dentro do retângulo? {'Sim' if forma.pointDentro(ponto) else 'Não'}")
            else:
                print("Forma geométrica não suportada para esta verificação.")

        elif escolha == 19: # Verificar relação ponto-reta
            key_ponto = int(input("Digite o número do ponto: "))
            key_reta = int(input("Digite o número da reta: "))
            
            ponto = formas.returnForma(key_ponto)
            reta = formas.returnForma(key_reta)
            
            if isinstance(reta, Line):
                distancia = reta.distanciaPoint(ponto)
                proximidade = reta.segmPointProx(ponto)
                
                print(f"A distância do ponto à reta é: {distancia}")
                print(f"O ponto está próximo da reta? {'Sim' if proximidade else 'Não'}")
            else:
                print("Forma geométrica não suportada para esta verificação.")
        
        elif escolha == 20:
            print("Saindo...")
            
            break

def showDetails(form):
    if form.identif() == '_ponto':
        form.showPoint()
        distPointOrigem = form.distanciaOrigem()
        
        print(f"Distância até a origem: {distPointOrigem}")

    elif form.identif() == '_reta':
        form.showLine()

    elif form.identif() == '_circulo':
        form.showCircle()

    elif form.identif() == '_quadrado':
        form.showSquare()

    elif form.identif() == '_retangulo':
        form.showRectangle()

    elif form.identif() == '_losango':
        form.showLosango()

    elif form.identif() == '_trianguloEquilatero':
        form.showTriEquil()
    
    elif form.identif() == '_trianguloIsosceles':
        form.showTriIsos()
    
    elif form.identif() == '_trianguloEscaleno':
        form.showTriEsc()
    
    elif form.identif() == '_pentagono':
        form.showPentagon()
    
    elif form.identif() == '_hexagono':
        form.showHexagon()
    
    elif form.identif() == '_trapezioIsosceles':
        form.showTrapIsos()
    
    elif form.identif() == '_trapezioRetangulo':
        form.showTrapRet()
    
    else:
        print("Desculpe, não há muitos detalhes para mostrar...")
    
if __name__ == "__main__":
    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')