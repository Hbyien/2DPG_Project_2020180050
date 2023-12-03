from pico2d import load_image, SDLK_SPACE, SDL_KEYDOWN, get_time,SDLK_d, SDL_KEYUP, SDLK_a, SDLK_f, get_time, SDLK_w, SDLK_s
import math
import game_world



def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def hit_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f

def hit_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_f

def time_out(e):
    return e[0] == 'TIME_OUT'

def sword_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

def sword_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w



class Run:
    @staticmethod
    def enter(man, e):
        if right_down(e):# or left_up(e): #오른쪽 런
            man.dir= 1
        elif left_down(e):# or right_up(e): #왼쪽 런
            man.dir = -1



    @staticmethod
    def exit(man, e):

        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        man.x += man.dir * 10


    @staticmethod
    def draw(man):
        if man.dir <0:
            man.Run_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
            man.isl = 1
        else:
            man.Run_image[int(man.frame)].draw(man.x, man.y, 50, 50)
            man.isl = 0


class Punch:
    @staticmethod
    def enter(man, e):
        man.frame =0
        print('punch 시작')
        man.wait_time = get_time()


    @staticmethod
    def exit(man, e):
        ('punch 끝')
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 13
        if get_time() - man.wait_time > 0.15:
            man.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man):
        if man.isl == 1:
            man.Punch_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
            man.isl = 1
        else:
            man.Punch_image[int(man.frame)].draw(man.x, man.y, 50, 50)
            man.isl = 0


class NoWeaponStand:
    def do(man):
        man.frame = (man.frame + 1) % 12

    def enter(man, e):
        man.dir = 0
        man.frame = 0

    def exit(man, e):
        pass

    @staticmethod
    def draw(man):
        if man.isl == 1:
            man.NoWeaponStand_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 30, 50)
        else:
            man.NoWeaponStand_image[int(man.frame)].draw(man.x, man.y, 30, 50)



class SwordStand:
    @staticmethod  # do(self) 이렇게 쓰지 않아도 됨  / 필요한 함수만 모아놨다 / 객체 생성용이 아니라 함수를 모아두는 용도로 변경
    def do(man):
        man.frame = (man.frame + 1) % 8

        pass

    @staticmethod
    def enter(man, e):
        man.dir = 0
        man.frame = 0

        print(man.swordwhere)


        pass

    @staticmethod
    def exit(man, e):
        if sword_up(e):
            print(man.swordwhere)
            man.swordwhere += 1
        elif sword_down(e):
            print(man.swordwhere)
            man.swordwhere   -= 1
        pass

    @staticmethod
    def draw(man):
        if man.swordwhere == 0:
            if man.isl == 1:
                man.ManSword_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
            else:
                man.ManSword_image[int(man.frame)].draw(man.x, man.y, 40, 50)
            man.swordwhere = 0
        elif man.swordwhere >= 1:
            print('위')
            print(man.swordwhere)
            if man.isl == 1:
                man.ManSwordHi_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
            else:
                man.ManSwordHi_image[int(man.frame)].draw(man.x, man.y, 40, 50)
            man.swordwhere = 1
        else:
            if man.isl == 1:
                man.ManSwordLo_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
            else:
                man.ManSwordLo_image[int(man.frame)].draw(man.x, man.y, 40, 50)

            man.swordwhere = -1


# self.image[int(self.frame)].draw(self.x, self.y, 50, 50)


class StateMachine:

    def __init__(self, man):
        self.cur_state =  SwordStand #클래스는 객체생성이 아니고 함수를 모아두는 용도가 있기 때문에 Idle이란 그룹을 가리키는 것이다.
        self.man = man
        self.transitions = {  # 딕셔너리 사용 키로부터 벨류를 찾아낸다.
            NoWeaponStand: {right_down: Run, left_down: Run,  hit_down: Punch}, #left_up: Run, right_up: Run,
            Run: {right_up:  SwordStand, left_up:  SwordStand, hit_down: Punch,hit_up: SwordStand}, #right_down:  SwordStand, left_down:  SwordStand
            Punch : {time_out:  SwordStand},
            SwordStand: {right_down: Run, left_down: Run,  hit_down: Punch, sword_up: SwordStand, sword_down: SwordStand}, #left_up: Run, right_up: Run,

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
    image = None
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.dir = 0
        self.swordwhere = 0 #검 위치
        self.isl =0  #왼쪽을 보고 있는가


        self.name_sManNoWeaponStand = 'sManNoWeaponStand'
        self.name_sManRun = 'sManRun'
        self.name_sManNoWeaponAttackPunch = 'sManNoWeaponAttackPunch'
        self.name_sManSwordStandMed = 'sManSwordStandMed'
        self.name_sManSwordStandLo = 'sManSwordStandLo'
        self.name_sManSwordStandHi = 'sManSwordStandHi'

        self.NoWeaponStand_image = [load_image("./sManNoWeaponStand/" + self.name_sManNoWeaponStand + "_%d" % i + ".png") for i in range(0, 16)]
        self.Run_image = [load_image("./sManRun/" + self.name_sManRun + "_%d" % i + ".png") for i in range(0, 8)]
        self.Punch_image = [load_image("./sManNoWeaponAttackPunch/" + self.name_sManNoWeaponAttackPunch + "_%d" %i + ".png")for i in range(0, 13)]
        self.ManSword_image = [load_image("./sManSwordStandMed/"+ self.name_sManSwordStandMed + "_%d" %i + ".png")for i in range(0, 12)]
        self.ManSwordLo_image = [load_image("./sManSwordStandLo/" + self.name_sManSwordStandLo + "_%d" % i + ".png") for i in range(0, 12)]
        self.ManSwordHi_image = [load_image("./sManSwordStandHi/" + self.name_sManSwordStandHi + "_%d" % i + ".png") for i in range(0, 10)]

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
