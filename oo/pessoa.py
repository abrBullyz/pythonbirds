class Pessoa:
    def __int__(self, nome=None):
       self.nome =nome


    def cumprimentar(self):
        """esse funcao comprimenta"""
        return f'Hello {id(self)} '


if __name__ == '__main__':
    p = Pessoa('Abr')
    print(Pessoa.cumprimentar(p))

    ##print('----------------------------')
    ##print(id(p))

  ##  print('----------------------------')
##    print(p.cumprimentar())

    ##print('----------------------------')
    ##p.nome='Abrahao'
    ##p.sobrenome = 'Vanelli'
    ##p.idade = '43'
  ##  print(f'{p.nome} {p.sobrenome} {p.idade} !')


##data attributes

