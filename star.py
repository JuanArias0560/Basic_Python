def conversor(tipo_pesos, valor_dolar):                                     #Conversor de moneda
    pesos = float (input("¿cuantos pesos " + tipo_pesos + " tienes?: "))
    valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """"                                                                 
Bienvenido al conversor de monedas :) 

1- Pesos Colombianos 
2- Pesos Argentinos 
3- Pesos mexicanos

Elige una opcion :

"""
opcion = int(input (menu))
if opcion == 1:
    conversor ("colombianos", 3875 )
elif opcion ==2:
     conversor ("Argentinos", 65 )
elif opcion ==3:
    conversor ("Mexicanos", 24 )
else:
    print("Elige una opcion correcta por favor")


