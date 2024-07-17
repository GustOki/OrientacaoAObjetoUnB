#from my_libraries.coordsystems import CartesianBoard


class Menu:

    def __init__(self):

        self.dashboard = CartesianBoard()
        self.actions = {
            'Criar_forma' : self.criar,
            'Interferencia_entre_formas': self.crash,
            'Sair' : exit
        }


    def criar(self):
        print('Estou criando uma forma geométrica...')
        pass


    def crash(self):
        print("Estou verificando a interferencia entre formas geométricas")
        pass


    def run(self):

         while True:
             print("Escolha uma opção:")
             print("1. Criar forma geométrica")
             print("2. Verificar interferências")
             print("3. Sair")
             escolha = input("Digite o número da opção selecionada")

             if escolha.isdigit() and int(escolha) in range(1,4):
                 selecao = list(self.actions.keys())[int(escolha)-1]
                 self.actions[selecao]()
             else:
                 print("Digite uma opçao válida.")
