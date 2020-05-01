class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def get_velocidade(self):
        return self.__velocidade

    def acelerar(self, acelerar):
        self.__velocidade += acelerar

    def frear(self, freio):
        self.__velocidade -= freio

    def imprimir_informacoes(self):
        print('marca: ', self.marca)
        print('modelo:', self.modelo)
        print('rodas', self.rodas)


class Carro(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print('potencia: ', self.potencia)


class Moto(Veiculo):
    def __init__(self, marca, modelo, rodas, partida_eletrica):
        super().__init__(marca, modelo, rodas)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print('partida_eletrica: ', self.partida_eletrica)


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marchas = marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print('marchas ', self.marchas)
        print('bagageiro', self.bagageiro)


carro = Carro("Ford", "Ka", 4, 85.0)
moto = Moto("Honda", "Biz", 2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()
bike.imprimir_informacoes()
moto.imprimir_informacoes()


print("Velocidade atual do Carro:", carro.get_velocidade())
print("Velocidade atual da Moto:", moto.get_velocidade())
print("Velocidade atual da Bicicleta:", bike.get_velocidade())
