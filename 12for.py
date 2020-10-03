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
    user = int(input("Escribe un número--->  "))
    table = range(1, 11)
    for i in table :
        print(str(user) + " multiplicado por " + str(i) + " es "+ str(user*i))
        
if __name__ == '__main__':
    run()