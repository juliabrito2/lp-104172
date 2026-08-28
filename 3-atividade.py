import os
os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Não pode votar! ')
elif idade >= 16 < 17:
    print('Voto opcional')
elif idade >= 18 <= 65:
    print('Voto obrigatório')
else:
    print('Voto opcional')