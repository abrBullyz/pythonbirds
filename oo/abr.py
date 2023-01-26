class Atualiza:
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Atualiza()
    print(Atualiza.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())