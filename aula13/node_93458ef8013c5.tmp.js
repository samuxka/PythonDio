#001
class veiculo:
    def __init__(self, cor, placa, modelo):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo
        
    def ligarMotor(self):
        print("ligado!")

class moto(veiculo):
    pass1

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass


moto = moto()