import pygame
import sys

pygame.init()
pygame.display.set_caption("〇×ゲーム")
sysfont1 = pygame.font.SysFont(None, 50)
sysfont2 = pygame.font.SysFont(None, 60)
SURFACE = pygame.display.set_mode((400,300))
SURFACE.fill((255, 255, 255))
board =[[0 for i in range(3)] for j in range(3)]
flag = [1, 5]

def initialize():
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
    
def squeare():
    SURFACE.fill((255, 255, 255))
    pygame.draw.rect(SURFACE, (255, 140, 0), (90, 70, 190, 190))
    for x in range(9):
        left = (60 * (x // 3)) + 100
        top = (60 * (x % 3)) + 80
        pygame.draw.rect(SURFACE, (255, 228, 181), (left, top, 50, 50))
        pygame.display.update()

def circle(i, j):
    i = 125 + 60 * i
    j = 105 + 60 * j
    pygame.draw.circle(SURFACE, (255, 0, 0), (i,j), 22, 5)

def cross(i, j):
    st_left = 60 * i + 104
    st_top = 60 * j + 84
    st1 = (st_left, st_top)
    st2 = ((st_left + 42), st_top)
    end1 = (st_left + 42, st_top + 42)
    end2 = (st_left, (st_top + 42))
    pygame.draw.line(SURFACE, (0, 0, 255), st1, end1, 7)
    pygame.draw.line(SURFACE, (0, 0, 255), st2, end2, 7)


def caption(text):
    sysfont = pygame.font.SysFont(None, 72)
    message = sysfont.render(text, True, (0, 128, 128))
    message_rect = message.get_rect()
    message_rect.center = (200, 35)
    SURFACE.blit(message,message_rect)
    pygame.display.update()
    

def win_judge():
    for x in range(3):
        tate = board[x][0] + board[x][1] + board[x][2] 
        yoko = board[0][x] + board[1][x] + board[2][x]
        naname1 = board[0][0] + board[1][1] + board[2][2]
        naname2 = board[0][2] + board[1][1] + board[2][0]
        if tate == 3 or yoko == 3 or naname1 == 3 or naname2 == 3:
            caption("Round Win !")
            return (1)
        if tate == 15 or yoko == 15 or naname1 == 15 or naname2 == 15:
            caption("Cross Win !")
            return (1)
    return (0)

def drow_judge():
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return (0)
    caption("Drow !")
    return (1)
     
def draw(i, j):
    if board[i][j] == 1:
        circle(i, j)
    elif board[i][j] == 5:
        cross(i, j)
    pygame.display.update()

def judge():
    if win_judge():
        return (1)
    if drow_judge():
        return (1)
    return (0)
    
def chart_judge(x, y, ka):
    for i in range(3):
        if i * 60 + 100 <= x <= i * 60 + 150:
            for j in range(3):
                if j * 60 + 80 <= y <= j * 60 + 130:
                    if board[i][j] == 0:
                        board[i][j] = flag[ka % 2]
                        draw(i, j)
                        judge()
                        return(ka + 1)
    return(ka)
    
def draw_button(text2, charactar, x, y):
    SURFACE.fill((240, 250, 250))
    pygame.draw.rect(SURFACE, (200, 240, 100), (40, 80, 140, 50))
    pygame.draw.rect(SURFACE, (200, 240, 100), (220, 80, 140, 50))
    message = charactar.render(text2, True, (0, 128, 128))
    message2 = sysfont2.render("Quit", True, (0, 128, 128))
    SURFACE.blit(message,[x, y])
    SURFACE.blit(message2,[240, 90])
    pygame.display.update()

def judge_button(flag, x, y):
    if 80 <= y <= 130:
        if 40 <= x <= 180:
            return (1)
        elif 220 <= x <= 360:
            return (-1)
    return(flag)

def start():
    draw_button("Start!", sysfont2, 50, 90)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                return (judge_button(0, x, y))
            elif event.type == pygame.QUIT:
                return (-1)

def restart():
    draw_button("Restart!", sysfont1, 45, 90)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                return (judge_button(3, x, y))
            elif event.type == pygame.QUIT:
                return (-1)

def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return (3)
            elif event.type == pygame.QUIT:
                return (0)

def run_game():
    squeare()
    initialize()

    kaisuu = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                kaisuu = chart_judge(x, y, kaisuu)
                if judge():
                    return (2)
            elif event.type == pygame.QUIT:
                return (-1)

def main():
    game_flag = 0
    
    while True:
        if game_flag == 0:
            game_flag = start()
        if game_flag == 1:
            game_flag = run_game()
        if game_flag == 2:
            game_flag = pause()
        if game_flag == 3:
            game_flag = restart()
        if game_flag == -1:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
