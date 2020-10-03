''' def run():
    contador=1
    print (contador)
    while contador < 1000 :
            print(contador)
            contador+=1
         '''
''' def run():
    contador =1
    for contador in range(1000) :
        print (contador)         ''' 

def run():
    palabra = input("Escribe una palabra--->  ")
    for letra in palabra:
        print (letra)
        
if __name__ == '__main__':
    run()