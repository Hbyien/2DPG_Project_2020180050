from pico2d import load_image, SDLK_SPACE, SDL_KEYDOWN, get_time,SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT
import math



def time_out(e):
    return e[0] == 'TIME_OUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT



class Run:
    @staticmethod
    def enter(man, e):
        if right_down(e) or left_up(e): #오른쪽 런
            man.dir, man.action = 1, 1
        elif left_down(e) or right_up(e): #왼쪽 런
            man.dir, man.action = -1, 0

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        man.x += man.dir * 5

    @staticmethod
    def draw(man):
        man.Run_image[int(man.frame)].draw(man.x, man.y, 50, 50)


class Idle:
    @staticmethod  # do(self) 이렇게 쓰지 않아도 됨  / 필요한 함수만 모아놨다 / 객체 생성용이 아니라 함수를 모아두는 용도로 변경
    def do(man):
        man.frame = (man.frame + 1) % 8
        print('Idle Do - 드르렁')
        if get_time() - man.idle_start_time > 3:
            man.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def enter(man, e):
        if man.action == 0:
            man.action = 2
        elif man.action == 1:
            man.action = 3
        man.dir = 0
        man.frame = 0
        man.idle_start_time = get_time()
        pass

    @staticmethod
    def exit(man, e):
        print('IDLE Exit')
        pass

    @staticmethod
    def draw(man):
        man.NoWeaponStand_image[int(man.frame)].draw(man.x, man.y, 30, 50)


# self.image[int(self.frame)].draw(self.x, self.y, 50, 50)


class StateMachine:

    def __init__(self, man):
        self.cur_state = Idle #클래스는 객체생성이 아니고 함수를 모아두는 용도가 있기 때문에 Idle이란 그룹을 가리키는 것이다.
        self.man = man
        self.transitions = {  # 딕셔너리 사용 키로부터 벨류를 찾아낸다.
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
        }

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.man, e)
                self.cur_state = next_state
                self.cur_state.enter(self.man, e)
                return True
        return  False

    def start(self):
        self.cur_state.enter(self.man, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.man)

    def draw(self):
        self.cur_state.draw(self.man)

class Man:

    #animation_names = ['sManRun']
    #name = 'sManRun'
    #Run = [load_image("./sManRun/" + name + "_%d" % i + ".png") for i in range(0, 8)]
    image = None
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 0
        self.action=3
        #self.animation_names = ['sManRun']
        self.name_sManNoWeaponStand = 'sManNoWeaponStand'
        self.name_sManRun = 'sManRun'
        self.NoWeaponStand_image = [load_image("./sManNoWeaponStand/" + self.name_sManNoWeaponStand + "_%d" % i + ".png") for i in range(0, 16)]
        self.Run_image = [load_image("./sManRun/" + self.name_sManRun + "_%d" % i + ".png") for i in range(0, 8)]
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        #self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        #self.image[int(self.frame)].draw(self.x, self.y, 50, 50)
        self.state_machine.draw()
