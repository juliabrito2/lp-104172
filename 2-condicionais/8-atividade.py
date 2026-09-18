import os
os.system('cls')

cor = input("Digite a cor do CD (Verde, Azul, Amarelo ou Vermelho): ").strip().lower()

if cor == "verde":
    print("Preço: R$ 10,00")
elif cor == "azul":
    print("Preço: R$ 20,00")
elif cor == "amarelo":
    print("Preço: R$ 30,00")
elif cor == "vermelho":
    print("Preço: R$ 40,00")
else:
    print("Cor inválida! Digite uma cor da tabela.")
