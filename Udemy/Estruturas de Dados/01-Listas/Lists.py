
# Arrays
minhaLista = ['Test', 1, 2.4]
print(minhaLista)
minhaLista[0] = 'Hello World'
print(minhaLista)


#TUPLA
#É imutavel
minhaTupla = ('')


#Strings
#Permite acessar, porém é imutavel, por caracteres
nome = 'Claudio'
print(nome[0])


#Dicionarios
#Chave+valor
dic = {'Claudio':27, 'Andy':10, 'Dudu':'0.8', 'Andrea':'28'}
print(dic)
print(dic['Dudu'])
for key in dic:
    print(dic[key])




#Outros comandos
num = 0

while (num < 11):
    print(num)
    num += 1


def ehPar(num):
    if num % 2:
        return True
    return False

print(ehPar(39))


list = [0,2,4,8,16,32,64]

for i in range(len(list)):
    print(list[i])

for i in range(1, len(list)):
    print(list[i])

#Pular com imcremento
print('Incrementos')

for i in range(0, len(list), 2):
    print(list[i])