from ClaseMascota import Mascota

class Ninja:

    info_ninjas_mascostas = []

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = []
        Ninja.info_ninjas_mascostas.append(self)


    def actividad(self,nombre_mascota,horas_actividad_fisica=0):
        for maskota in range(0,len(self.mascotas)):
            if nombre_mascota == self.mascotas[maskota].name:
                self.mascotas[maskota].jugar(horas_actividad_fisica)
                print(f"Luego de la actividad física con la mascota {nombre_mascota}, esta tiene una salud de: {self.mascotas[maskota].salud} puntos y su cantidad de premios es: {self.mascotas[maskota].premio}")
                return self
                

    def alimentar(self, nombre_mascota):
        for maskota in range (0,len(self.mascotas)):
            if nombre_mascota == self.mascotas[maskota].name:
                a= self.mascotas[maskota].comer()
                if a == True:
                    print(f"Luego de alimentar a la mascota {nombre_mascota}, esta tiene una salud de: {self.mascotas[maskota].salud} puntos y una energía de: {self.mascotas[maskota].energia} puntos")
                    return self
                else:
                    print(f"Oh {nombre_mascota} morirá de hambre, compra comida")
                    return self

    def banar(self, nombre_maskota):
        for maskota in range(0,len(self.mascotas)):
            if nombre_maskota == self.mascotas[maskota].name:
                self.mascotas[maskota].sonido()
                return self

    def cantidad_comida_restante(self,nombre_maskota):
        for maskota in range(0,len(self.mascotas)):
            if nombre_maskota == self.mascotas[maskota].name:
                print(f"La cantiad de alimento restante de {nombre_maskota} es: {self.mascotas[maskota].cantidad_comida_inical}")

    def imprimir_datos_por_ninja(self):
        print(f"\n++++++   DATOS DEL NIJA   +++++\nNombre completo: {self.nombre} {self.apellido}\n")
        for maskota in self.mascotas:
            maskota.imprimir_info_mascota()
        return self

    @classmethod

    def imprimir_todos_ninjas(cls):
        for ninja in cls.info_ninjas_mascostas:
            ninja.imprimir_datos_por_ninja()