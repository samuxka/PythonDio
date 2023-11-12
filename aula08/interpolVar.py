#Old style

nome = "samuel"
idade = 16
profissao = "programador"
linguagem = "Python"
pi = 3.14159

print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print()

#Metodo format
print("Meu nome é {}, tenho {} anos e sou {}. Gosto de programar em Python".format(nome, idade, profissao))

print()

print("Meu nome é {3}, tenho {2} anos e sou {1}. Gosto de programar em {0}".format(linguagem, profissao, idade, nome))

print()

print("Meu nome é {nome}, tenho {idade} anos e sou {profissao}. Gosto de programar em {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print()

print(f"Meu nome é {nome}, tenho {idade} anos e sou {profissao}. Gosto de programar em {linguagem}")

print()

print(f"Valor de PI: {pi:.2f}")
print(f"Valor de PI: {pi:10.2f}")