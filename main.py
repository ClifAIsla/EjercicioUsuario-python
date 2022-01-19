"""
from Usuario import Usuario

ricardo = Usuario( "Ricardo" , "ricardo.humoz@gmail.com", 100 )
jorge = Usuario( "Jorge" , "jorgetuterror@gmail.com", 1 )

#Guido.nombre_banco = "Banco Interlank"
#print(Guido.nombre_banco)

# Accediendo a los atributos de la instancia
#print(ricardo.name)	
#print(jorge.email)

#HACEMOS DEPOSITO
jorge.hacer_deposito(100)
jorge.hacer_deposito(1)
print(jorge.balance_cuenta)

#HACEMOS RETIRO
jorge.retiro(51)
print(jorge.balance_cuenta)

#MOSTRAR BALANCE
jorge.mostrar_balance()
ricardo.mostrar_balance()
#HACEMOS PRUEBA DE LA TRANSFERENCIA

jorge.transfer_dinero( ricardo, 50)
jorge.mostrar_balance()
ricardo.mostrar_balance()

#HACEMOS OTRA PUREBA
ricardo.hacer_deposito(1000)
ricardo.transfer_dinero( jorge , 2000)

print("-----------------------")
jorge.mostrar_balance()
ricardo.mostrar_balance()

piero = Usuario("Piero","piro@gmail.com")
pepe = Usuario("Pedro","pero@gmail.com")

piero.hacer_deposito(100).hacer_deposito(1).retiro(51).mostrar_balance()
"""
from Usuario import CuentaBancaria
"""
usuario1 = CuentaBancaria(200)
usuario1.deposito(150)
usuario1.retiro(50)
#usuario1.mostrar_info_cuenta()
usuario1.ganar_interes()

CuentaBancaria.dame_los_balances()
"""
usuario1 = CuentaBancaria(20,0.01)
#usuario1.deposito(100).deposito(50).deposito(150).retiro(40).ganar_interes().mostrar_info_cuenta()

print("---------------------------------------")

usuario2 = CuentaBancaria(120,0.5)
#usuario2.deposito(25).deposito(1000).retiro(280).retiro(75).ganar_interes().mostrar_info_cuenta()

print("---------------------------------------")

usuario3 = CuentaBancaria(100,0.01)

CuentaBancaria.dame_los_balances()