times = int(input("times: "))
casos = 1
contador = 0
encontro=False

print(times)

while casos <= times:
    encontro=False
    word = input("ingresa una palabra: ")
    word2 = input("ingresa una palabra: ")
    letras= []
    for a in word:
        letras.append(a)
        
    for letra in word2:
            if letra==letras[contador]:
                contador+=1
                if contador>=len(letras):
                    encontro=True
                    break
                
    if encontro != True:
        contador == 0
        for letra in reversed(word2):
            if letra==letras[contador]:
                if contador>=len(letras)-1:
                    encontro=True     
                    break   
                contador+=1
    if encontro == True:
        print("yes")    
    else:
        print("no")   
    casos+=1