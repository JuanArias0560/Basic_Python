def run():                                      
    # nombre=input('Escribe tu nombre: ')       # Deletrea tu nombre
    # for letra in nombre :
    #     print(letra)

    frase=input('Escribe una frase : ')
    for caracter in frase:
        print(caracter.upper())                 # Lo lleva a mayusculas 

if __name__=='__main__':
    run()
