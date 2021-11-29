import pygame
import sys
import random
import math
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,Rect
from tkinter import *
from tkinter import messagebox

class Block:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) +270

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
    def draw_E(self):
        pygame.draw.ellipse(SURFACE, self.col, self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)
root= Tk()
root.withdraw()
pygame.init()
pygame.display.set_caption('벽돌깨기')
pygame.key.set_repeat(10,10)
screen_width = 480
screen_height = 640
SURFACE = pygame.display.set_mode((screen_width,screen_height))
FPSCLOCK = pygame.time.Clock()

def main():
    Score = 0
    BLOCK = []
    PADDLE = Block((200,200,0),Rect((screen_width/2-50),600,100,30))
    BALL = Block((200,200,0),Rect((screen_width/2-20),600,20,20),10)
    colors = [(255, 0, 0), (255, 150, 0), (255, 228, 0), (11, 201, 4),(0,84,255),(0,0,147),(201,0,167)]
    for y,color in enumerate(colors,start=0):
        for x in range(0,6):
            BLOCK.append(Block(color,Rect(x*80+12, y*40 + 10, 55, 20)))

    Bigfont = pygame.font.SysFont(None, 80)
    Smallfont = pygame.font.SysFont(None, 50)

    running = True  # 게임이 진행중인가?
    while running:
        M_SCORE = Smallfont.render(f"SCORE : {Score}", True, (255, 255, 255))
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    PADDLE.rect.centerx += 10
        else:
            SURFACE.blit(M_SCORE, (10, 500))
            LenBlock = len(BLOCK)
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock:
                Score += 10
                BALL.dir *= -1
            if BALL.rect.centery < 1000:
                BALL.move()

            if PADDLE.rect.colliderect(BALL.rect):
                BALL.speed += 0.25
                BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100

            if PADDLE.rect.centerx < 55 :
                PADDLE.rect.centerx = 55
            if PADDLE.rect.centerx > screen_width-55:
                PADDLE.rect.centerx = screen_width-55

            if BALL.rect.centerx < 0 or BALL.rect.centerx > 480:
                BALL.dir = 180 - BALL.dir  # 반사각만큼 방향 변화

            elif BALL.rect.centery < 0:
                BALL.dir = -BALL.dir

            if len(BLOCK) == 0:
                messagebox.showinfo("성공하셨습니다!", f"점수 : {Score}")
                running = False
            if BALL.rect.centery >770 and len(BLOCK) > 0:
                messagebox.showinfo("종료", f"점수 : {Score} \n 종료되었습니다.")
                running = False

            BALL.draw_E()
            PADDLE.draw_R()
            for i in BLOCK:
                i.draw_R()

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
