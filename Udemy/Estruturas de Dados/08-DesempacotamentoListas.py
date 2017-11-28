
lista = [1,2,3,4]

a,b,c,d = lista

print(a)
print(b)
print(c)
print(d)

#Desconsiderar outras posições
e,f, _,_ = lista
print(e)
print(f)

#Desconsiderar outras posições
g,_, _,h = lista
print(g)
print(h)

# A MESMA REGRA VALE PARA STRINGS


#-------------------------------------
#Multiplos retornos em funções
def func(x,y):
    return x**2,y**2

#RETORNA UMA TUPLA
val = func(2,3)

print(val)

x,y = func(4,5)

print(x)
print(y)
    