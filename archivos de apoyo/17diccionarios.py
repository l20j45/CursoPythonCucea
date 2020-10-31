def run():
    mi_diccionario ={
        'nombre':"daniel",   
        'estatura':1.75,
        'peso':120
        }

    for elemento in mi_diccionario.keys():
        print(elemento)
    for elemento in mi_diccionario.values():
        print(elemento)
    for elemento in mi_diccionario.items():
        print(elemento)



if __name__ == '__main__':
    run()