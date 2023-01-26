class Person:
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



    print(abr.nome)
    for filho in abr.filhos:
        print(filho.nome)
    print(clara.nome)

    print(abr.__dict__)
