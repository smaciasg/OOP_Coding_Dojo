import random

lista_numeros_cuenta = []
def creador_cuentas():
    numero_cuenta = "".join(map(str,[random.randint(0,9) for i in range(0,21)]))
    while numero_cuenta not in lista_numeros_cuenta:
        lista_numeros_cuenta.append(numero_cuenta)
    posicio_cuenta=len(lista_numeros_cuenta)-1
    return lista_numeros_cuenta[posicio_cuenta]


cuenta1 = creador_cuentas()
cuenta2 = creador_cuentas()
cuenta3 = creador_cuentas()
print(cuenta1)
print(cuenta2)
print(cuenta3)
print(lista_numeros_cuenta)