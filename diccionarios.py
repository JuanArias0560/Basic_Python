from sys import path_hooks                  # Importacion de libreria 


def run ():
    mi_diccionario = {                      # Ejemplo de diccionarios
        'llave1': 1 ,
        'llave2': 2 ,
        'llave3': 3 ,
    }
    
    # print(mi_diccionario['llave1'])       # Ejemplo de como imprimir solo la llave 
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {                    # ejemplo de diccionarios
        'Argentina' : 44938712,
        'Brasil': 210147125,
        'Colombia' : 50372424,
    }

    # print(poblacion_paises['Argentina'])       

    # for pais in poblacion_paises.keys():      # Ejemplo impresion solo las llaves 
    #     print (pais)

    # for pais in poblacion_paises.values():    # Ejemplo impresion solo los valores
    #     print (pais)

    for pais, poblacion in poblacion_paises.items():                #Ejemplo de como imprimir las llaves y los valores
        print (pais + ' Tiene '+ str(poblacion)+ ' habitantes ')



if __name__=='__main__':
    run ()