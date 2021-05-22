mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[2])
print(len(mylist))
mylist.append("orange")
print(mylist)
print(mylist[3])
print(len(mylist))
mylist.remove("banana")
print(mylist)
print(len(mylist))
mylist.pop();
print(mylist)
print(len(mylist))
mylist.append("banana")
for elemento in mylist:
    print('quiero una: '+elemento)
    
mylistacopiada = mylist.copy();
print(mylistacopiada)
mylistacopiada.append("rene")
print(mylistacopiada)
print(mylist)

myextendedida = mylist+mylistacopiada
print(myextendedida)