#001
class veiculo:
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
    def __init__(self, carregado, cor, placa, modelo):
        self.carregado = False
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
        


moto = motocicleta("vermelha", "xre-0023", "XRE 300")
moto.ligarMotor()

carro = Carro("verde", "ccs-0453", "Jaguar Xe")
carro.ligarMotor()

caminhao = Caminhao("Preto", "mht-4512", "scania", False)
caminhao.ligarMotor()
caminhao.esta_carregado()
print(caminhao)