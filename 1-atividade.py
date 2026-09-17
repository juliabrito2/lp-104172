import os
os.system('cls')

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (F/M): ")
estado = input("Digite seu estado civil: ")

if sexo == "F" and estado == "CASADA":
    tempo = int(input("Há quantos anos você é casada? "))

print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado)

if sexo == "F" and estado == "CASADA":
    print("Tempo de casada:", tempo, "anos")
