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

import sqlite3
import os

menu = """
===================== SISTEMA BANCARIO =====================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor
              ):
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
    global saldo, numero_saques, LIMITE_SAQUES
    qtd_saques = LIMITE_SAQUES - numero_saques
    print("===================  EXTRATO ========================")
    print(f"Seu saldo é de R${saldo:.2f}.")
    print(f"Voce tem {qtd_saques} saque(s).")
    print("=================== HISTORICO =======================")
    if consultar_transacoes():
        [print(transacao) for transacao in consultar_transacoes()]
    else:
        print("Nao houveram movimentaçoes.")
            
# =================== OPCIONAL (BANCO DE DADOS) ===================

def init_banco():
    with sqlite3.connect('transacoes.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo TEXT NOT NULL,
                quantia REAL NOT NULL
            )
        ''')

def reg_transacao(tipo, quantia):
    with sqlite3.connect('transacoes.db') as conn:
        conn.execute('INSERT INTO transacoes (tipo, quantia) VALUES (?, ?)', (tipo, quantia))

def consultar_transacoes():
    with sqlite3.connect('transacoes.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transacoes ORDER BY data DESC')
        return cursor.fetchall()

def deletar_transacoes():
    with sqlite3.connect('transacoes.db') as conn:
        conn.execute('DELETE FROM transacoes')

# =================== OPCIONAL (BANCO DE DADOS) ===================

while True:

    init_banco()

    opcao = input(menu)

    if opcao == "d":
        quantia = float(input("Qual quantia deseja depositar? "))
        depositar(quantia)
        reg_transacao("Deposito", quantia)

    elif opcao == "s":
        quantia = float(input("Qual quantia deseja sacar? "))
        sacar(quantia)
        reg_transacao("Saque", quantia)

    elif opcao == "e":
        extrato_completo()

    elif opcao == "q":
        deletar_transacoes()
        break

    else:
        print('Operaçao invalida!')
