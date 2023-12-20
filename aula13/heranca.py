#simples
'''class veiculo:
    def __init__(self, cor, placa, modelo):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo

    def ligarMotor(self):
        print("ligado!")

    def __str__(self):
        return self.cor

class motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):
    def __init__(self, cor, placa, modelo, carregado):
            super().__init__(cor, placa, modelo)
            self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")



moto = motocicleta("vermelha", "xre-0023", "XRE 300")
carro = Carro("verde", "ccs-0453", "Jaguar Xe")
caminhao = Caminhao("Preto", "mht-4512", "scania", False)


print(moto)
print(carro)
print(caminhao)
'''

#Multipla

class Animal:
    def __init__(self, nroPatas):
        self.nroPatas = nroPatas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join ([f'{chave} = {valor}' for chave , valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, corPelo, **kw):
        self.corPelo = corPelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, corBico, **kw):
        self.corBico = corBico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Morcego(Mamifero, Ave):
    pass

'''gato = Gato(nroPatas = 4, corPelo = "Cinza")
print(gato)'''

morcego = Morcego(nroPatas = 4, corPelo = "preta", corBico = "preto")
print(morcego)


#metodo "__mro__"
