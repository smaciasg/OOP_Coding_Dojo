from itertools import count
from random import random
from classes.ninja import Ninja, Ninja_GrisNeblina, Ninja_CianPlomo, Ninja_TransparteOscuro, Ninja_NadaVeo
from classes.pirate import Pirate, Pirata_ArdeFuego, Pirata_AzulProfundo,Pirata_BlancoUltimaLuz,Pirata_EspacialUA
import random

class Games_Nija_Pirata:


    def __init__(self, nombre_pirata, numero_pirata, nombre_nija, numero_ninja):
        lista_piratas = [Pirata_ArdeFuego(nombre_pirata), Pirata_AzulProfundo(nombre_pirata), Pirata_EspacialUA(nombre_pirata), Pirata_BlancoUltimaLuz(nombre_pirata)]
        lista_nijas = [Ninja_GrisNeblina(nombre_nija), Ninja_CianPlomo(nombre_nija), Ninja_TransparteOscuro(nombre_nija), Ninja_NadaVeo(nombre_nija)]
        self.nombre_pirata = nombre_pirata
        self.info_pirata = lista_piratas[numero_pirata-1]
        self.nombre_nija =nombre_nija
        self.info_ninja = lista_nijas[numero_ninja-1]

    def combatir(self):
        count_atacks_gamer1 = 0
        count_atacks_gamer2 = 0
        while (self.info_pirata.health >=0) and (self.info_ninja.health >=0):
            x= random.randint(1,1000)
            if x%10 == 0:
                self.info_pirata.attack(self.info_ninja)
                count_atacks_gamer1 +=1
                self.info_ninja.attack(self.info_pirata)
                count_atacks_gamer2 +=1
            if x%2 == 0:
                self.info_pirata.attack(self.info_ninja)
                count_atacks_gamer1 +=1
            if x%2 != 0:
                self.info_ninja.attack(self.info_pirata)
                count_atacks_gamer2 +=1

        if self.info_pirata.health > self.info_ninja.health:
            print(f"The winner is el pirata {self.nombre_pirata}, con un total de {count_atacks_gamer1} ataques")
        else:
            print(f"The winner is eñ ninja {self.nombre_nija}, con un total de {count_atacks_gamer2} ataques")



    @staticmethod

    def informacion_general_piratas():
        print("Los piratas son personas terribles las cuales infunden terror, dentro de tos tipos de piratas con los que cuenta nuestro juego tenemos:\n1 - Piratas ArdeFuego - Fuerza Mágica: 200 - Velocidad: 100 - Salud: 100 - Bombas de fuego: 729\n2 - Piratas AzulProfundo - Fuerza Mágica: 101 - Velocidad: 70 - Salud: 170 - Espadas de agua: 809\n3 - Piratas EspacialUA - Fuerza Mágica: 20 - Velocidad: 1000 - Salud: 1000 - Space sould: 890\n4 - Piratas BlancoUltimaLuz - Fuerza Mágica: 111 - Velocidad: 1000 - Salud: 1000 - Fuego Sol: 1000")

    @staticmethod
    def informacion_general_ninjas():
        print("Los Ninjas son personas especiales las cuales liberan del terror, dentro de tos tipos de Ninjas con los que cuenta nuestro juego tenemos:\n1 - Ninjas GrisNeblina - Armas: 200 - Velocidad: 100 - Salud: 100 - Transformaciones: 2\n2 - Ninjas CianPlomo - Armas: 101 - Velocidad: 70 - Salud: 170 - Transformaciones:3\n3 - Ninjas TransparteOscuro - Armas: 20 - Velocidad: 1000 - Salud: 1000 - Transformaciones: 8\n4 - Ninjas NadaVeo - Armas: 111 - Velocidad: 1000 - Salud: 1000 - Transformaciones: 10")

# pirata1.show_stats()
# michelangelo = Ninja("Michelanglo")
# jack_sparrow = Pirate("Jack Sparrow")
# barba_azul = Pirata_AzulProfundo("Barba Azul Ultramar")
# barba_azul.show_stats()
# 
# Ninja.información_generica_ninjas()
# Pirate.informacion_general_juego()
# Ninja.informacion_general_juego()