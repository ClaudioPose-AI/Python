# Criar um lista de 0 a 100, apenas com números pares
# Compressão de listas
pares = [num for num in range(101) if(num % 2 == 0)]

print(pares)

#versão procedural
listPares = []

for num in range(101):
    if(num % 2 == 0):
        listPares.append(num)

print('Versão procedural')
print(listPares)

