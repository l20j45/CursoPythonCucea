from os import system

def saludo():
    system("cls")
    print("----------------------------------")
    print("Hola soy daniel")
    
def suma(number,number2):
    number+=1
    number2+=1
    print(number+number2)
    
def suma2():
    print(number+number2)    
    
saludo()
print("hola mundo")
number=1
number2=2
suma(number,number2)
suma2()