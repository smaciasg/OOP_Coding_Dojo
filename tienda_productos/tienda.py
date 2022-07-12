from generador_id import lista_id
from productos import Producto

class Tienda:

    lista_productos_tienda = []

    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = {}
        Tienda.lista_productos_tienda.append(self)

    def agregar_producto(self, producto):
        id = lista_id[len(self.productos)]
        self.productos[id]=producto
        return self

    def vender_producto(self, id ,cantidad):
        contar_coincidencias = 0
        for key in self.productos:
            if str(id) in key:         
                contar_coincidencias +=1 
                if cantidad >= self.productos[str(id)].cantidad:
                    if input(f"La cantidad disponible para venderle es de: {self.productos[str(id)].cantidad} unidad, ¿está de acuerdo? S/N:  ").lower() == "s":
                        del self.productos[str(id)]
                        return self
                    else:
                        print("Vuelva mañana acá tendremos todo el producto disponible")
                        return self
                else:
                    self.productos[str(id)].cantidad -=cantidad
                    if self.productos[str(id)].cantidad < self.productos[str(id)].rotacion:
                        print(f"Deben comprar más producto, la cantidad actual disponible es de: {self.productos[str(id)].cantidad} unidades")
                        return self
                    else:
                        return self
        if contar_coincidencias == 0:
            print(f"El ID: {id} no es válido")

    def hacer_liquidación(self, category, porcentaje_descuento):
        for key in self.productos:
            if category == self.productos[key].categoria:
                self.productos[key].actualizar_precio(porcentaje_descuento,False)
                print(self.productos[key].precio)
        return self

    @classmethod
    def inflacion(cls,porcentaje_aumento):
        for producto in range(0,len(Producto.lista_productos)):
                Producto.lista_productos[producto].actualizar_precio(porcentaje_aumento,True)
        Producto.informacion_general_productos()
    
    @classmethod
    def informacion_general_tiendas(cls):
        for tienda in range(0,len(cls.lista_productos_tienda)):
            print(f"**************TIENDA: {cls.lista_productos_tienda[tienda].nombre_tienda}*************\n")
            for key in cls.lista_productos_tienda[tienda].productos:
                cls.lista_productos_tienda[tienda].productos[key].print_info_producto()


            