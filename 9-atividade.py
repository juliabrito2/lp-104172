import os
os.system('cls')

# Passo 1: Pedir os dados para o usuário
renda_mensal = float(input("Digite a sua renda mensal (R$): "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado (R$): "))
num_prestacoes = int(input("Digite a quantidade de prestações desejada: "))

# Passo 2: Fazer os cálculos das regras da financeira
limite_emprestimo_total = renda_mensal * 10
valor_prestacao_solicitada = valor_emprestimo / num_prestacoes
limite_prestacao_mensal = renda_mensal * 0.30

# Passo 3: Testar as duas condições ao mesmo tempo
# O valor total deve ser até 10x a renda E a parcela deve ser no máximo 30% da renda
if valor_emprestimo <= limite_emprestimo_total and valor_prestacao_solicitada <= limite_prestacao_mensal:
    print("\nParabéns! O empréstimo PODE ser concedido.")
else:
    print("\nDesculpe, o empréstimo NÃO PODE ser concedido.")
    
    # Mostra o motivo da negação para ajudar o usuário
    if valor_emprestimo > limite_emprestimo_total:
        print("- O valor total pedido ultrapassa 10 vezes a sua renda.")
    if valor_prestacao_solicitada > limite_prestacao_mensal:
        print("- O valor da prestação mensal ultrapassa 30% da sua renda.")
