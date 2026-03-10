from juego import Juego
from nave import Nave
class Tablero:
    def __init__(self):
        self.AGUA = 0

    def comprobar_impacto(self,x,y):
        Nave.recibir_disparo(x,y)
