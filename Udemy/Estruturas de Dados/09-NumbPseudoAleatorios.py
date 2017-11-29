import random

#Número inteiro
#Número randomico dentro de um range númerico
#Se for 4 - Resultados entre 0 e 3, similar a regra de listas, index 0 é o inicial
print(random.randrange(4))

#Entre ranges
print(random.randint(1,9))

#Buscar de forma randomica o valor de uma lista
list = [1,2,3,4,5,6,7,8]

print(random.choice(list))


#Embaralhar a lista
print(list)
print(random.shuffle(list))
print(list)

#Buscar um número de elementos da lista, de forma aleatória
print(random.sample(list, 2))

#Número flutuante entre 0 e 1
print(random.random())

#Número flutuante entre 0 >
print(random.uniform(1,20))