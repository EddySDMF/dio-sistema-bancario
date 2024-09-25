'''
REGRAS DO SISTEMAS

Para a primeira versao do sistema, devemos implementar apenas 3 operaçoes: deposito, saque e extrato.
O sistema terá apenas 1 usuario e nao deve permitir valores negativos.

DEPOSITO:
    - Todos os depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato.

SAQUE:
    - O sistema deve permitir 3 saques diarios com limite maximo de R$500 por saque;
    - Se nao houver saldo em conta, exibir uma mensagem informando que nao sera possivel sacar por falta de saldo;
    - Todos os saques devem ser armazenados em uma variavel e exibidos na operaçao de extrato.

EXTRATO:
    - Esta operaçao deve listar todos os depositos e saques realizados na conta e no fim deve exibir o saldo atual;
    - Os valores devem ser exibidos no formato R$xxx.xx (R$1500.45)
'''



menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")