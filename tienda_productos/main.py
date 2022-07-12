import random
from productos import Producto
from tienda import Tienda
from generador_id import lista_id

#CREAR DOS INSTANACIAS DE TIENDA
tienda1 = Tienda("Simpre hay de todo")
tienda2 = Tienda("Traemos cosas nuevas todos los días")
#CREAR CUATRO INSTANCIAS DE PRODUCTO
producto1 = Producto("Maracuyá x unidad",1500,"Frutas",100,10)
producto2 = Producto("Quesito",2100,"Lácteos y derivados",10,1)
producto3 = Producto("Bocadillo",150,"Dulces y golosinas",50,1)
producto4 = Producto("Arequipe",1050,"Dulces y golosinas",50,1)
producto5 = Producto("Coco x unidad",4500,"Frutas",100,10)
#AGREGAR PRODUCTOS A LA TIENDA1
tienda1.agregar_producto(producto1)
tienda1.agregar_producto(producto2)
tienda1.agregar_producto(producto3)
tienda1.agregar_producto(producto4)
#AGREGAR PRODUCTOS A LA TIENDA2
tienda2.agregar_producto(producto1)
tienda2.agregar_producto(producto2)
tienda2.agregar_producto(producto3)
tienda2.agregar_producto(producto4)
tienda2.agregar_producto(producto5)
#IMPRESIÓN PRODUCTOS TIENDA 1
print(tienda1.productos)
print("*---------------------------------------*")
#IMPRESIÓN PRODUCTOS TIENDA 2
print(tienda2.productos)
print("*---------------------------------------*")
#VENTA DE PRODUCTOS TIENDA 1
tienda1.vender_producto(454654,100)
tienda1.vender_producto(lista_id[0],100)
print(tienda1.productos)
tienda1.vender_producto(lista_id[3],100)
print(tienda1.productos)
print("*---------------------------------------*")
#VENTA DE PRODUCTOS TIENDA 2
tienda2.vender_producto(10101010,100)
tienda2.vender_producto(lista_id[1],100)
print(tienda2.productos)
print("*---------------------------------------*")
#INFLACION GENERAL PRODUCTOS
Tienda.inflacion(10)
print("*---------------------------------------*")
#LIQUIDACIÓN TIENDA 1
tienda1.hacer_liquidación("Dulces y golosinas",20)
print("*---------------------------------------*")
#LIQUIDACIÓN TIENDA 2
tienda2.hacer_liquidación("Frutas",35)
print("*---------------------------------------*")
#INFORMACIÓN GENERAL PRODUCTOS Y TIENDAS
Tienda.informacion_general_tiendas()