def exibirMenu():
    print("1 Depositar\n 2 Sacar\n 3 Extrato\n 0 Sair ->\n")

def deposito(saldo, extrato):
    print("Depósito")
    valor = float(input("Por favor, digite o valor que deseja depositar:"))

    if valor > 0:
        saldo += valor
        extrato += f"Você depositou R$ {valor} reais.\n"
    else:
        print("Valor inválido!") 


def saque(saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    print("Saque")
    valor = float(input("Por favor, digite o valor que você gostaria de sacar:"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Operação falhou! O valor de saque excede o limite por transação.")
    elif excedeu_saques:
        print("Número máximo de saques diário excedido.")
    else:
        saldo -= valor
        extrato += f"Você sacou R$ {valor} reais.\n"
        numero_saques += 1


def exibirExtrato(extrato, saldo):
    print("Extrato")
    print("########## EXTRATO ##########")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Seu saldo atual é: {saldo}")
    print("#############################")



def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        exibirMenu()
        opcao = int(input())

        if opcao == 1:
            deposito(saldo, extrato)

        elif opcao == 2:
            saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == 3:
            exibirExtrato(extrato, saldo)

        elif opcao == 0:
            print("Muito obrigado por usar o nosso banco. Volte sempre!")
            break
        else:
            print("Opção inváida! Por favor, tente novamente e selecione uma opção válida.") 

main()


        
