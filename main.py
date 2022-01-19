from Usuario import Usuario
from Usuario import CuentaBancaria

"""
diccionario = {
    "CuentaAhorros" : (100, 0.5),
    "CuentaFondos" : (200, 0.10)
}

print(diccionario["CuentaAhorros"][0])
"""

#CASO RICARDO
ricardo = Usuario( "Ricardo")

print("---------------------")

ricardo.crear_cuenta ( "CuentaAhorros", 30 ).hacer_retiro (25, "CuentaAhorros").hacer_deposito(100,"CuentaAhorros")

print("---------------------")

ricardo.crear_cuenta ( "CuentaFondos",100).hacer_deposito(100,"CuentaFondos").hacer_deposito(25,"CuentaFondos").hacer_retiro(5,"CuentaFondos")

print("---------------------")

ricardo.mostrar_balance("CuentaFondos")
ricardo.mostrar_balance("CuentaAhorros")


























"""
ricardo = Usuario( "Ricardo" , "ricardo@gmail.com", 100, 0.05 )
#CuentaRi = CuentaBancaria( 100, 0.05 )
ricardo.hacer_deposito( 150 ).retiro( 50 ).mostrar_balance()
print("--------------------")
ander = Usuario("Anderson", "anger@gmail.com", 200, 0.01)

ricardo.transfer_dinero(ander, 100).mostrar_balance()
print("--------------------")
"""
