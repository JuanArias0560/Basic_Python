import random                                                       # Importa la libreria random


def run():                                                          # Define una funcion 
    numero_aleatorio= random.randint(1,100)                         # Escoge un numero aletorio
    numero_elegido=int(input('Elige un numero del 1 al 100: '))     # Imprime el mensaje y lo trasforma a entero
    while numero_elegido != numero_aleatorio:                       
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')            
        else: 
            print('Busca un numero menor')
        numero_elegido = int(input('Elige otro numero :'))          # Da continuidad al ciclo
    print ('Ganaste')                                               # Resultado
    


if __name__=='__main__':
    run()