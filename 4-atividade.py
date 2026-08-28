import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print("Os numeros informados são: ", n1, "e", n2)
if n1 > n2:
    print("O maior número é:", n1)
    print("O menor número é:", n2)
elif n2 > n1:
    print("O maior número é:", n2)
    print("O menor número é:", n1)
else:
    print("Os dois números são iguais")