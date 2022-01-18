class Usuario:
    nombre_banco = "Banco del Pueblo"
    def __init__(self, name = "N/A", email = "N/A", balance_cuenta = 0):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito( self, cantidad ):
        self.balance_cuenta = self.balance_cuenta + cantidad
    
    def retiro (self, cantidad):
        self.balance_cuenta -= cantidad

    def mostrar_balance( self ):
        print( f"Usuario: {self.name}, balance: S/.{self.balance_cuenta}")
    
    def transfer_dinero(self, otro_usuario, cantidad):
        otro_usuario.hacer_deposito( cantidad )
        self.balance_cuenta -= cantidad
