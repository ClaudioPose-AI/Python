from functools import reduce


#Case - número fatorial
result = 5 * 4 * 3 * 2 * 1

print(result)

def fat(num):
    if (num==0): # Se for zero, o resultado é 1
        return 1
    return (num * fat(num -1))

print('Função com recursão, o resultado é %d' % fat(5))

# Funcional + recursão

fatFunc = lambda num: num * fatFunc(num -1) if num > 1 else 1

print(fatFunc(5))


#map
#Calcula todos os números de uma lista
lista = [1,2,3,4]

pot2 = map(lambda x: x**2, lista)
print(pot2)
for i in pot2:
    print(i)


#redduce - Descontinuada
print(reduce(lambda x,y: x + y, [1,2,3,4]))


#filter
#gera uma lista de números de 0 a 10 que são pares
f = filter(lambda x: x%2 == 0, range(10))
print(f)
for i in f:
    print(i)