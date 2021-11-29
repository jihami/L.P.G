import random
import pygame
from tkinter import *
from tkinter import messagebox
#############################################
root= Tk()
root.withdraw()
#기본초기화(반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("눈 피하기")
game_font = pygame.font.Font(None, 40)

#FPS - Frame per Second - 초당 프레임수
clock = pygame.time.Clock()
#############################################

#1.사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 만들기
BLACK = (0, 0, 0)
# background = pygame.image.load("D:/Project_LPG/img/background.png")

#캐릭터 만들기
character = pygame.image.load("D:/Project_LPG/img/people.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) #화면중앙
character_y_pos = screen_height - character_height # 화면 최하단

#이동 위치
too_x = 0
character_speed = 35

#눈 만들기
snow = pygame.image.load("D:/Project_LPG/img/snow.png")
snow2 = pygame.image.load("D:/Project_LPG/img/snow.png")
snow3 = pygame.image.load("D:/Project_LPG/img/snow.png")
snow_size = snow.get_rect().size
snow_width = snow_size[0]
snow_height = snow_size[1]
snow_x_pos = random.randint(0,(screen_width-snow_width)) #0~스크린크기-눈의 가로중 랜덤
snow_y_pos = random.randint(0,0)
snow_x2_pos = random.randint(0,(screen_width-snow_width)) #0~스크린크기-눈의 가로중 랜덤
snow_y2_pos = random.randint(0,30)
snow_x3_pos = random.randint(0,(screen_width-snow_width)) #0~스크린크기-눈의 가로중 랜덤
snow_y3_pos = random.randint(0,50)

game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)
score = 0
level = 1
snow_speed = 10

sound = pygame.mixer.Sound("D:/Project_LPG/bgm/bgm.mp3")
sound.play(-1)
score_sound = pygame.mixer.Sound("D:/Project_LPG/bgm/score.wav")

running = True #게임이 진행중인가?
def Click():
    messagebox.showinfo("알림칭", "알림창")
while running:
    dt = clock.tick(30) #보통은 30사용
    #2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: #키를 눌렀을 떄
            if event.key == pygame.K_LEFT:
                too_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                too_x += character_speed
        if event.type == pygame.KEYUP: #키 뗐을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                too_x = 0

    #3.게임 캐릭터 위치 정의
    character_x_pos += too_x

    if character_x_pos < 0: #화면 오른쪽 밖으로 나갈때
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: #화면 왼쪽으로 나갈때
        character_x_pos = screen_width - character_width


    snow_y_pos += snow_speed #떨어지는 효과
    if snow_y_pos > screen_height: #화면에서 밑으로 떨어졌을때
        snow_y_pos = 0
        snow_x_pos = random.randint(0, (screen_width-snow_width))
    snow_y2_pos += snow_speed
    if snow_y2_pos > screen_height:
        snow_y2_pos = 0
        snow_x2_pos = random.randint(0, (screen_width-snow_width))
    snow_y3_pos += snow_speed
    if snow_y3_pos > screen_height:
        snow_y3_pos = 0
        snow_x3_pos = random.randint(0, (screen_width-snow_width))

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    snow_rect = snow.get_rect()
    snow_rect.left = snow_x_pos
    snow_rect.top = snow_y_pos

    snow2_rect = snow2.get_rect()
    snow2_rect.left = snow_x2_pos
    snow2_rect.top = snow_y2_pos

    snow3_rect = snow3.get_rect()
    snow3_rect.left = snow_x3_pos
    snow3_rect.top = snow_y3_pos

    if snow_y_pos == 0 :
        score += 1
        score_sound.play()
    if snow_y2_pos == 0 :
        score += 1
        score_sound.play()
    if snow_y3_pos == 0:
        score += 1
        score_sound.play()
    if character_rect.colliderect(snow_rect) or character_rect.colliderect(snow2_rect) or character_rect.colliderect(snow3_rect): #충돌했는지
        print("충돌")
        running = False

    if 25 <= score :
        snow_speed = 25
        level = 5
    elif 20 <= score:
        snow_speed = 19
        level = 4
    elif 15 <= score:
        snow_speed = 16
        level = 3
    elif 10 <= score :
        snow_speed = 13
        level = 2

    sL = game_font.render(f"Score : {score}, Level : {level}", True, (255, 255, 255))  # 카운트당 스코어가 오르게하고 화면에 스코어 메세지를 출력하게 함
    sL_rect = sL.get_rect()

    #5.화면 그리기기
    # screen.blit(background, (0,0))
    screen.fill(BLACK)
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(snow3, (snow_x3_pos, snow_y3_pos))
    screen.blit(snow2, (snow_x2_pos, snow_y2_pos))
    screen.blit(snow, (snow_x_pos, snow_y_pos))
    screen.blit(sL, sL_rect)  # 스코어 메세지 출력

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

def Click():
    messagebox.showinfo("종료", f"점수 : {score} , 단계 : {level} \n 종료되었습니다.")
Click()
# pygame 종료
pygame.quit()
