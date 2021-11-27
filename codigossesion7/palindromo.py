def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    
    if palabra[::] == reversed(palabra):
        return True
    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ') 
    if es_palindromo(palabra):
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()