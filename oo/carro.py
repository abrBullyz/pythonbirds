


"""
classe carro
    2 atributos (motor e direcao)
    motor -> controla a velocidade
        atributo -> velocidade
        metodo acelarar velocidade + 1
        metodo desacelerar velocidade -1

    direcao -> controla a direcao
        valor de direcao N L S O
        metodo virar a esquerda
        metodo virar a direita
        N
     O     L
        S

Exemplo
TESTANDO MOTOR
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.acelerar()
>>> motor.velocidade
4
>>> motor.acelerar()
>>> motor.velocidade
5
>>> motor.frear()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

DIRECAO

>>> direcao = Direcao()
>>> direcao.onde
'North'
>>> direcao.goto_right()
>>> direcao.onde
'East'
>>> direcao.goto_right()
>>> direcao.onde
'South'
>>> direcao.goto_right()
>>> direcao.onde
'Weast'
>>> direcao.goto_right()
>>> direcao.onde
'North'
>>> direcao.goto_left()
>>> direcao.onde
'Weast'

>>> direcao.goto_left()
>>> direcao.onde
'South'

>>> direcao.goto_left()
>>> direcao.onde
'East'













"""
class Motor:
    def __init__(self):
       self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTH = "North"
SOUTH = 'South'
EAST = 'East'
WEAST = 'Weast'


class Direcao:
    turn_right_dct = {
        NORTH: EAST, EAST: SOUTH, SOUTH: WEAST, WEAST: NORTH
    }
    turn_left_dct = {
        NORTH: WEAST, WEAST: SOUTH, SOUTH: EAST, EAST: NORTH
    }

    def  __init__(self):
        self.onde = NORTH

    def goto_right(self):
        self.onde = self.turn_right_dct[self.onde]
    def goto_left(self):
        self.onde = self.turn_left_dct[self.onde]