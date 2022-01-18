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




