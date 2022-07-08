class Mascota:

    def __init__(self, name, tipo, golosinas, comida_mascotas_cada_comida=0, premio=0, cantidad_comida_inical = 0):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energia = 0
        self.comida_mascotas_cada_comida = comida_mascotas_cada_comida
        self.premio = premio
        self.horas_actividad = 0
        self.cantidad_comida_inical=cantidad_comida_inical
        Mascota.validador_tipo_mascotas(tipo)
    
    def dormir(self):
        self.energia += 25
        print(self.energia)
        return self
    
    def comer(self):
        if self.cantidad_comida_inical< self.comida_mascotas_cada_comida:
            return False
        else:
            self.cantidad_comida_inical -= self.comida_mascotas_cada_comida
            self.energia += 5
            self.salud += 10
            return True

    def jugar(self,horas_juego=0):
        self.salud +=5
        self.premio +=1
        self.horas_actividad +=horas_juego
        return self

    def imprimir_info_mascota(self):
        print(f"*****INFORMACIÓN MASCOTA*****\nname: {self.name}\ntipo: {self.tipo}\ngolosinas: {self.golosinas}\nsalud: {self.salud} puntos\nenergia: {self.energia} puntos\ncantidad de comidad diaria: {self.comida_mascotas_cada_comida}\npremio: {self.premio}\ncantiad de comidad total disponible: {self.cantidad_comida_inical} unidades\n")

    def sonido(self):
        raise NotImplementedError

    @staticmethod

    def validador_tipo_mascotas(tipo):
        tipos_mascotas = {
            "volador": ["buho","gaviota","loro","mariposa","palona","canario"],
            "acuatico": ["pez","delfin","pulpo","ostra","caballos_mar"],
            "terrestre": ["vaca","perro","gato"]
        }
        for key in tipos_mascotas:
            for i in range(0,len(tipos_mascotas[key])):
                if tipo == tipos_mascotas[key][i]:
                    return key

#////////////MASCOTAS VOLADORAS///////////////////////////

class MascotasVoladoras(Mascota):

    def __init__(self, name, tipo, golosinas, comida_mascotas_cada_comida=0, premio=0, cantidad_comida_inical=0,horas_de_vuelo=0):
        super().__init__(name, tipo, golosinas, comida_mascotas_cada_comida, premio, cantidad_comida_inical)
        self.horas_de_vuelo= horas_de_vuelo
        MascotasVoladoras.es_mascota_del_grupo(tipo)

    def sonido(self):
        sonidos_mascotas = {"buho": "bubububbububu", "gaviota": "gavgavgav","loro":"hola mor, qué querés bb","mariposa":"flylfly"}
        sonido_esperado = sonidos_mascotas[self.tipo]
        print(f"Cada que baño mi maskota suena como raro, algo así como: {sonido_esperado}")
        return self

    def jugar(self,horas_de_vuelo):
        self.horas_de_vuelo += horas_de_vuelo
        if self.tipo == "mariposa":
            print(f"Esta mascota no se ejercita, pero tiene estas horas de vuelo: {self.horas_de_vuelo}")
            return self
        else:
            super().jugar(horas_de_vuelo)
            print(f"Horas de vuelo:{self.horas_de_vuelo}")
            return self

    @staticmethod

    def es_mascota_del_grupo(tipo):
        if (Mascota.validador_tipo_mascotas(tipo) == "volador"):
            print(f"{tipo} es una mascota permitida y es de la clase {Mascota.validador_tipo_mascotas(tipo)}")
        else:
            print(f"{tipo} no es una mascota permitida para la clase volador")

#/////////////////////MASCOTAS ACUÁTICAS///////////////////

class MascotasAcuaticas(Mascota):

    def __init__(self, name, tipo, golosinas, comida_mascotas_cada_comida=0, premio=0, cantidad_comida_inical=0):
        super().__init__(name, tipo, golosinas, comida_mascotas_cada_comida, premio, cantidad_comida_inical)
        MascotasAcuaticas.es_mascota_del_grupo(tipo)

    def sonido(self):
        sonidos_mascotas = {"pez":"Activar sonido mudo", "pulpo":"pick-pick-pick-pick-pick"}
        sonido_esperado = sonidos_mascotas[self.tipo]
        print(f"Cada que baño mi maskota suena como raro, algo así como: {sonido_esperado}")
        return self

    @staticmethod

    def es_mascota_del_grupo(tipo):
        if (Mascota.validador_tipo_mascotas(tipo) == "acuatico"):
            print(f"{tipo} es una mascota permitida y es de la clase {Mascota.validador_tipo_mascotas(tipo)}")
        else:
            print(f"{tipo} no es una mascota permitida para la clase acuatico")

#/////////////////////MASCOTAS TERRESTRES //////////////////

class MascotasTerrestres(Mascota):

    def __init__(self, name, tipo, golosinas, comida_mascotas_cada_comida=0, premio=0, cantidad_comida_inical=0):
        super().__init__(name, tipo, golosinas, comida_mascotas_cada_comida, premio, cantidad_comida_inical)
        MascotasTerrestres.es_mascota_del_grupo(tipo)

    def sonido(self):
        sonidos_mascotas = {"vaca": "miaumiau",  "perro":"arrarrarrrarr"}
        sonido_esperado = sonidos_mascotas[self.tipo]
        print(f"Cada que baño mi maskota suena como raro, algo así como: {sonido_esperado}")
        return self

    @staticmethod

    def es_mascota_del_grupo(tipo):
        if (Mascota.validador_tipo_mascotas(tipo) == "terrestre"):
            print(f"{tipo} es una mascota permitida y es de la clase {Mascota.validador_tipo_mascotas(tipo)}")
        else:
            print(f"{tipo} no es una mascota permitida para la clase terrestre")