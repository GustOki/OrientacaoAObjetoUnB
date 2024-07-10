import sys
import pickle
from package.matlab import M22

if len(sys.argv) < 2:
    print("Por favor, forneça o nome do arquivo como argumento.")
else:
    file_name = sys.argv[1]  # O primeiro argumento é o nome do arquivo

    # Carregando os objetos do arquivo
    with open(file_name, 'rb') as file:
        m1 = pickle.load(file)
        m2 = pickle.load(file)
        result = pickle.load(file)

    # Exibindo os objetos carregados
    print("Matriz m1:")
    print(m1)
    print("Matriz m2:")
    print(m2)
    print(f"Resultado da operação entre m1 e m2:")
    print(result)

