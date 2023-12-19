class VendaBike:
    def __init__(self, nome, cor, modelo, ano, valor):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bibiiiiiiii")

    def correr(self):
        print("vrummm")

    def parar(self):
        print("parado")


venda_1 = VendaBike("samuel", "azul", "monark", 2020, "R$ 1560")
venda_2 = VendaBike("igor", "preta", "kaloi", 2018, "R$ 1680")

venda_1.buzinar()
venda_2.correr()