import os

# Limpa o terminal.
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite sua primeira nota: ').replace(',', '.'))
segunda_nota = float(input('Digite sua segunda nota: ').replace(',', '.'))

media = (primeira_nota + segunda_nota) / 2

print('\n= EXIBINDO DADOS =')
print('Nome:', nome)
print('Idade:', idade)
print('Primeira nota:', primeira_nota)
print('Segunda nota:', segunda_nota)
print('Media:', media)
