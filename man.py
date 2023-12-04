from pico2d import (load_image, SDLK_SPACE, SDL_KEYDOWN, get_time,SDLK_d, SDL_KEYUP, SDLK_a, SDLK_f, get_time, SDLK_w,
                    SDLK_s,SDLK_e)
import math
import game_world
from sword import Sword
import game_framework


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
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w

def throw_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_e

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Boy Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_TIME = FRAMES_PER_ACTION * ACTION_PER_TIME #액션 프레임 증가 속도

class Run:
    @staticmethod
    def enter(man, e):
        if right_down(e):# or left_up(e): #오른쪽 런
            man.dir= 1
            man.face_dir =1
        elif left_down(e):# or right_up(e): #왼쪽 런
            man.dir = -1
            man.face_dir = -1


    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        man.x += man.dir * RUN_SPEED_PPS * game_framework.frame_time



    @staticmethod
    def draw(man):
        if man.dir <0:
            man.Run_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
            man.isl = 1
        else:
            man.Run_image[int(man.frame)].draw(man.x, man.y, 50, 50)
            man.isl = 0

class Run2:
    @staticmethod
    def enter(man, e):
        if right_down(e):# or left_up(e): #오른쪽 런
            man.dir= 1
            man.face_dir =1
        elif left_down(e):# or right_up(e): #왼쪽 런
            man.dir = -1
            man.face_dir = -1


    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        man.x += man.dir * RUN_SPEED_PPS * game_framework.frame_time


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
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man.wait_time > 0.3:
            man.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man):
        if man.isl == 1:
            man.Punch_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
            man.isl = 1
        else:
            man.Punch_image[int(man.frame)].draw(man.x, man.y, 40, 50)
            man.isl = 0

class Kick:
    @staticmethod
    def enter(man, e):
        man.frame =0
        print('zlr')
        man.wait_time = get_time()


    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man.wait_time > 0.3:
            man.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man):
        if man.isl == 1:
            man.Kick_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 30, 50)
            man.isl = 1
        else:
            man.Kick_image[int(man.frame)].draw(man.x, man.y, 30, 50)
            man.isl = 0

class NoWeaponStand:
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

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
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8



    @staticmethod
    def enter(man, e):
        man.dir = 0
        man.frame = 0
        man.wait_time = get_time()


    @staticmethod
    def exit(man, e):
        if sword_up(e):
            man.swordwhere += 1
        elif sword_down(e):
            man.swordwhere  -= 1

        if throw_down(e):
            man.throw_sword()
        pass

    @staticmethod
    def draw(man):

        if man.swordwhere == 0:
            if man.isl == 1:
                man.ManSword_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 10, 25, 8)

            else:
                man.ManSword_image[int(man.frame)].draw(man.x, man.y, 40, 50)
                man.Sword_image.draw(man.x + 28, man.y + 10, 25, 8)
            man.swordwhere = 0
        elif man.swordwhere == 1:

            if man.isl == 1:
                man.ManSwordHi_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 22, 25,8)
            else:
                man.ManSwordHi_image[int(man.frame)].draw(man.x, man.y, 40, 50)
                man.Sword_image.draw(man.x + 28, man.y + 22, 25, 8)
            man.swordwhere = 1
        elif man.swordwhere >= 2:
            if man.isl == 1:
                man.SwordThrowStand_image.composite_draw(0, 'h', man.x, man.y, 30, 50)
            else:
                man.SwordThrowStand_image.draw(man.x, man.y, 30, 50)
        else:
            if man.isl == 1:
                man.ManSwordLo_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 40, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y -5, 25, 8)
            else:
                man.ManSwordLo_image[int(man.frame)].draw(man.x, man.y, 40, 50)
                man.Sword_image.draw(man.x + 28, man.y -5, 25, 8)

            man.swordwhere = -1

class SwordAttck:
    @staticmethod
    def enter(man, e):
        man.frame =0
        man.wait_time = get_time()


    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15
        if get_time() - man.wait_time > 0.15:
            man.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man):
        if man.swordwhere == 0:
            if man.isl == 1:
                man.ManSwordAttackMed_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 10, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 48, man.y + 10, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 10, 25, 8)
            else:
                man.ManSwordAttackMed_image[int(man.frame)].draw(man.x, man.y, 50, 50)
                man.Sword_image.draw(man.x + 28, man.y + 10, 25, 8)
                man.Sword_image.draw(man.x + 48, man.y + 10, 25, 8)
                man.Sword_image.draw(man.x + 28, man.y + 10, 25, 8)
            man.swordwhere = 0
        elif man.swordwhere >= 1:
            if man.isl == 1:
                man.ManSwordAttackHi_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 22, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 48, man.y + 22, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y + 22, 25, 8)

            else:
                man.ManSwordAttackHi_image[int(man.frame)].draw(man.x, man.y, 50, 50)
                man.Sword_image.draw(man.x + 28, man.y + 22, 25, 8)
                man.Sword_image.draw(man.x + 48, man.y + 22, 25, 8)
                man.Sword_image.draw(man.x + 28, man.y + 22, 25, 8)

            man.swordwhere = 1
        else:
            if man.isl == 1:
                man.ManSwordAttackLo_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 50, 50)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y - 5, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 48, man.y - 5, 25, 8)
                man.Sword_image.composite_draw(0, 'h', man.x - 28, man.y - 5, 25, 8)
            else:
                man.ManSwordAttackLo_image[int(man.frame)].draw(man.x, man.y, 50, 50)
                man.Sword_image.draw(man.x + 28, man.y - 5, 25, 8)
                man.Sword_image.draw(man.x + 48, man.y - 5, 25, 8)
                man.Sword_image.draw(man.x + 28, man.y - 5, 25, 8)

            man.swordwhere = -1
# self.image[int(self.frame)].draw(self.x, self.y, 50, 50)




class Throw:
    @staticmethod
    def enter(man, e):
        man.frame =0
        man.wait_time = get_time()


    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man.wait_time > 0.2:
            man.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man):
        if man.isl == 1:
            man.Throw_image[int(man.frame)].composite_draw(0, 'h', man.x, man.y, 30, 50)

            man.isl = 1
        else:
            man.Throw_image[int(man.frame)].draw(man.x, man.y, 30, 50)
            man.isl = 0


class StateMachine:

    def __init__(self, man):
        self.cur_state =  SwordStand #클래스는 객체생성이 아니고 함수를 모아두는 용도가 있기 때문에 Idle이란 그룹을 가리키는 것이다.
        self.man = man
        self.transitions = {  # 딕셔너리 사용 키로부터 벨류를 찾아낸다.
            NoWeaponStand: {right_down: Run2, left_down: Run2,  hit_down: Punch, throw_down: Kick}, #left_up: Run, right_up: Run,
            Run: {right_up:  SwordStand, left_up:  SwordStand, hit_down: SwordAttck,hit_up: SwordStand},
            Run2: {right_up: NoWeaponStand, left_up: NoWeaponStand, hit_down: Punch, hit_up: NoWeaponStand, throw_down: Kick},
            Punch : {time_out:  NoWeaponStand},
            SwordStand: {right_down: Run, left_down: Run,  hit_down: SwordAttck, sword_up: SwordStand, sword_down: SwordStand,
                         throw_down: Throw}, #left_up: Run, right_up: Run,
            SwordAttck: {time_out: SwordStand},
            Throw: {time_out: NoWeaponStand},
            Kick : {time_out:  NoWeaponStand}


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
        self.face_dir = 1


        self.name_sManNoWeaponStand = 'sManNoWeaponStand'
        self.name_sManRun = 'sManRun'
        self.name_sManNoWeaponAttackPunch = 'sManNoWeaponAttackPunch'
        self.name_sManSwordStandMed = 'sManSwordStandMed'
        self.name_sManSwordStandLo = 'sManSwordStandLo'
        self.name_sManSwordStandHi = 'sManSwordStandHi'
        self.name_sManSwordAttackMed = 'sManSwordAttackMed'
        self.name_sManSwordAttackHi = 'sManSwordAttackHi'
        self.name_sManSwordAttackLo = 'sManSwordAttackLo'
        self.name_sManThrowStanding = 'sManThrowStanding'
        self.name_sManHiKick = 'sManHiKick'

        self.NoWeaponStand_image = [load_image("./sManNoWeaponStand/" + self.name_sManNoWeaponStand + "_%d" % i + ".png") for i in range(0, 16)]
        self.Run_image = [load_image("./sManRun/" + self.name_sManRun + "_%d" % i + ".png") for i in range(0, 8)]
        self.Punch_image = [load_image("./sManNoWeaponAttackPunch/" + self.name_sManNoWeaponAttackPunch + "_%d" %i + ".png")for i in range(0, 13)]
        self.ManSword_image = [load_image("./sManSwordStandMed/"+ self.name_sManSwordStandMed + "_%d" %i + ".png")for i in range(0, 12)]
        self.ManSwordLo_image = [load_image("./sManSwordStandLo/" + self.name_sManSwordStandLo + "_%d" % i + ".png") for i in range(0, 12)]
        self.ManSwordHi_image = [load_image("./sManSwordStandHi/" + self.name_sManSwordStandHi + "_%d" % i + ".png") for i in range(0, 10)]
        self.ManSwordAttackMed_image = [load_image("./sManSwordAttackMed/" + self.name_sManSwordAttackMed + "_%d" % i + ".png") for i in range(0, 15)]
        self.ManSwordAttackHi_image = [load_image("./sManSwordAttackHi/" + self.name_sManSwordAttackHi + "_%d" % i + ".png") for i in range(0, 15)]
        self.ManSwordAttackLo_image = [load_image("./sManSwordAttackLo/" + self.name_sManSwordAttackLo + "_%d" % i + ".png") for i in range(0, 15)]
        self.Throw_image = [load_image("./sManThrowStanding/" +  self.name_sManThrowStanding + "_%d" % i + ".png") for i in range(0, 13)]
        self.Kick_image = [load_image("./sManHiKick/" + self.name_sManHiKick+ "_%d" % i + ".png") for i in range(0, 13)]

        self.Sword_image = load_image('sSword.png')
        self.SwordThrowStand_image = load_image('sManThrowStand.png')



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

    def throw_sword(self):
        sword = Sword(self.x, self.y, self.face_dir * 2)
        game_world.add_object(sword)

        if self.face_dir == -1:
            print('FIRE BALL LEFT')
        elif self.face_dir == 1:
            print('FIRE BALL RIGHT')


