import os
os.system('cls')

operacao = input("Digite a operação (+, -, * ou /): ")

A = int(input("Digite A: "))
B = int(input("Digite B: "))

if operacao == "+":
    resultado = A + B
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = A - B
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = A * B
    print("Resultado:", resultado)

elif operacao == "/":
    if B != 0:
        resultado = A / B
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Operação inválida.")
