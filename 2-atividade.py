import os
os.system ('cls')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2
media = soma/ 2
produto = n1 * n2
maior = max(n1, n2)
menor = min(n1, n2)

print(f'soma {soma}')
print(f'media {media}')
print(f'produto {produto}')

if n1 == n2:
    print('Os numeros são iguais')
else:
    print('os numeros não são iguais')
