from pico2d import load_image
import game_world

class Sword:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Sword.image == None:
            Sword.image = load_image('sSword.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.face_dir = 1

    def draw(self):
        if self.face_dir >=0:
            self.image.draw(self.x, self.y, 25, 8)
        else:
            self.image.composite_draw(0, 'h',self.x, self.y, 25, 8)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            self.velocity = 0
            while self.y >= 60:
                self.y -= 1



    def throw_sword(self):
        sword = Sword(self.x, self.y, self.face_dir * 2)
        game_world.add_object(sword, 1)