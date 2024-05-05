menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 8300
limite = 1200
extrato = ""
numero_saques = 0
SAQUES_LIMITES = 2

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Por favor, informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido.")
    elif opcao == "2":
        valor = float(input("Por favor, informe o valor de saque: "))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= SAQUES_LIMITES

        if saldo_excedido:
            print("Saldo insuficiente.")
        elif saldo_excedido:
            print("O valor do saque excede o limite.")
        elif saque_excedido:
            print("Número de saques excedido. Em caso de dúvida entre em contato com a central do banco")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n###### EXTRATO ######")
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "4":
        break
    
    else:
        print("Opção inválida, tente novamente!")