menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

"""

saldo = 0
limite = 500 
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido." )

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Seu saldo é de R$: {saldo:.2f}")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$: {limite:.2f}.")
        elif excedeu_saques:
            print(f"Operação falhou! Você já realizou o número máximo de saques. Qtde: {numero_saques}.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operaççao falhou! O valor informado é inválido.")
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas Movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
