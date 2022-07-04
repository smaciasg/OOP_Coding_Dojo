# CLASE CREACIÓN USUSARIO 
class Usuario:
    info_cuentas_usuarios = []

    def __init__(self,name, identificador_usuario):
        self.nombre_usuario = name
        self.identificador_usuario = identificador_usuario
        self.cuenta_bancaria = []
        Usuario.info_cuentas_usuarios.append(self)

    def hacer_deposito(self,cuenta_num,valor_deposito):
        for cuenta_lista in range(0, len(self.cuenta_bancaria)):
            if cuenta_num == self.cuenta_bancaria[cuenta_lista].nombre_cuenta:
                self.cuenta_bancaria[cuenta_lista].deposito(valor_deposito) 
                print(f"Luego del DEPÓSITO el balance de la cuenta {self.cuenta_bancaria[cuenta_lista].nombre_cuenta} de {self.nombre_usuario} es de: ${self.cuenta_bancaria[cuenta_lista].balance_cuenta}\n")
                return self

    def hacer_retiro(self, cuenta_num, valor_retiro):
        for cuenta_lista in range(0, len(self.cuenta_bancaria)):
            if cuenta_num == self.cuenta_bancaria[cuenta_lista].nombre_cuenta:
                self.cuenta_bancaria[cuenta_lista].retiro(valor_retiro) 
                return self

    def mostrar_balance_usuario(self, cuenta_num):
        for cuenta_lista in range(0, len(self.cuenta_bancaria)):
            if cuenta_num == self.cuenta_bancaria[cuenta_lista].nombre_cuenta:
                print(f"El Usuario: {self.nombre_usuario} para la cuenta {self.cuenta_bancaria[cuenta_lista].nombre_cuenta} cuenta con un") 
                self.cuenta_bancaria[cuenta_lista].mostrar_info_cuenta() 
                return self

    def generar_interes(self, cuenta_num):
        for cuenta_lista in range(0, len(self.cuenta_bancaria)):
            if cuenta_num == self.cuenta_bancaria[cuenta_lista].nombre_cuenta:
                self.cuenta_bancaria[cuenta_lista].generar_interes() 
                return self

    def transfer_dinero(self, num_cuenta_origen, num_cuenta_destino, nombre_otro_usuario, cantidad_transferencia):
        for cuenta_lista in range(0, len(self.cuenta_bancaria)): 
            if num_cuenta_origen == self.cuenta_bancaria[cuenta_lista].nombre_cuenta:
                if self.cuenta_bancaria[cuenta_lista].balance_cuenta < cantidad_transferencia:
                    print(f"El usuario {self.nombre_usuario} posee saldo insuficiente para realizar la transferencia, su balance actual es de: ${self.cuenta_bancaria[cuenta_lista].balance_cuenta}\n")
                    return self
                else: 
                    self.cuenta_bancaria[cuenta_lista].balance_cuenta -= cantidad_transferencia
                    for otra_cuenta_lista in range(0, len(nombre_otro_usuario.cuenta_bancaria)):
                        if num_cuenta_destino == nombre_otro_usuario.cuenta_bancaria[otra_cuenta_lista].nombre_cuenta:
                            nombre_otro_usuario.cuenta_bancaria[otra_cuenta_lista].balance_cuenta += cantidad_transferencia
                            print(f"El Usuario: {self.nombre_usuario} realizó una transferencia por valor de: ${cantidad_transferencia} desde la cuenta {num_cuenta_origen} al Usuario {nombre_otro_usuario.nombre_usuario}. El saldo de: {self.nombre_usuario} luego de la transacción es de: ${round(self.cuenta_bancaria[cuenta_lista].balance_cuenta,2)}\n")
                            return self

    @classmethod
    def ver_info_cuentas_usuarios(cls,id_usuario=""):
        contador = 0
        for datos in range(0,len(cls.info_cuentas_usuarios)):
            if id_usuario == cls.info_cuentas_usuarios[datos].identificador_usuario:
                contador +=1
                print("\n**//**//** CONSULTA DE UN USUARIO Y EL ESTADO DE SUS CUENTAS **\\**\\**")
                print(f"\n***** Titular: {cls.info_cuentas_usuarios[datos].nombre_usuario} - Identificador: {cls.info_cuentas_usuarios[datos].identificador_usuario} *****")
                for cuenta in range(0,len(cls.info_cuentas_usuarios[datos].cuenta_bancaria)):
                    Cuenta_Bancaria.ver_info_cuentas(cls.info_cuentas_usuarios[datos].cuenta_bancaria[cuenta].nombre_cuenta)
        if ((id_usuario != "") and (contador ==0)):
            print("\nEl idenfiticador de cliente asociado no es válido")    
        elif id_usuario == "":
            print("\n**\\**\\** CONSULTA DE TODOS LOS USUARIOS Y EL ESTADO DE SUS CADA UNA DE SUS CUENTAS **//**//**")
            for datos in range(0,len(cls.info_cuentas_usuarios)):
                print(f"\n***** Titular: {cls.info_cuentas_usuarios[datos].nombre_usuario} - Identificador: {cls.info_cuentas_usuarios[datos].identificador_usuario} *****")
                for cuenta in range(0,len(cls.info_cuentas_usuarios[datos].cuenta_bancaria)):
                    Cuenta_Bancaria.ver_info_cuentas(cls.info_cuentas_usuarios[datos].cuenta_bancaria[cuenta].nombre_cuenta)
        

# CLASE CUENTA BANCARIA ///////////////////////////////////////////////////////////////////////////////////////////////////
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
                print(f"Sus fondos en la cuenta {self.nombre_cuenta} son menores que el cobro por intento de transacción en su próximo depósito a su cuenta se debitará ${self.balance_cuenta}\n")
                return self
            else:
                print(f"La cuenta {self.nombre_cuenta} no posee fondo suficientes para esta transacción. Se procede al cobro de la tarifa de $5\n")
                return self
        else: 
            self.balance_cuenta -= cantidad_retiro
            print(f"El SALDO de la cuenta {self.nombre_cuenta} luego del retiro es de: ${self.balance_cuenta}\n")
            return self

    def mostrar_info_cuenta(self):
        print(f"Balance actual de: ${round(self.balance_cuenta,2)}\n")
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
            dicc["Tasa de interes"] = f"{round(((datos.porcentaje_tasa_interes)*100),2)}%"
            dicc["Intereses generados"] = f"$: {round(datos.valor_intereses,2)}"
            dic[f"{datos.nombre_cuenta}"] = dicc
        if nombre_cuenta != "":
            print(f"--- Información de la cuenta {nombre_cuenta}:")
            for key,val in dic[nombre_cuenta].items():
                print(f"/// {key} {val}")
        else:
            print("--- Información de todas las cuentas:")
            for key,val in dic.items():
                print(f"/// {key} {val}")


#/////////////////////////////////////////////////////////////////////////////////////////////////
# EJERCICIOS:

cliente1 = Usuario("Sebas Macías Gallego", 123456789)
cliente1.cuenta_bancaria.append(Cuenta_Bancaria("CB1",2,100))
cliente1.cuenta_bancaria.append(Cuenta_Bancaria("CB2",5,500))
# //////////////////////////////////////////////
cliente1.hacer_deposito("CB1",100).hacer_retiro("CB1",80).hacer_deposito("CB2",1000).hacer_retiro("CB2",280).mostrar_balance_usuario("CB1").mostrar_balance_usuario("CB2")
# //////////////////////////////////////////////
cliente1.cuenta_bancaria.append(Cuenta_Bancaria("CB3",3.5,850))
cliente1.mostrar_balance_usuario("CB3")
# //////////////////////////////////////////////
cliente2 = Usuario("Alejandro De Liz", 987456321)
cliente2.cuenta_bancaria.append(Cuenta_Bancaria("CB4",5,50))
cliente2.mostrar_balance_usuario("CB4")
# //////////////////////////////////////////////
cliente1.transfer_dinero("CB2","CB4",cliente2,560)
# //////////////////////////////////////////////
cliente2.generar_interes("CB4")
#//////////////////////////////////////////////
cliente1.hacer_retiro("CB1",125)
#//////////////////////////////////////////////
Usuario.ver_info_cuentas_usuarios(123456789)
#//////////////////////////////////////////////
Usuario.ver_info_cuentas_usuarios()
#//////////////////////////////////////////////
Usuario.ver_info_cuentas_usuarios(21588)
