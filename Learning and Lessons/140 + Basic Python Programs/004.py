# Insira duas variáveis
a = input("Digite o valor da segunda variável (a): ")
b = input("digite o valor da segunda variável (b): ")
# Impressão dos valores
print(f"valores de a = {a} e b = {b}")
# Troca dos valores utilisando uma variável temporária
temp = a
a = b
b = temp
# Impressão dos valores trocados
print(f"Valores trocados: a = {a} e b = {b}")