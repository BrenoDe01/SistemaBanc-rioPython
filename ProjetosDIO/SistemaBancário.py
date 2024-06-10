def banco():
    saldo = 500.00  # Saldo inicial do usuário
    extrato = []  # Lista para armazenar transações
    saques_diarios = 0  # Contador de saques diários
    LIMITE_SAQUES_DIARIOS = 3  # Limite de saques por dia
    LIMITE_SAQUE_VALOR = 500.00  # Limite de valor por saque

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")
        
        if opcao == '1':
            valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
            saldo += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        
        elif opcao == '2':
            if saques_diarios >= LIMITE_SAQUES_DIARIOS:
                print("Limite de saques diários atingido.")
            else:
                valor_saque = float(input("Digite o valor a ser sacado: R$ "))
                if valor_saque > LIMITE_SAQUE_VALOR:
                    print(f"Você só pode sacar no máximo R$ {LIMITE_SAQUE_VALOR:.2f} por saque.")
                elif valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato.append(f"Saque: R$ {valor_saque:.2f}")
                    saques_diarios += 1
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente para realizar o saque.")
        
        elif opcao == '3':
            print("\n--- Extrato ---")
            if extrato:
                for transacao in extrato:
                    print(transacao)
            else:
                print("Nenhuma transação realizada.")
            print(f"Saldo atual: R$ {saldo:.2f}")
        
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
banco()
