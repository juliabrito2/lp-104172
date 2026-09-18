import os
os.system('cls')

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 6:
    print("Parabéns! Você foi aprovado!")

elif media >= 4:
    print("Você está em recuperação.")

else:
    print("Você foi reprovado.")
