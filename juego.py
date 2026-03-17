from tablero import Tablero
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(4,0)
        self.lanzar_ataque(7,6)

    def lanzar_ataque(self,x,y):
        print(f"Ataque a {x},{y}")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self,resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        else:
            print("Hundido")

if __name__ == "__main__":
    Juego()
