from pico2d import *

from man import Man
from background import Background

import game_world

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            man.handle_event(event)


def reset_world():
    global running
    global background
    global world
    global man

    running = True

    background = Background()
    game_world.add_object(background, 0)
    man = Man()
    game_world.add_object(man, 1)


def update_world():
    game_world.update()

    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()

