class Cuenta_Bancaria:
    info_cuentas = []
    def __init__(self, nombre_cuenta, porcentaje_tasa_interes, valor_apertura=0):
        self.nombre_cuenta = nombre_cuenta
        self.balance_cuenta = valor_apertura
        self.porcentaje_tasa_interes = porcentaje_tasa_interes/100
        self.valor_intereses = 0
        Cuenta_Bancaria.info_cuentas.append(self)

    def deposito(self, cantidad_deposito):
        self.balance_cuenta +=cantidad_deposito
        return self

    def retiro(self, cantidad_retiro):
        if self.balance_cuenta < cantidad_retiro:
            self.balance_cuenta -= 5
            if self.balance_cuenta < 5:
                print(f"Sus fondos son menores que el cobro por intento de transacción en su próximo depósito a su cuenta se debitará ${self.balance_cuenta}")
                return self
            else:
                print("La cuenta no posee fondo suficientes para esta transacción. Cobrando una tafrifa de $5")
                return self
        else: 
            self.balance_cuenta -= cantidad_retiro
            return self

    def mostrar_info_cuenta(self):
        print(f"El balance de la cuenta es de:$ {round(self.balance_cuenta,2)}")
        return self

    def generar_interes(self):
        if self.balance_cuenta > 0:
            self.valor_intereses += self.balance_cuenta*self.porcentaje_tasa_interes
            self.balance_cuenta += self.valor_intereses     
        return self
    
    @classmethod
    def ver_info_cuentas(cls,nombre_cuenta=""):
        dic = {}
        for datos in cls.info_cuentas:
            dicc = {}
            dicc["Balance"] = f"$: {round(datos.balance_cuenta,2)}"
            dicc["Tasa de interes"] = f"{(datos.porcentaje_tasa_interes)*100}%"
            dicc["Intereses generados"] = f"$: {round(datos.valor_intereses,2)}"
            dic[f"{datos.nombre_cuenta}"] = dicc
        if nombre_cuenta != "":
            print(f"Información de la cuenta {nombre_cuenta}:")
            for key,val in dic[nombre_cuenta].items():
                print(f"/// {key} {val}")
        else:
            print("Información de todas las cuentas:")
            for key,val in dic.items():
                print(f"/// {key} {val}")


#/////////////////////////////////////////
# Crear dos cuentas bancarias
cuenta_bancaria_1 = Cuenta_Bancaria("Cuenta_Bancaria_1",2,100)
cuenta_bancaria_2 = Cuenta_Bancaria("Cuenta_Bancaria_2",5,500)
#/////////////////////////////////////////
# Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta,
# todo en una línea de código (es decir, encadenando)
cuenta_bancaria_1.deposito(100).deposito(200).deposito(300).retiro(250).generar_interes().mostrar_info_cuenta()
#////////////////////////////////////////
# Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, 
# todo en una línea de código (es decir, encadenando)
cuenta_bancaria_2.deposito(500).deposito(923).retiro(125).retiro(236.58).retiro(89.87).retiro(356.25).generar_interes().mostrar_info_cuenta()
#///////////////////////////////////////
# BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria
Cuenta_Bancaria.ver_info_cuentas("Cuenta_Bancaria_2")
# Si no pone cuenta muestra todas
Cuenta_Bancaria.ver_info_cuentas()