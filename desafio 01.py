
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = saldo < valor
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================")

    elif opcao == "0":
        print("Saindo.\nObrigado por usar nosso sistema bancário")
        break

    else:
        print("Operação inválidade, por favor selecione novamente a operação deseja.")



