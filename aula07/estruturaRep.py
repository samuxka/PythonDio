texto = input("frase: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
print()

print(list(range(4)))


for numero in range(0, 11):
    print(numero, end=" ")

print()
    
for numero in range(0, 51, 5):
    print(numero, end=" ")
    
print()

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato")
    else:
        print("Opção inválida")
else:
    print("Tchau!")