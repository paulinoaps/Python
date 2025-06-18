quilometros = float(input("Insira a distância em quilômetros: "))
#Fator de conversão: 1 quilômetro = 0.621371 milha = 0.621371
fator_de_conversao = 0.621371
milhas = quilometros * fator_de_conversao
print(f"{quilometros} quilômetro(s) é igual a {milhas} milha(s)")