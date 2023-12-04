from pico2d import *

from man import Man
from man2 import Man2
from background import Background

import game_world
import game_framework

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            man.handle_event(event)
            man2.handle_event(event)


def init():
    global background
    global man, man2
    global running

    background = Background()
    game_world.add_object(background, 0)

    man = Man()
    man2 = Man2()
    game_world.add_object(man, 1)
    game_world.add_object(man2, 1)

    running = True

def finish():
    game_world.clear()
    pass



def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    #man.wait_time =100000000000000000.0
    pass
def resume():
   #man.wait_time = get_time()
    pass

