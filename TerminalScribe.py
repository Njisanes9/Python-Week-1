import os
import time
from termcolor import colored



class Canvas:
    def __init__(self, width, height):
        self.x = width
        self.y = height

        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]


def hitsWall(self, point):
    return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

def setPos(self, pos, mark):
    self._canvas[pos[0]][pos[1]] = mark


def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear') 

def print(self):
    self.clear()

    for y in range(self.y):
        print(' ' , join[[col[y]for col in self._canvas]])

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas