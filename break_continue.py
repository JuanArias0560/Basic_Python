def run():
    # for contador in range (1000):            # Ejemplo de contador unicamente par, con continue 
    #     if contador % 2 != 0 :
    #         continue 
    #     print(contador)

    # for i in range (10000) :                 # Ejemplo de contador con parada, break 
    #     print (i)
    #     if i == 5678:
    #         break

    texto=input('Escribe un texto : ')         # Ejemplo contador con letras parando en la o 
    for letra in texto:
        if letra =='o':
            break
        print(letra)    



if __name__=='__main__':
    run()