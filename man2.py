from pico2d import (load_image, SDLK_n, SDL_KEYDOWN, get_time,SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_m, get_time, SDLK_UP,
                    SDLK_DOWN,SDLK_j)
import math
import game_world
from sword2 import Sword2
import game_framework



def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def hit_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_m

def hit_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_m

def time_out(e):
    return e[0] == 'TIME_OUT'

def sword_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def sword_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def throw_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_n

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j


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
    def enter(man2, e):
        if right_down(e):# or left_up(e): #오른쪽 런
            man2.dir= 1
            man2.face_dir =1
        elif left_down(e):# or right_up(e): #왼쪽 런
            man2.dir = -1
            man2.face_dir = -1


    @staticmethod
    def exit(man2, e):
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        man2.x += man2.dir * RUN_SPEED_PPS * game_framework.frame_time



    @staticmethod
    def draw(man2):
        if man2.dir <0:
            man2.Run_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 50, 50)
            man2.isl = 1
        else:
            man2.Run_image[int(man2.frame)].draw(man2.x, man2.y, 50, 50)
            man2.isl = 0

class Run2:
    @staticmethod
    def enter(man2, e):
        if right_down(e):# or left_up(e): #오른쪽 런
            man2.dir= 1
            man2.face_dir =1
        elif left_down(e):# or right_up(e): #왼쪽 런
            man2.dir = -1
            man2.face_dir = -1


    @staticmethod
    def exit(man2, e):
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        man2.x += man2.dir * RUN_SPEED_PPS * game_framework.frame_time


    @staticmethod
    def draw(man2):
        if man2.dir <0:
            man2.Run_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 50, 50)
            man2.isl = 1
        else:
            man2.Run_image[int(man2.frame)].draw(man2.x, man2.y, 50, 50)
            man2.isl = 0


class Punch:
    @staticmethod
    def enter(man2, e):
        man2.frame =0
        print('punch 시작')
        man2.wait_time = get_time()


    @staticmethod
    def exit(man2, e):
        ('punch 끝')
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man2.wait_time > 0.3:
            man2.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man2):
        if man2.isl == 1:
            man2.Punch_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 40, 50)
            man2.isl = 1
        else:
            man2.Punch_image[int(man2.frame)].draw(man2.x, man2.y, 40, 50)
            man2.isl = 0

class Kick:
    @staticmethod
    def enter(man2, e):
        man2.frame =0
        print('zlr')
        man2.wait_time = get_time()


    @staticmethod
    def exit(man2, e):
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man2.wait_time > 0.3:
            man2.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man2):
        if man2.isl == 1:
            man2.Kick_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 30, 50)
            man2.isl = 1
        else:
            man2.Kick_image[int(man2.frame)].draw(man2.x, man2.y, 30, 50)
            man2.isl = 0

class NoWeaponStand:
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

    def enter(man2, e):
        man2.dir = 0
        man2.frame = 0

    def exit(man2, e):
        pass

    @staticmethod
    def draw(man2):
        if man2.isl == 1:
            man2.NoWeaponStand_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 30, 50)
        else:
            man2.NoWeaponStand_image[int(man2.frame)].draw(man2.x, man2.y, 30, 50)



class SwordStand:
    @staticmethod  # do(self) 이렇게 쓰지 않아도 됨  / 필요한 함수만 모아놨다 / 객체 생성용이 아니라 함수를 모아두는 용도로 변경
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8



    @staticmethod
    def enter(man2, e):
        man2.dir = -1
        man2.frame = 0
        man2.wait_time = get_time()


    @staticmethod
    def exit(man2, e):
        if sword_up(e):
            man2.swordwhere += 1
        elif sword_down(e):
            man2.swordwhere  -= 1

        if throw_down(e):
            man2.throw_sword()
        pass

    @staticmethod
    def draw(man2):

        if man2.swordwhere == 0:
            if man2.isl == 1:
                man2.Man2Sword_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 40, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 10, 25, 8)

            else:
                man2.Man2Sword_image[int(man2.frame)].draw(man2.x, man2.y, 40, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y + 10, 25, 8)
            man2.swordwhere = 0
        elif man2.swordwhere == 1:

            if man2.isl == 1:
                man2.Man2SwordHi_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 40, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 22, 25,8)
            else:
                man2.Man2SwordHi_image[int(man2.frame)].draw(man2.x, man2.y, 40, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y + 22, 25, 8)
            man2.swordwhere = 1
        elif man2.swordwhere >= 2:
            if man2.isl == 1:
                man2.SwordThrowStand_image.composite_draw(0, 'h', man2.x, man2.y, 30, 50)
            else:
                man2.SwordThrowStand_image.draw(man2.x, man2.y, 30, 50)
        else:
            if man2.isl == 1:
                man2.Man2SwordLo_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 40, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y -5, 25, 8)
            else:
                man2.Man2SwordLo_image[int(man2.frame)].draw(man2.x, man2.y, 40, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y -5, 25, 8)

            man2.swordwhere = -1

class SwordAttck:
    @staticmethod
    def enter(man2, e):
        man2.frame =0
        man2.wait_time = get_time()


    @staticmethod
    def exit(man2, e):
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15
        if get_time() - man2.wait_time > 0.15:
            man2.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man2):
        if man2.swordwhere == 0:
            if man2.isl == 1:
                man2.Man2SwordAttackMed_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 50, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 10, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 48, man2.y + 10, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 10, 25, 8)
            else:
                man2.Man2SwordAttackMed_image[int(man2.frame)].draw(man2.x, man2.y, 50, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y + 10, 25, 8)
                man2.Sword_image.draw(man2.x + 48, man2.y + 10, 25, 8)
                man2.Sword_image.draw(man2.x + 28, man2.y + 10, 25, 8)
            man2.swordwhere = 0
        elif man2.swordwhere >= 1:
            if man2.isl == 1:
                man2.Man2SwordAttackHi_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 50, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 22, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 48, man2.y + 22, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y + 22, 25, 8)

            else:
                man2.Man2SwordAttackHi_image[int(man2.frame)].draw(man2.x, man2.y, 50, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y + 22, 25, 8)
                man2.Sword_image.draw(man2.x + 48, man2.y + 22, 25, 8)
                man2.Sword_image.draw(man2.x + 28, man2.y + 22, 25, 8)

            man2.swordwhere = 1
        else:
            if man2.isl == 1:
                man2.Man2SwordAttackLo_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 50, 50)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y - 5, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 48, man2.y - 5, 25, 8)
                man2.Sword_image.composite_draw(0, 'h', man2.x - 28, man2.y - 5, 25, 8)
            else:
                man2.Man2SwordAttackLo_image[int(man2.frame)].draw(man2.x, man2.y, 50, 50)
                man2.Sword_image.draw(man2.x + 28, man2.y - 5, 25, 8)
                man2.Sword_image.draw(man2.x + 48, man2.y - 5, 25, 8)
                man2.Sword_image.draw(man2.x + 28, man2.y - 5, 25, 8)

            man2.swordwhere = -1
# self.image[int(self.frame)].draw(self.x, self.y, 50, 50)




class Throw:
    @staticmethod
    def enter(man2, e):
        man2.frame =0
        man2.wait_time = get_time()


    @staticmethod
    def exit(man2, e):
        pass

    @staticmethod
    def do(man2):
        man2.frame = (man2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        if get_time() - man2.wait_time > 0.2:
            man2.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def draw(man2):
        if man2.isl == 1:
            man2.Throw_image[int(man2.frame)].composite_draw(0, 'h', man2.x, man2.y, 30, 50)

            man2.isl = 1
        else:
            man2.Throw_image[int(man2.frame)].draw(man2.x, man2.y, 30, 50)
            man2.isl = 0


class StateMachine:

    def __init__(self, man2):
        self.cur_state =  SwordStand #클래스는 객체생성이 아니고 함수를 모아두는 용도가 있기 때문에 Idle이란 그룹을 가리키는 것이다.
        self.man2 = man2
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
                self.cur_state.exit(self.man2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.man2, e)
                return True
        return  False

    def start(self):
        self.cur_state.enter(self.man2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.man2)

    def draw(self):
        self.cur_state.draw(self.man2)




class Man2:
    image = None
    def __init__(self):
        self.x, self.y = 180, 90
        self.frame = 0
        self.dir = -1
        self.swordwhere = 0 #검 위치
        self.isl = 1  #왼쪽을 보고 있는가
        self.face_dir = -1


        self.name_sMan2NoWeaponStand = 'sMan2NoWeaponStand'
        self.name_sMan2Run = 'sMan2Run'
        self.name_sMan2NoWeaponAttackPunch = 'sMan2NoWeaponAttackPunch'
        self.name_sMan2SwordStandMed = 'sMan2SwordStandMed'
        self.name_sMan2SwordStandLo = 'sMan2SwordStandLo'
        self.name_sMan2SwordStandHi = 'sMan2SwordStandHi'
        self.name_sMan2SwordAttackMed = 'sMan2SwordAttackMed'
        self.name_sMan2SwordAttackHi = 'sMan2SwordAttackHi'
        self.name_sMan2SwordAttackLo = 'sMan2SwordAttackLo'
        self.name_sMan2ThrowStanding = 'sMan2ThrowStanding'
        self.name_sMan2HiKick = 'sMan2HiKick'

        self.NoWeaponStand_image = [load_image("./sMan2NoWeaponStand/" + self.name_sMan2NoWeaponStand + "_%d" % i + ".png") for i in range(0, 16)]
        self.Run_image = [load_image("./sMan2Run/" + self.name_sMan2Run + "_%d" % i + ".png") for i in range(0, 8)]
        self.Punch_image = [load_image("./sMan2NoWeaponAttackPunch/" + self.name_sMan2NoWeaponAttackPunch + "_%d" %i + ".png")for i in range(0, 13)]
        self.Man2Sword_image = [load_image("./sMan2SwordStandMed/"+ self.name_sMan2SwordStandMed + "_%d" %i + ".png")for i in range(0, 12)]
        self.Man2SwordLo_image = [load_image("./sMan2SwordStandLo/" + self.name_sMan2SwordStandLo + "_%d" % i + ".png") for i in range(0, 12)]
        self.Man2SwordHi_image = [load_image("./sMan2SwordStandHi/" + self.name_sMan2SwordStandHi + "_%d" % i + ".png") for i in range(0, 10)]
        self.Man2SwordAttackMed_image = [load_image("./sMan2SwordAttackMed/" + self.name_sMan2SwordAttackMed + "_%d" % i + ".png") for i in range(0, 15)]
        self.Man2SwordAttackHi_image = [load_image("./sMan2SwordAttackHi/" + self.name_sMan2SwordAttackHi + "_%d" % i + ".png") for i in range(0, 15)]
        self.Man2SwordAttackLo_image = [load_image("./sMan2SwordAttackLo/" + self.name_sMan2SwordAttackLo + "_%d" % i + ".png") for i in range(0, 15)]
        self.Throw_image = [load_image("./sMan2ThrowStanding/" +  self.name_sMan2ThrowStanding + "_%d" % i + ".png") for i in range(0, 13)]
        self.Kick_image = [load_image("./sMan2HiKick/" + self.name_sMan2HiKick+ "_%d" % i + ".png") for i in range(0, 13)]

        self.Sword_image = load_image('sSword2.png')
        self.SwordThrowStand_image = load_image('sManThrowStand2.png')

        Man2

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
        sword2 = Sword2(self.x, self.y, self.face_dir * 2)
        game_world.add_object(sword2)

        if self.face_dir == -1:
            print('FIRE BALL LEFT')
        elif self.face_dir == 1:
            print('FIRE BALL RIGHT')


