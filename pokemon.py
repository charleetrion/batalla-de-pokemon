import time
import numpy as np
import sys

# imprimir con demora
def imprimir_con_retraso(s):
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

    def impresa(self, pokemon2):
        '''imprimir informacion de lucha'''

        print("-----BATALLA DE POKEMON-----")
        print(f"\n{self.nombre}")
        print("Tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque, self.defensa])))
        print("\nVS")
        print(f"\n{pokemon2.nombre}")
        print("Tipo/", pokemon2.tipos)
        print("ataque/", pokemon2.ataque)
        print("defensa/", pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([pokemon2.ataque, pokemon2.defensa])))
        time.sleep(2)

    def ventaja(self, pokemon2):
        ''' Considerar la ventaja de tipo actualiza poderes de ataque
            y defensa, Devuelve dos cadena de informacion'''

        version = ['fuego', 'agua', 'planta']
        for i, k in enumerate(version):
            if self.tipos == k:

                # Son tipo mismo
                if pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'

                # pokemon2 es fuerte
                elif pokemon2.tipos == version[(i+1) % 3]:
                    pokemon2.ataque *= 2
                    pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\n¡Es muy eficaz!'
                    
                # pokemon2 es débil
                elif pokemon2.tipos == version[(i+2) % 3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    pokemon2.ataque /= 2
                    pokemon2.defensa /= 2
                    cadena_1_ataque = '\n¡Es muy eficaz!'
                    cadena_2_ataque = '\nNo es muy efectivo...'
        return cadena_1_ataque, cadena_2_ataque

    def turno(self, pokemon2, cadena_1_ataque, cadena_2_ataque):
        ''' Empieza con pokemon1, elige ataque y calcular los nuevos
            puntos de salud.
            hacer lo mismo con pokemon2. siga hasta que los puntos de salud de
            uno de los pokemon son < 0
            Actualizar los datos.'''

        while (self.barra > 0) and (pokemon2.barra > 0):
            # imprimir los puntos_de_salud de cada pokemon
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")

            # POKEMON 1
            print(f"¡Adelante {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento:'))
            imprimir_con_retraso(f"\n¡{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar el daño
            pokemon2.barra -= self.ataque
            pokemon2.puntos_de_salud = ""

            # Agregar barras adicionales más defnsa boost
            for j in range(int(pokemon2.barra + .1 * pokemon2.defensa)):
                pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            # Comprueba si pokemon se debilitó
            if pokemon2.barra <= 0:
                imprimir_con_retraso("\n..." + pokemon2.nombre + 'se debilitó')
                break

            # POKEMON 2
            print(f"¡Adelante {pokemon2.nombre}!")
            for i, x in enumerate(pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento:'))
            imprimir_con_retraso(f"\n¡{pokemon2.nombre} usó {pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar el daño
            self.barra -= pokemon2.ataque
            self.puntos_de_salud = ""

            # Agregar barras adicionales más defnsa boost
            for j in range(int(self.barra + .1 * self.defensa)):
                self.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            # Comprueba si pokemon se debilitó
            if self.barra <= 0:
                imprimir_con_retraso("\n..." + self.nombre + 'se debilitó')
                break

    def lucha(self, pokemon2):
        ''' Permitir que dos pokemones luchen entre ellos'''
        # Imprimir informacion de lucha
        self.impresa(pokemon2)
        # Considerar la ventaja de tipo
        cadena_1_ataque, cadena_2_ataque = self.ventaja(pokemon2)
        # Ahora para la lucha real ...
        # Continua mientras pokemon aun tenga puntos_de_salud
        self.turno(pokemon2, cadena_1_ataque, cadena_2_ataque)
        # Recibir dinero o (PREMIO)
        money = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente te pagó ${money}.\n")

# CREACION DE POKEMONEES OBJETOS PARA LA BATALLA 
if __name__ == '__main__':
    # crear pokemones objetos
    charizard = pokemon('charizard', 'fuego', ['lanzallamas', 'pirotecnia', 'Giro fuego', 'Ascuas'], {'ataque': 12, 'defensa': 8})
    blastoise = pokemon('Blastoise', 'agua', ['pistola agua', 'burbujas', 'hidropulso', 'hidrobomba'], {'ataque': 10, 'defensa': 10})
    
    # Luchar
    charizard.lucha(blastoise)
