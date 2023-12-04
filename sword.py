from pico2d import load_image, draw_rectangle
import game_world

class Sword:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, isstand =0, swordwhere= 0):
        if Sword.image == None:
            Sword.image = load_image('sSword.png')
        self.x, self.y, self.velocity , self.isstand , self.swordwhere= x, y, velocity, isstand, swordwhere
        self.face_dir = 1
        self.isis =0

    def draw(self):
        if self.face_dir >=0:
            if self.swordwhere == 0:
                self.image.draw()
                return self.x + 15, self.y + 6, self.x + 40, self.y + 16
            elif self.swordwhere == 1:
                return self.x + 15, self.y + 16, self.x + 40, self.y + 26
            else:
                return self.x + 15, self.y - 10, self.x + 40, self.y
        else:
            self.image.composite_draw(0, 'h',self.x, self.y, 25, 8)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity
        if self.isstand == 1:
            if self.isis != self.x:
                game_world.remove_object(self)
                print("흠")



        if self.x < 25 or self.x > 800 - 25:
            self.velocity = 0
            while self.y >= 60:
                self.y -= 1

    def with_sword(self):

        sword = Sword(self.x, self.y,0)
        game_world.add_object(sword)

    def throw_sword(self):
        sword = Sword(self.x, self.y, self.face_dir * 2)
        game_world.add_object(sword, 1)


    def get_bb(self):
        return self.x - 15, self.y - 5, self.x + 15, self.y + 5