import random
import pygame
import sqlite3
from tkinter import *
from tkinter import messagebox

def main():
    score = 0
    level = 1
    root = Tk()
    root.withdraw()
    pygame.init()

    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("눈 피하기")

    clock = pygame.time.Clock()
    BLACK = (0, 0, 0)

    character = pygame.image.load("D:/Project_LPG/img/people.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2)
    character_y_pos = screen_height - character_height
    too_x = 0
    character_speed = 35

    snow = pygame.image.load("D:/Project_LPG/img/snow.png")
    snow2 = pygame.image.load("D:/Project_LPG/img/snow.png")
    snow3 = pygame.image.load("D:/Project_LPG/img/snow.png")
    snow_size = snow.get_rect().size
    snow_width = snow_size[0]
    snow_height = snow_size[1]
    snow_x1_pos = random.randint(0, (screen_width - snow_width))
    snow_y1_pos = random.randint(0, 0)
    snow_x2_pos = random.randint(0, (screen_width - snow_width))
    snow_y2_pos = random.randint(0, 30)
    snow_x3_pos = random.randint(0, (screen_width - snow_width))
    snow_y3_pos = random.randint(0, 50)

    game_font = pygame.font.Font(None, 40)

    snow_speed = 10

    sound = pygame.mixer.Sound("D:/Project_LPG/bgm/bgm.mp3")
    sound.play(-1)
    score_sound = pygame.mixer.Sound("D:/Project_LPG/bgm/score.wav")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    too_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    too_x += character_speed
            if event.type == pygame.KEYUP:  # 키 뗐을때
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    too_x = 0

        character_x_pos += too_x

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        snow_y1_pos += snow_speed
        if snow_y1_pos > screen_height:
            snow_y1_pos = 0
            snow_x1_pos = random.randint(0, (screen_width - snow_width))
        snow_y2_pos += snow_speed
        if snow_y2_pos > screen_height:
            snow_y2_pos = 0
            snow_x2_pos = random.randint(0, (screen_width - snow_width))
        snow_y3_pos += snow_speed
        if snow_y3_pos > screen_height:
            snow_y3_pos = 0
            snow_x3_pos = random.randint(0, (screen_width - snow_width))

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        snow_rect = snow.get_rect()
        snow_rect.left = snow_x1_pos
        snow_rect.top = snow_y1_pos

        snow2_rect = snow2.get_rect()
        snow2_rect.left = snow_x2_pos
        snow2_rect.top = snow_y2_pos

        snow3_rect = snow3.get_rect()
        snow3_rect.left = snow_x3_pos
        snow3_rect.top = snow_y3_pos

        if snow_y1_pos == 0:
            score += 1
            score_sound.play()
        if snow_y2_pos == 0:
            score += 1
            score_sound.play()
        if snow_y3_pos == 0:
            score += 1
            score_sound.play()
        if character_rect.colliderect(snow_rect) or character_rect.colliderect(
                snow2_rect) or character_rect.colliderect(snow3_rect):
            messagebox.showinfo("종료", f"점수 : {score} , 단계 : {level} \n 종료되었습니다.")
            running = False

        if 40 <= score:
            snow_speed = 25
            level = 5
        elif 30 <= score:
            snow_speed = 19
            level = 4
        elif 20 <= score:
            snow_speed = 16
            level = 3
        elif 10 <= score:
            snow_speed = 13
            level = 2

        sL = game_font.render(f"SCORE : {score}, LEVEL: {level}", True, (255, 255, 255))
        sL_rect = sL.get_rect()

        screen.fill(BLACK)
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(snow3, (snow_x3_pos, snow_y3_pos))
        screen.blit(snow2, (snow_x2_pos, snow_y2_pos))
        screen.blit(snow, (snow_x1_pos, snow_y1_pos))
        screen.blit(sL, sL_rect)
        pygame.display.update()
        clock.tick(30)
    print(score)
    con = sqlite3.connect("snowScore.db")
    cur = con.cursor()
    cur.execute("insert into snowScore values(?)", (score,))
    con.commit()
    con.close()


if __name__ == "__main__":
    main()

