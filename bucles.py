# contador = 0 
# print('2 elevado a ' + str(contador) + ' es igual a: ' +str(2**contador))


def run():
    LIMITE = 1000000                                                              # Mayusculas es igual a una constante

    contador = 0 
    potencia_2 = 2**contador 
    while potencia_2 < LIMITE:                                                    # Contador de exponentes con paro en 1000000
        print('2 elevado a ' + str(contador) + ' es igual a: ' +str(potencia_2))
        contador += 1
        potencia_2 = 2**contador 


if __name__ == '__main__' :
    run()