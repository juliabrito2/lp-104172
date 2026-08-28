import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input('Digite um número: '))

# Corrigido para incluir o número 10 na validação
if numero > 10:
    print('É maior que 10!')
elif numero == 10:
    print('É igual a 10!')
else:
    print('É menor que 10!')

