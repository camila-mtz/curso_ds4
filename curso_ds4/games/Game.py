from Athlete import Athlete
from Sport import Sport
from Team import Team

'''Clase Game'''
class Game:
    '''Constructor de Game'''
    def __init__(self, A:Team, B:Team)-> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

def play(self):
    ''' Juego simulado entre equipos'''
    