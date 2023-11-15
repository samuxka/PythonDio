#frutas = ["laranja", "maçã", "uva"]

#frutas = []

#letras = list("python")

#numeros = list(range(10))

#carro = ["ferrari", "f8", 4200000, 2020, 2900, "são paulo", true]

#-----------------------------------------------

#frutas = ["maçã", "laranja", "uva", "pera"]
#frutas[0] - maçã
#frutas[2] - uva

#frutas = ["maçã", "laranja", "uva", "pera"]
#frutas[-1] - pera
#frutas[-3] - laranja

#matriz = [
    #    [1, "a", 2],
    #    ["b", 3, 4],
    #    [6, 5, "c"],
#]

#matriz[0] - [1, "a", 2]
#matriz[0][0] - 1
#matriz[0][-1] - 2
#matriz[-1][-1] - "c"

#lista = ["p", "y", "t", "h", "o", "n"]

#lista[2:] - ["t", "h", "o", "n"]
#lista[:2] - ["p", "y"]
#lista[1:3] - ["y", "t"]
#lista[0:3:2] - ["p", "t"]
#lista[::] - ["p", "y", "t", "h", "o", "n"]
#lista[::-1] - ["n", "o", "h", "t", "y", "p"]

#carros = ["gol", "celta", "palio"]

#for carro in carros:
    #print(carro)

#for indice, carro in enumerate(carros):
    #print(f"{indice}: {carro}")
    
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
pares_ = [numero for numero in numeros if numero % 2 == 0]

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    
quadrado_ = [numero ** 2 for numero in numeros]

#[].append
#lista = []

#lista.append(1)
#lista.append("Python")
#lista.append([40, 30, 20])
#print(lista) - [1, "Python", [40, 30, 20]]

#[].clear
#lista = [1, "Python", [40, 30, 20]]
#print(lista) - [1, "Python", [40, 30, 20]]
#lista.clear()
#print(lista) - []

#[].copy
#lista = [1, "Python", [40, 30, 20]]
#lista.copy()
#print(lista) - [1, "Python", [40, 30, 20]]

#[].count
#cores = ["vermelho", "azivis", "verde", "azivis"]

#cores.count("vermelho") - 1
#cores.count("azivis") - 2
#cores.count("verde") - 1

#[].extend
#lista = [1, 2, 3]
#outraLista = [4, 5, 6]
#lista.extend(outraLista)
#print(lista) - [1, 2, 3, 4, 5, 6]

#[].index
#cores = ["vermelho", "azul", "verde", "azul"]
#cores.index("azul") - 1
#cores.index("vermelho") - 0

#[].insert
#lista = [1, 2, 3]
#lista.insert(1, "Python")
#print(lista) - [1, 'Python', 2, 3]

#[].pop
#lista = [1, 2, 3]
#lista.pop()
#print(lista) - [1, 2]
#lista.pop(1)
#print(lista) - [1, 3]

#[].remove
#lista = [1, 2, 3]
#lista.remove(2)
#print(lista) - [1, 3]

#[].reverse
#lista = [1, 2, 3]
#lista.reverse()
#print(lista) - [3, 2, 1]

#[].sort
#lista = [3, 2, 1]
#lista.sort()
#print(lista) - [1, 2, 3]