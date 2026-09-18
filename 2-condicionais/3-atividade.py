import os
os.system('cls')

morangos = float(input("Quantos Kg de morango você comprou? "))
macas = float(input("Quantos Kg de maçã você comprou? "))

# Preço dos morangos
if morangos <= 5:
    preco_morango = morangos * 2.50
else:
    preco_morango = morangos * 2.20

# Preço das maçãs
if macas <= 5:
    preco_maca = macas * 1.80
else:
    preco_maca = macas * 1.50

total = preco_morango + preco_maca
quantidade = morangos + macas

# Desconto
if quantidade >= 10 or total > 15:
    desconto = total * 0.10
else:
    desconto = 0

total_pagar = total - desconto

print("Total:", total)
print("Desconto:", desconto)
print("Total a pagar:", total_pagar)
