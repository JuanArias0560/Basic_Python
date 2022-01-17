def palindromo (palabra):
    palabra = palabra.replace(' ','')
    palabra=palabra.lower()
    palabra_inveritida = palabra[::-1]
    if palabra == palabra_inveritida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindormo = palindromo(palabra)
    if es_palindormo == True:
        print("Es palindromo")
    else :
        print("No es palindromo")


if __name__== "__main__" :
    run()