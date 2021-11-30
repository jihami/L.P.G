import pygame
import random
import math
import sqlite3
import datetime as dt
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
clock = pygame.time.Clock()
score_sound = pygame.mixer.Sound("D:/Project_LPG/bgm/blop_sound.mp3")
sound = pygame.mixer.Sound("D:/Project_LPG/bgm/bgm2.mp3")
sound.play(-1)
def main():
    score = 0
    block = []
    paddle = Block((200, 200, 0), Rect((screen_width / 2 - 50), 600, 100, 30))
    ball = Block((200, 200, 0), Rect((screen_width / 2 - 20), 600, 20, 20), 10)
    colors = [(255, 0, 0), (255, 150, 0), (255, 228, 0), (11, 201, 4),(0,84,255),(0,0,147),(201,0,167)]
    today = str(dt.datetime.today().strftime('%Y-%m-%d'))
    for y,color in enumerate(colors,start=0):
        for x in range(0,6):
            block.append(Block(color, Rect(x * 80 + 12, y * 40 + 10, 55, 20)))
    game_font = pygame.font.SysFont(None, 50)
    running = True
    while running:
        scoreT = game_font.render(f"SCORE : {score}", True, (255, 255, 255))
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    paddle.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    paddle.rect.centerx += 10
        else:
            SURFACE.blit(scoreT, (10, 500))
            LenBlock = len(block)
            block = [x for x in block if not x.rect.colliderect(ball.rect)]
            if len(block) != LenBlock:
                score_sound.play()
                score += 10
                ball.dir *= -1
            if ball.rect.centery < 1000:
                ball.move()
            if paddle.rect.colliderect(ball.rect):
                ball.speed += 0.25
                ball.dir = 90 + (paddle.rect.centerx - ball.rect.centerx) / paddle.rect.width * 100
            if paddle.rect.centerx < 55 :
                paddle.rect.centerx = 55
            if paddle.rect.centerx > screen_width-55:
                paddle.rect.centerx = screen_width - 55
            if ball.rect.centerx < 0 or ball.rect.centerx > 480:
                ball.dir = 180 - ball.dir
            elif ball.rect.centery < 0:
                ball.dir = -ball.dir
            if len(block) == 0:
                messagebox.showinfo("성공하셨습니다!", f"점수 : {score}")
                running = False
            if ball.rect.centery >770 and len(block) > 0:
                messagebox.showinfo("종료", f"점수 : {score} \n종료되었습니다.")
                running = False
            ball.draw_E()
            paddle.draw_R()
            for i in block:
                i.draw_R()
        pygame.display.update()
        clock.tick(30)
    con = sqlite3.connect("brickScore.db")
    cur = con.cursor()
    # cur.execute("insert into brickScore values('21-11-02',score)")
    ins_sql = 'insert into brickScore values(?,?)'
    record = (today,score)
    cur.execute(ins_sql,record)
    con.commit()
    con.close()
if __name__ == "__main__":
    main()
