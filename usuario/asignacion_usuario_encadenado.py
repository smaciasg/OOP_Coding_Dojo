class Usuario:
    def __init__(self,name):
        self.nombre_usuario = name
        self.balance_cliente = 0

    def hacer_deposito(self,valor_deposito):
        self.balance_cliente +=valor_deposito
        print(f"Luego del DEPÓSITO el balance de la cuenta de {self.nombre_usuario} es de: ${self.balance_cliente}\n")
        return self

    def hacer_retiro(self, valor_retiro):
        if self.balance_cliente < valor_retiro:
            print(f"El usuario {self.nombre_usuario} posee saldo insuficiente, su balance actual es de: ${self.balance_cliente}\n")
            return self
        else: 
            self.balance_cliente -= valor_retiro
            print(f"Luego del RETIRO el balance de la cuenta de {self.nombre_usuario} es de: ${self.balance_cliente}\n")
            return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre_usuario}, cuenta con un Balance actual de: ${round(self.balance_cliente,2)}\n")
        return self

    def transfer_dinero(self, nombre_otro_usuario, cantidad_transferencia):
        if self.balance_cliente < cantidad_transferencia:
            print(f"El usuario {self.nombre_usuario} posee saldo insuficiente para realizar la transferencia, su balance actual es de: ${self.balance_cliente}\n")
            return self
        else: 
            self.balance_cliente -= cantidad_transferencia
            nombre_otro_usuario.balance_cliente += cantidad_transferencia
            print(f"El Usuario: {self.nombre_usuario} realizó una transferencia por valor de: ${cantidad_transferencia} al Usuario {nombre_otro_usuario.nombre_usuario}. El saldo de: {self.nombre_usuario} luego de la transacción es de: ${round(self.balance_cliente,2)}\n")
            return self

cliente1 = Usuario("Sebas Macías Gallego")
cliente2 = Usuario("Carlos Andrés Orozco Loaiza")
cliente3 = Usuario("Daniela López Rojo")
cliente1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(400).hacer_retiro(100).transfer_dinero(cliente2,100).mostrar_balance_usuario()
print("\n-----------------------------------------\n")
cliente2.hacer_deposito(200).hacer_deposito(300).transfer_dinero(cliente1,50).transfer_dinero(cliente3,50).mostrar_balance_usuario()
print("\n-----------------------------------------\n")
cliente3.hacer_deposito(1000).transfer_dinero(cliente1,100).transfer_dinero(cliente2,100).transfer_dinero(cliente1,1000).mostrar_balance_usuario()
print("\n-----------------------------------------\n")
cliente1.mostrar_balance_usuario().transfer_dinero(cliente3,100).mostrar_balance_usuario()
