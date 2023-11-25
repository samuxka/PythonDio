def exibirMsg():
    print("hello World")

def exibirMsg2(nome):
    print(f"welcome {nome}!")

def exibirMsg3(nome="anonimo"):
    print(f"welcome {nome}!")
    
exibirMsg()
exibirMsg2("joao")
exibirMsg3()
exibirMsg3(nome="samuel")