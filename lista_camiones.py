from clases import NodoCamion

class ListaCamiones:
    
    def __init__(self):
        self.head = None
        self.cantidad_elementos = 0

    def adicionar_camion(self, camion):
        """
        Adiciona un camion a la lista
        """
        #Escenario 1: La lista esta vacia

        #Paso 1: Crear el nodo
        nodo_nuevo = NodoCamion(camion)

        if self.head is None: #verificar si la lista esta vacia
            self.head = nodo_nuevo
            self.cantidad_elementos = 1
        else: #Escenario 2: La lista no esta vacia
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo_nuevo
            self.cantidad_elementos += 1


