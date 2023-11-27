from pico2d import *

import random
import math
import game_framework
import game_world

import play_mode

import server

open_canvas(800,600)
animation_names = ['sManRun']
name = 'sManRun'
Run = [load_image("./sManRun/" + name + "_%d" % i + ".png") for i in range(0, 24)]


running = True
x = 800//2
frame = 0
dir = 0
while running:
    clear_canvas()
    Run[int(frame)].draw(200, 200, 30, 30)
    update_canvas()

    frame = (frame + 1) % 24
    x+= dir*5
    delay(0.05)
close_canvas()

class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./sManRun/" + name + "_%d" % i + ".png") for i in range(0, 24)]

    def __init__(self, name='Noname', x=0, y=0, size=1.0):
        self.name, self.x, self.y, self.size = name, x, y, size
        self.load_images()
        self.dir = 0.0  # radian 값으로 방향을 표시
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'

        self.tx, self.ty = 0, 0
    def draw(self):

        if math.cos(self.dir) < 0:
            Zombie.images[self.state][int(self.frame)].composite_draw(0, 'h', 200, 200, 100*self.size, 100*self.size)
        else:
            Zombie.images[self.state][int(self.frame)].draw(200, 200, 100*self.size, 100*self.size)