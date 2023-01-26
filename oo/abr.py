class Person:
    olhos = 2
    pernas = 2

    def __init__(self, *filhos,  nome=None, idade=35, email = None):
        self.filhos = list(filhos)
        self.email = email
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':


    clara = Person(nome = 'Clara')
    noah = Person(nome = 'Noah')
    abr = Person(noah, nome='abrahao')
    abr.sobrenome = 'Vanelli'
    b = Person(clara, nome='Beth')


    print(abr.pernas)
    b.sobrenome = 'Bianchi Vanelli'
    print(abr.nome)
    for filho in abr.filhos:
        print(filho.nome)



    print(clara.nome)

    print(abr.__dict__)
    print(noah.__dict__)
    print(clara.__dict__)
    print(b.__dict__)



    print(F' Nome:  {b.nome}   Sobrenome:{b.sobrenome}')
    for filho in b.filhos:
        print(filho.nome)

