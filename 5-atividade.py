import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

print("Os numeros informados são: ", n1, n3, "e", n2)
if n1 > n2 > n3:
    print("O menor número é:", n1)
    print("O número do meio é:", n2)
    print("O maior número é:", n3)
elif n2 > n1 > n3:
    print("O menor número é:", n1)
    print("O número do meio é:", n2)
    print("O maior número é:", n3)
else:
    print("O maior número é: ")
    print("O menor número é: ")