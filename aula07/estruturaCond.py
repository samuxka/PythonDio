MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Qual a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Você é muito noo para tirar CNH")


if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
else:
    print("Muito novo!")
    

if idade >= MAIOR_IDADE:
    print("Pode ter")
elif idade >= IDADE_ESPECIAL:
    print("Pode ter, mas so com a autorização dos pais")
else:
    print("Sem direito de ter")