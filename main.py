from pico2d import *


Background_WIDTH, Background_HEIGHT = 1000, 800

def handle_events():
    global running, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

open_canvas(Background_WIDTH, Background_HEIGHT)



class Background:
    def __init__(self):
        self.image = load_image('Background.png')
    def draw(self):
        self.image.draw(500,400)

    def update(self):
        pass

class Man:

    #animation_names = ['sManRun']
    #name = 'sManRun'
    #Run = [load_image("./sManRun/" + name + "_%d" % i + ".png") for i in range(0, 8)]
    image = None
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.animation_names = ['sManRun']
        self.name = 'sManRun'
        if Man.image == None:
            Man.image = [load_image("./sManRun/" + self.name + "_%d" % i + ".png") for i in range(0, 8)]
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image[int(self.frame)].draw(self.x, 200, 50, 50)


def reset_world():
    global running, background, man
    running = True
    background = Background()
    man = Man()


def update_world():
    background.update()
    man.update()

    pass

def render_world():
    clear_canvas()
    background.draw()
    man.draw()

    update_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()

#