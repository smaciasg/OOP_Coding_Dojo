class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 120
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

#///////////////////////////////////

class Pirata_ArdeFuego(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.strengthmagic = 200
        self.atributounico = 729
        self.speed = 100
        self.health = 100

    def attack ( self , ninja ):
        ninja.health -= ((self.strength)+(ninja.speed/self.speed))
        ninja.health -= self.strengthmagic*0.05
        ninja.armor -= self.strengthmagic*0.01
        self.health += ninja.strength*0.1
        return self

class Pirata_AzulProfundo(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.strengthmagic = 101
        self.atributounico = 809
        self.speed = 70
        self.health = 170

    def attack ( self , ninja ):
        ninja.health -= ((self.strength)*5*(ninja.speed/self.speed))
        ninja.health -= self.strengthmagic*0.02
        ninja.armor -= self.strengthmagic*0.02
        self.health += ninja.strength*0.2
        return self

class Pirata_EspacialUA(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.strengthmagic = 20
        self.atributounico = 890
        self.speed = 1000
        self.health = 1000

    def attack ( self , ninja ):
        ninja.health -= self.strength
        ninja.health -= self.strengthmagic*0.1
        ninja.armor -= self.strengthmagic*0.1
        self.health += ninja.strength*0.3
        return self

class Pirata_BlancoUltimaLuz(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.strengthmagic = 111
        self.atributounico = 1000
        self.speed = 1000
        self.health = 1000

    def attack ( self , ninja ):
        ninja.health -= self.strength*(0.001*self.speed)
        ninja.health -= self.strengthmagic*0.001
        ninja.armor -= self.strengthmagic*0.5
        self.health += ninja.strength*0.5
        self.strength +=0.1
        return self