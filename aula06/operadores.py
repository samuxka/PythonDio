#ARITIMETICOS:
#Adição
print(1 + 1)
#Subtração
print(5 - 3)
#Multiplicação
print(2 * 4)
#Divisão
print(10 / 2)
#Divisão inteira
print(17 // 2)
#Modulo
print(9 % 3)
#Potência
print(2 ** 3)

#COMPARAÇÃO
#Igualdade (==)
saldo = 500
saque = 150
print(saldo == saque)
#diferença (!=)
print(saldo != saque)
#Maior que / maior ou igual (> | >=)
print(saldo > saque)
print(saldo >= saque)
#Menor que / menor ou igual (< | <=)
print(saldo < saque)
print(saldo <= saque)

#ATRIBUIÇÃO
#Atribuição Simples
saldo = 500
print(saldo)
#Atribuição com adição
saldo += 200
print(saldo)
#Atribuição com subtração
saldo -= 100
print(saldo)
#Atribuição com subtração
saldo *= 10
print(saldo)
#Atribuição com subtração
saldo /= 10
print(saldo)
#Atribuição com subtração
saldo //= 100
print(saldo)
#Atribuição com subtração
saldo %= 100
print(saldo)
#Atribuição com subtração
saldo **= 3
print(saldo)

#LOGICOS
#Operador E (and)
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
#Operador OU (or)
saldo >= saque or saque <= limite
#Operador Negação (not)
contatosEmergencia = []
not 1000 > 1500
not contatosEmergencia
not "saque 1500"
not ""
#Parenteses ()
contaEspecial = True
saldo >= saque and saque <= limite or contaEspecial and saldo >= saque
(saldo >= saque and saque <= limite) or (contaEspecial and saldo >= saque)

#IDENTIDADE
#Operador É (is)
curso = "Python"
nomeCurso = curso
curso is nomeCurso
#Operador NÃO é (is not)
curso is not nomeCurso

#ASSOCIAÇÃO
#Operador Está (is)
frutas = ["Laranja", "Uva", "Limão"]
"Python" in curso
#Operador Não Está (not in)
"Maçã" not in frutas