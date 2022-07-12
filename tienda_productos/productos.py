import random
from generador_id import lista_id

class Producto:

    lista_productos = []

    def __init__(self, nombre_producto, precio, categoria,cantidad,rotacion):
        self.nombre_producto=nombre_producto
        self.precio=precio
        self.categoria=categoria
        self.cantidad = cantidad
        self.rotacion = rotacion
        Producto.lista_productos.append(self)

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado == True:
            self.precio = self.precio*(1+(cambio_porcentaje/100))
            return self
        elif esta_elevado == False:
            self.precio = self.precio*(1-(cambio_porcentaje/100))
            return self

    def print_info_producto(self):
        print(f"Datos del producto:\nNombre: {self.nombre_producto}\nCategoría: {self.categoria}\nPrecio: ${self.precio}\nCantidad disponible de producto: {self.cantidad} unidad\nCantidad nímina de producto esperado: {self.rotacion} unidad\n--------------")

    @classmethod

    def informacion_general_productos(cls):
        for producto in cls.lista_productos:
            producto.print_info_producto()