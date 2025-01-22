import time
import numpy as np
import sys

# imprimir con demora
def imprimir_con_demora(s):
    # imprimir una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

# crear la clase 
class pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
    # guardar las variables de atributos
    self.nombre = nombre
    self.tipos = tipos
    self.movimientos = movimientos
    self.ataque = EVs['ataque']
    self.defensa = EVs['defensa']
    self.puntos_de_salud = puntos_de_salud
    self.barra = 20 # Amout of puntos_de_salud barras

    def impresa(self,pokemon2):
        '''imprimir informacion de lucha 
        '''
        print("-----BATALLA DE POKEMON-----")
        print(f"\n{self.nombre}")
        print("Tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{pokemon2.nombre}")
        print("Tipo/", pokemon2.tipos)
        print("ataque/", pokemon2.ataque)
        print("defensa/", pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([pokemon2.ataque,pokemon2.defensa])))
        time.sleep(2)


