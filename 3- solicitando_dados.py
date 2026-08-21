import os
os.system("cls")

# SOLICITANDO DADOS.

nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
peso = float(input("Digite seu peso").replace(',', '.'))
altura = float(input("Digite sua altura").replace(',', '.'))

# MOSTRANDO DADOS.
print('nome', nome)
print('idade', idade)
print('peso', peso)
print('altura', altura)

