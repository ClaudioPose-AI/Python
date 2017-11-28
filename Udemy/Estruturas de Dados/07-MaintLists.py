# Convertendo lista em Tupla (Lista imutavel)

list = [10,2,30,4]
print(list)
print(type(list))

#Conversão Lista para Tupla :D

tupleList = tuple(list)
print(tupleList)
print(type(tupleList))


list.sort()
print(list)

#imprimir menos o ultimo elemento da lista
print(list[:-1])
#imprimir o ultimo elemento da lista
print(list[-1])
#Imprimir a lista invertida
print(list[::-1])