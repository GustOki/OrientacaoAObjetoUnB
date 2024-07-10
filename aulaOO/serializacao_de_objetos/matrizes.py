import pickle
from package.matlab import M22

# Criando as matrizes m1 e m2
m1 = M22.new("[1.0, 2.0; 2.0, 1.0]")  # Exemplo de criação de m1
m2 = M22(2.0, 3.0, 4.0, 5.0)  # Exemplo de criação de m2

# Realizando a operação entre as matrizes (exemplo: soma)
result = m1 + m2

print("As matrizes foram definidas:")
print(m1)
print(m2)
print(f"O resultado da soma é {result}")


print(f"A matriz m1 é simétrica? {M22.eh_simetrica(m1)}")
print(f"A matriz m2 é simétrica? {M22.eh_simetrica(m2)}")


# Salvando as matrizes e o resultado em disco
with open('dados.txt', 'wb') as file:
    pickle.dump(m1, file)
    pickle.dump(m2, file)
    pickle.dump(result, file)

print("As matrizes foram armazenadas em disco (arquivo: dados.txt)")

