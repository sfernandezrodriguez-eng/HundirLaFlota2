from tablero import Tablero
from nave import Nave
class Juego:
    def __init__(self):
        self.lanzar_ataque(3,2)


    def lanzar_ataque(self,x,y):
        print(f"Atacando a {x}, {y}")
        obj_tablero = Tablero()
        obj_tablero.comprobar_impacto(x,y)

    def mostrar_resultado(self,resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")

        else:
            print("Hundido")



if __name__ == "__main__":
    Juego()
