#deposito, saque e extrato

#var area
USUARIO = "samuka"
SENHA = "Smzin321"
AGENCIA = "001-9"

use = input("Nome: ")
sen = input("Senha: ")
agc = input("Agência: ")

if use != USUARIO and sen != SENHA and agc != AGENCIA:
    print("informações para login incorretas")
else:
    print()
    print(f"Bem vindo(a) {use}!")
    
    menu = """
    [d] Depitar
    [s] Sacar
    [e] Extrato
    [q] sair
    
    => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Valor do deposito: "))
            print()
            
            if valor > 0:
                print("Deposito efetuado com sucesso!")
                saldo += valor
                extrato += f"Deposito: R${valor:.2f}\n"
            else:
                print("Valor inválido.")
        elif opcao == "s":
            
            valor = float(input("Valor do saque: "))
            print()
            exedeuSaldo = valor > saldo
            exedeuLimite = valor > limite
            exedeuSaques = numero_saques >= LIMITE_SAQUES
            
            if exedeuSaldo:
                print("Saldo insuficiente.")
            elif exedeuLimite:
                print("Você exedeu seu limite Bancario")
            elif exedeuSaques:
                print("Máximo de saques diários atingidos.")
            elif valor > 0:
                print()
                print("Saque efetuado com sucesso!")
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
            else:
                print("Valor inválido.")
        elif opcao == "e":
            print("\n=============== EXTRATO ===============")
            print("Nenhuma movimentação realizada" if not extrato else extrato)
            print(f"\nSaldo: R${saldo:.2f}")
            print("========================================")
        elif opcao == "q":
            break
        else:
            print("operação inválida")