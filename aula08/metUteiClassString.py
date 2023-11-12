#MAIUSCULAS, minusculas e Titulo
curso = "pYtHon"

print(curso.upper()) #"PYTHON"
print(curso.lower()) #"python"
print(curso.title()) #"Python"

#eliminando espaços em branco
print(curso.strip()) #remove todos
print(curso.ltrip()) #remove espaços da esquerda
print(curso.rtrip()) #remove espaços da direita

#junções e centralizações
print(curso.center(10, "#")) #"##Python##"
print(".".join(curso)) #"P.y.t.h.o.n"