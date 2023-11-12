def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")
        print("Retire o seu dinheito no caixa.")
    else:
        print("Saldo insuficiente!")
    print("Obrigado pela preferência")
    
def depositar(valor):
    saldo = 500
    saldo += valor
    print("Depositado com sucesso")

sacar(700)