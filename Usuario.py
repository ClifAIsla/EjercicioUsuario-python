class Usuario:
    #OJO, LOS VALORES QUE AGREGAMOS EN BALANCE E INTERES SON POR DEFAULT
    def __init__(self, name = "N/A", email = "N/A", balance = 0, interes = 0.01, tipo = "Ahorros"):
        self.name = name
        self.email = email
        self.tipo = { 
            "CuentaAhorros" : CuentaBancaria(balance, interes),
            "CuentaFondos" : CuentaBancaria(balance, interes)
    }
    
    #ACTUALIZAMOS DEPOSITOS CON EL OBJETO DE LA CUENTA
    def hacer_deposito( self, cantidad, tipo_cuenta ):
        self.tipo[ tipo_cuenta ].deposito (cantidad)
        print(f"{self.name} hizo un deposito de ${cantidad} hacia su {tipo_cuenta}")
        return self
    
    #ACTUALIZAMOS RETIROS CON EL OBJETO DE LA CUENTA
    def hacer_retiro (self, cantidad , tipo_cuenta):
        self.tipo[tipo_cuenta].retiro(cantidad)
        print(f"{self.name} hizo un retiro de ${cantidad} desde su {tipo_cuenta}")
        return self

    #ACTUALIZAMOS MOSTRAR BALANCE CON EL OBJETO DE LA CUENTA
    def mostrar_balance( self, tipo_cuenta):
        #print( f"Usuario: {self.name}, balance: $ {self.cuenta.balance}")
        print( f"Usuario: {self.name}, balance: $ {self.tipo[tipo_cuenta].balance} en su {tipo_cuenta}")

    
    def transfer_dinero(self, otro_usuario, cantidad, tipo_cuenta ):
        otro_usuario.cuenta.deposito ( cantidad )
        print(f"{self.name} hizo un transferencia de ${cantidad} a {otro_usuario.name}")
        self.cuenta.retiro ( cantidad )
        return self

    #METODO CREAR CUENTA
    def crear_cuenta ( self , tipo_cuenta, cantidad):
        self.tipo[tipo_cuenta].balance = cantidad
        print( f"El usuario {self.name} se esta creando una {self.tipo[tipo_cuenta]} con un balance de ${cantidad}" )
        return self


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
        return self

    @classmethod
    def dame_los_balances(cls):
        for x in cls.todas_las_cuentas:
            x.mostrar_info_cuenta()























































"""
class Usuario:
    #OJO, LOS VALORES QUE AGREGAMOS EN BALANCE E INTERES SON POR DEFAULT
    def __init__(self, name = "N/A", email = "N/A", balance = 0, interes = 0.01):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria (balance, interes)
    
    #ACTUALIZAMOS DEPOSITOS CON EL OBJETO DE LA CUENTA
    def hacer_deposito( self, cantidad ):
        #self.cuenta.balance += cantidad
        self.cuenta.deposito ( cantidad )
        #self.cuenta.mostrar_info_cuenta()
        print(f"{self.name} hizo un deposito de ${cantidad}")
        return self
    
    #ACTUALIZAMOS RETIROS CON EL OBJETO DE LA CUENTA
    def retiro (self, cantidad):
        #self.cuenta.balance -= cantidad
        self.cuenta.retiro(cantidad)
        print(f"{self.name} hizo un retiro de ${cantidad}")
        return self

    #ACTUALIZAMOS MOSTRAR BALANCE CON EL OBJETO DE LA CUENTA
    def mostrar_balance( self ):
        print( f"Usuario: {self.name}, balance: $ {self.cuenta.balance}")
    
    def transfer_dinero(self, otro_usuario, cantidad):
        #otro_usuario.hacer_deposito( cantidad )
        #otro_usuario.cuenta.balance += cantidad
        otro_usuario.cuenta.deposito ( cantidad )
        print(f"{self.name} hizo un transferencia de ${cantidad} a {otro_usuario.name}")
        #self.cuenta.balance -= cantidad
        self.cuenta.retiro ( cantidad )
        return self

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
"""
