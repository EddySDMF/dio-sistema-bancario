"""
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
"""

from datetime import datetime

menu = """
===================== SISTEMA BANCARIO =====================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_por_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, numero_saques
    if valor > 0:
        saldo += valor
        print(f"Seu deposito de R${valor:.2f} foi efetuado!")
    else:
        print("Nao foi possivel realizar o deposito. Tente novamente.")


def sacar(valor):
    global saldo, numero_saques
    regra_saldo = saldo >= valor
    regra_limite = limite_por_saque >= valor
    regra_saque = numero_saques < LIMITE_SAQUES
    if valor > 0:
        if not regra_saldo:
            print("Voce nao tem saldo para realizar esta operaçao. Confira no extrato e tente novamente.")
        elif not regra_limite:
            print("Voce nao tem limite para realizar esta operaçao. Confira no extrato e tente novamente.")
        elif not regra_saque:
            print("Voce nao tem saque disponivel para realizar esta operaçao. Confira no extrato e tente novamente.")
        else:
            saldo -= valor
            numero_saques += 1
            print(f"Seu saque de R${valor:.2f} foi efetuado!")


def extrato_completo():
    global saldo, extrato, numero_saques, LIMITE_SAQUES
    qtd_saques = LIMITE_SAQUES - numero_saques
    cabecalhos = ["Data", "Tipo", "Valor"]
    print("===================  EXTRATO ========================")
    print(f"Seu saldo é de R${saldo:.2f}.")
    print(f"Voce tem {qtd_saques} saque(s).")
    print("=================== HISTORICO =======================")
    if extrato:
        print(f"{cabecalhos[0].center(20)} | {cabecalhos[1].center(10)} | {cabecalhos[2].center(10)}")
        for reg in extrato:
            print(f"{reg[0].center(20)} | {reg[1].center(10)} | {reg[2]}")
    else:
        print("Nao houveram movimentaçoes.")


def gravar_transacao(quantia):
    global extrato
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if opcao == "d":
        extrato.append([data, "Deposito", quantia])
    elif opcao == "s":
        extrato.append([data, "Saque", quantia])

if __name__ == "__main__":
    while True:

        opcao = input(menu)

        if opcao == "d":
            quantia = float(input("Qual quantia deseja depositar? "))
            depositar(quantia)
            gravar_transacao(quantia)

        elif opcao == "s":
            quantia = float(input("Qual quantia deseja sacar? "))
            sacar(quantia)
            gravar_transacao(quantia)

        elif opcao == "e":
            extrato_completo()

        elif opcao == "q":
            break

        else:
            print('Operaçao invalida!')
