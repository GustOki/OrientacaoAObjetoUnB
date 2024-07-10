class Pessoa:
    total_pessoas = 0
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

    @classmethod
    def total(cls):
        return cls.total_pessoas
    
    def apresentar(self):
        return f"Olá meu nome é {self.nome} e tenho {self.idade} anos."
    

#Criando instâncias
pessoa1 = Pessoa("Ana", 30)
pessoa2 = Pessoa("Jorge", 19)

#Chamando o mét. de classe total()
print(f'Total de pessoas: {Pessoa.total()}')

#Chamando o mét de instância apresentar()
print(pessoa1.apresentar())
print(pessoa2.apresentar())