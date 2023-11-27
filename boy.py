from pico2d import *

import random
import math
import game_framework
import game_world

import play_mode

import server

animation_names = ['sManRun']
class Boy:
    images = None

    def load_images(self):
        if Boy.images == None:
            Boy.images = {}
            for name in animation_names:
                Boy.images[name] = [load_image("./sManRun/" + name + "_%d" % i + ".png") for i in range(0, 24)]

    def __init__(self, name='Noname', x=0, y=0, size=1.0):
        self.name, self.x, self.y, self.size = name, x, y, size
        self.load_images()
        self.dir = 0.0  # radian 값으로 방향을 표시
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'

        self.tx, self.ty = 0, 0
    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if math.cos(self.dir) < 0:
            Boy.images[self.state][int(self.frame)].composite_draw(0, 'h', sx, sy, 100*self.size, 100*self.size)
        else:
            Boy.images[self.state][int(self.frame)].draw(sx, sy, 100*self.size, 100*self.size)