from pico2d import *

from man import Man
from background import Background


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
    world = []

    background = Background()
    world.append(background)

    man = Man()
    world.append(man)


def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()


while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()