"""
class Usuario:
    nombre_banco = "Banco del Pueblo"
    def __init__(self, name = "N/A", email = "N/A", balance_cuenta = 0):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito( self, cantidad ):
        self.balance_cuenta = self.balance_cuenta + cantidad
        return self
    
    def retiro (self, cantidad):
        self.balance_cuenta -= cantidad
        return self

    def mostrar_balance( self ):
        print( f"Usuario: {self.name}, balance: S/.{self.balance_cuenta}")
    
    def transfer_dinero(self, otro_usuario, cantidad):
        otro_usuario.hacer_deposito( cantidad )
        self.balance_cuenta -= cantidad
"""

class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self, balance = 0, tasa_interes = 0.01):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito (self, cantidad):
        self.balance += cantidad
        return self
    
    def retiro (self, cantidad):
        if self.balance > 0:
            self.balance -= cantidad
        else:
            self.balance -= cantidad - 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        return self

    def mostrar_info_cuenta (self):
        print(f"Su Balance es ${self.balance}")
        return self

    def ganar_interes (self):
        if self.balance > 0:
            self.balance += (self.balance*self.tasa_interes)
            #print(  f"El interes ganado es ${self.balance}")
        return self

    #def imprime_todo (self):
        self.deposito(19).retiro(5).ganar_interes().mostrar_info_cuenta()

    @classmethod
    def dame_los_balances(cls):
        for x in cls.todas_las_cuentas:
            x.mostrar_info_cuenta()

    
