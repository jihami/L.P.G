import pygame
#기본초기화
pygame.init()
#화면 크기 설정, 타이틀
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Loding Python Game")
clock = pygame.time.Clock()
# icon = pygame.image.load("<< <<image_Nmae>>.<<extension>> >>")
# pygame.display.set_icon(icon)

#폰트
game_font = pygame.font.Font(None, 80)
black = (0,0,0)
white = (255,255,255)

#1.사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
running = True
while running:
    dt = clock.tick(30)
    #2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #3.게임 캐릭터 위치 정의

    #텍스트 직사각형 영역 설정
    title = game_font.render("L . P . G", True, white)
    title_Rect = title.get_rect()
    title_Rect.centerx = round(screen_width/2)
    title_Rect.centery = round(screen_height/2)

    #4.충돌처리

    #5.화면 그리기기
    screen.blit(title, title_Rect)

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종료
pygame.quit()
