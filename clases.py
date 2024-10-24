class Camion:
    def __init__(self, placa, modelo, capacidad):
        self.placa = placa
        self.modelo = modelo
        self.capacidad = capacidad

class CamionTransporteEspecial(Camion):
    def __init__(self, placa, modelo, capacidad, mercancia_peligrosa):
        super().__init__(placa, modelo, capacidad)
        self.mercancia_peligrosa = mercancia_peligrosa

class NodoCamion:
    def __init__(self, camion, siguiente=None):
        self.camion = camion
        self.siguiente = siguiente
