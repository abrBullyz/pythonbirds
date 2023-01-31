class Person:
    olhos = 2
    pernas = 2
    dedos_maos = 10
    dedos_pes = 10

    def __init__(self, *filhos,  nome=None, idade=35, email = None):
        self.filhos = list(filhos)
        self.email = email
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 50

    @classmethod
    def nome_e_atributos_declasse(cls):
        return f'{cls} - olhos - {cls.pernas}'

if __name__ == '__main__':


    clara = Person(nome = 'Clara')
    noah = Person(nome = 'Noah')
    abr = Person(noah, nome='abrahao')
    abr.sobrenome = 'Vanelli'
    b = Person(clara, nome='Beth')

    abr.email ='abrbullyz@gmail.com'

    print(F' PERNAS: {abr.pernas}')
    b.sobrenome = 'Bianchi Vanelli'

    print(F' ABR NOME: {abr.nome}')
    for filho in abr.filhos:
        print(filho.nome)



    print(F' CLARA NOME: {clara.nome}')

    print(' __dict__')
    print(abr.__dict__)
    print(noah.__dict__)
    print(clara.__dict__)
    print(b.__dict__)



    print(F' Nome:  {b.nome}   Sobrenome:{b.sobrenome}')
    for filho in b.filhos:
        print(filho.nome)

    b.funcao = 'administradora'

    print(b.__dict__)

    """Delete atributes """
    del abr.filhos
    print(abr.__dict__)

    print(id(Person.olhos) , id(Person.pernas))
    print(Person.metodo_estatico())
    print(abr.metodo_estatico())

    print(Person.nome_e_atributos_declasse(), abr.nome_e_atributos_declasse())