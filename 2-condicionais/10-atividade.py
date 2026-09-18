import os
os.system('cls')

# 1. Pedir os dados para o usuário
tipo = input("Digite A para Álcool ou G para Gasolina: ")
litros = float(input("Digite a quantidade de litros: "))

# 2. Definir os preços de cada um
preco_alcool = 3.79
preco_gasolina = 6.59

# 3. Fazer as contas se for Álcool
if tipo == "A":
    preco_total = litros * preco_alcool
    
    if litros <= 25:
        desconto = preco_total * 0.10  # 10% de desconto
    else:
        desconto = preco_total * 0.20  # 20% de desconto
        
    valor_final = preco_total - desconto
    print("Total a pagar: R$", valor_final)

# 4. Fazer as contas se for Gasolina
elif tipo == "G":
    preco_total = litros * gasolina_preco  # Ops, o nome correto da variável é preco_gasolina
    preco_total = litros * preco_gasolina
    
    if litros <= 25:
        desconto = preco_total * 0.15  # 15% de desconto
    else:
        desconto = preco_total * 0.30  # 30% de desconto
        
    valor_final = preco_total - desconto
    print("Total a pagar: R$", valor_final)

# 5. Se o usuário digitar qualquer outra letra
else:
    print("Tipo de combustível incorreto!")
