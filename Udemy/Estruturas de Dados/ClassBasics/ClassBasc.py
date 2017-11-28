
class Pessoa:

    def __init__(self, name, old):
        self.name = name
        self.old = old

    def getName(self):
        return self.name

    def getOld(self):
        return self.old


p1 = Pessoa('Claudio',27)


# %s = identificador de string e %d = identificador de númerico
print('Nome: %s' % p1.getName())
print('Idade: %d' % p1.getOld())