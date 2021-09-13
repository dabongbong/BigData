# Cave 
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()                                           # pygame를 초기화.
pygame.key.set_repeat(5, 5)                             # 키의 반복 기능을 설정하는 pygame의 메서드, 키를 눌렀을때 KEYDOWN 이벤트를 생성하기 위해.
SURFACE = pygame.display.set_mode((800, 600))           # 화면 크기를 설정
FPSCLOCK = pygame.time.Clock()

def main():
    """메인루틴"""
    walls = 80                                          # 동굴을 구성하는 직 사각형의 수
    ship_y = 250                                        # 내 캐릭터의 y 좌표값
    velocity = 0                                        # 내 캐릭터가 상하로 이동하는 속도
    score = 0                                           # 점수
    slope = randint(1, 6)                               # 동굴의 기울기(옆 직사각형과 Y축 방향으로 얼마나 비켜 있는지)
    sysfont = pygame.font.SysFont(None, 36)             
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    holes = []                                          # 동굴을 구성하는 직사각형을 저장하는 배열
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))     # 동굴을 구성하는 직사각형을 생성.
        # Rect = pygame 안에 정의된 클래스, 인수는 (x좌표, y좌표, 폭, 높이), x축 방향으로 10씩 이동하며 직사각형을 wall개 생성. 만든 직사각형은 holes 리스트에 추가함.
    game_over = False                                   # 게임오버인지 아닌지 여부의 플래그

    while True:                                         # 초기화 후 메인루프에 진입함.
        is_space_down = False                           # (is_space_down = 스패이스키를 눌렀는가)루프를 시작하자 마자 is_space_down을 False로 초기화
        for event in pygame.event.get():                # 여기서 이벤트를 취득하고 이벤트가 QUIT이면 게임을 종료한다.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:                 # 이벤트 유형이 KEYDOWN(java의 Keypress?), 키 코드가 K_SPACE(스페이스키)이면 is_space_down을 True로 설정
                if event.key == K_SPACE:
                    is_space_down = True

        # 내 캐릭터를 이동
        if not game_over :                              # 게임 오버가 아닐때(게임 중)의 처리를 기술.
            score += 10                                 # 점수를 10점씩 증가시킴
            velocity += -3 if is_space_down else 3      # is_space_down이 True이면 y값 -3, False이면 +3
            ship_y += velocity                          # 속도를 비행기의 y값에 대입함.

            # 동굴을 스크롤
            edge = holes[-1].copy()                     # 오른쪽 끝의 직사각형을 복사해서 변수 edge에 저장함.
            test = edge.move(0, slope)                  # 직사각형을 이동시켜, 천장이나 바닥에 부딪히지 않는지를 검사함. edge를 Y축 방향으로 slope만큼 이동해 test에 담아둠
            if test.top <= 0 or test.bottom >= 600:     # 위에서 만든 test가 천장, 혹은 바닥에 닿았는지 판정함.
                slope = randint(1, 6) * (-1 if slope > 0 else 1)    # randint(1, 6) <- 기울기의 절대값을 난수로 생성 * (-1 if slope > 0 else 1) <- 기울기의 부호를 반전
                edge.inflate_ip(0, -20)                 # Y축 방향의 크기를 20만큼 작게함.
            edge.move_ip(10, slope)                     # edge(오른쪽 끝의 직사각형, 아직 화면에 표시 X)을 X축 방향으로 10, Y축 방향으로 slope(기울기)만큼 이동시킴
            holes.append(edge)                          # 제일 오른쪽 끝애 새로운 직사각형을 생성. 이때 화면 밖 가장 끝에 새로운 직사각형 생성.
            del holes[0]                                # 가장 왼쪽에 있는 직사각형을 삭제
            holes = [x.move(-10, 0) for x in holes]     # 전체 직사각형을 왼쪽으로 10만큼 이동함

            if holes[0].top > ship_y or holes[0].bottom < ship_y + 80:  # 캐릭터가 벽에 충돌했는지를 판별하는 if문.
                game_over = True                        # ship_y 는 내 캐릭터의 y축값. 즉 비행기의 윗쪽부분. 아랫쪽부분은 ship_y + 80으로 설정. 이걸 줄이면 
                                                        # 아랫쪽 판정이 넉넉해짐. 결국 80만큼의 크기의 비행기가 가장 왼쪽 끝(holes[0])의 직사각형 안에 들어있는지 판별

        # 그리기
        SURFACE.fill((0, 255, 0))                       # 배경을 녹색으로 칠함.
        for hole in holes:                              # 동굴 안의 직사각형을 그림
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, ship_y))           # 내 캐릭터를 그림
        score_image = sysfont.render("score is {}".format(score), True, (0, 0, 225))    # 화면 우측 상단에 점수를 나타냄
        SURFACE.blit(score_image, (600, 20))

        if game_over:                                   # 게임오버시 비행기가 터지는 이미지를 표시함
            SURFACE.blit(bang_image, (0, ship_y - 40))

        pygame.display.update()                         # 위의 그리기를 화면에 반영(= Rander)
        FPSCLOCK.tick(15)                               # FPS를 설정함

if __name__ == '__main__':
    main()
