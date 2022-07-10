class Ninja:

    lista_ninjas = []

    def __init__( self , name ):
        self.name = name
        self.strength = 200
        self.speed = 5
        self.health = 100
        self.armor = 105
        Ninja.lista_ninjas.append(self)
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    @classmethod
    
    def información_generica_ninjas(cls):
            for ninja in cls.lista_ninjas:
                ninja.show_stats()

 # //////////////////////////

class Ninja_GrisNeblina(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.transformaciones = 2
        self.armor = 200
        self.speed = 100
        self.health = 100

    
    def attack( self , pirate ):
        pirate.health -= self.strength*0.9
        self.transformaciones +=0.01
        self.strength +=0.1
        return self

    def transformacion(self):
        if self.strength > 100 and self.transformaciones>0:
            self.strength += 120
            self.health +=100
            self.transformaciones -=1
            return self
        else:
            print("Ya no cuenta con más transformaciones")
            return self


class Ninja_CianPlomo(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.transformaciones = 3
        self.armor = 101
        self.speed = 70
        self.health = 170

    
    def attack( self , pirate ):
        pirate.health -= self.strength
        self.transformaciones +=0.05
        self.strength +=0.5
        return self

    def transformacion(self):
        if self.strength > 100 and self.transformaciones>0:
            self.strength += 220
            self.health +=200
            self.transformaciones -=1
            return self
        else:
            print("Ya no cuenta con más transformaciones")
            return self

#/////////////////

class Ninja_TransparteOscuro(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.transformaciones = 8
        self.armor = 20
        self.speed = 1000
        self.health = 1000

    
    def attack( self , pirate ):
        pirate.health -= self.strength*0.9
        self.transformaciones +=0.01
        self.strength +=0.1
        return self

    def transformacion(self):
        if self.strength > 100 and self.transformaciones>0:
            self.strength += 220
            self.health +=200
            self.transformaciones -=1
            return self
        else:
            print("Ya no cuenta con más transformaciones")
            return self


class Ninja_NadaVeo(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.transformaciones = 10
        self.armor = 111
        self.speed = 1000
        self.health = 1000

    
    def attack( self , pirate ):
        pirate.health -= self.strength
        self.transformaciones +=0.05
        self.strength +=0.5
        return self

    def transformacion(self):
        if self.strength > 100 and self.transformaciones>0:
            self.strength += 220
            self.health +=200
            self.transformaciones -=1
            return self
        else:
            print("Ya no cuenta con más transformaciones")
            return self