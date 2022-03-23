import random
import pygame

pygame.init()
w = 1000
h = 700
sc = pygame.display.set_mode((w,h), pygame.DOUBLEBUF )
pygame.display.set_caption("Pong")
#Переменные
s1 = 0 #счёт1
s2 = 0 #счёт2
startgame = False
k1 = 1
k2 = 2
speed = 5
speed2 = 5
fps = 60
clock = pygame.time.Clock()

#colors
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
#Платформы
surf1 = pygame.Surface((30, 170))
surf1.fill(red)
rect1 = surf1.get_rect()
rect1.centery = 350;

surf2 = pygame.Surface((30, 170))
surf2.fill(blue)
rect2 = surf2.get_rect()
rect2.x = 970
rect2.centery = 350;
#Мяч
surf3 = pygame.Surface((44, 44))
surf3.fill(white)
pygame.draw.circle(surf3,black,(22,22),22)
rect3 = surf3.get_rect()
rect3.center = (500,350)

sc_rect = sc.get_rect()
#Шрифт
font = pygame.font.SysFont('arial',32)
font2 = pygame.font.SysFont('arial',30)
font3 = pygame.font.SysFont('arial', 64)
#Параметры надписей
follow1 = font.render("*Пробел* = начать",1,black,green)
follow2 = font.render("*BACKSPACE* = начать заново",1,black,green)
follow3 = font2.render("Скорость = {speed}",1,black,green)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        startgame = True

    if rect1.top < 0:
        rect1.top = 1
    if rect1.bottom > h:
        rect1.bottom = h
    if rect2.top < 0:
        rect2.top = 0
    if rect2.bottom > h:
        rect2.bottom = h

    if startgame == True:
        if keys[pygame.K_BACKSPACE]:
            s1 = 0
            s2 = 0
            fps = 60
            rect3.center = (500, random.randint(50, h - 50))
            startgame = False
            rect2.x = 970
            rect2.centery = 350;
            rect1.centery = 350;
            speed = 5

        if keys[pygame.K_w]:
            rect1.y -= speed2
        elif keys[pygame.K_s]:
            rect1.y += speed2
        if keys[pygame.K_UP]:
            rect2.y -= speed2
        elif keys[pygame.K_DOWN]:
            rect2.y += speed2
        rect3.centery+= speed * k1
        rect3.centerx-= speed // 2 * k2

    if rect3.bottom > h:
        k1 = -k1
    if rect3.top < 0:
        k1 = -k1

    if rect2.colliderect(rect3):
        speed += 0.5
        k2 = -k2
        rect3.centerx -= 1


    if rect1.colliderect(rect3):
        speed += 0.5
        k2 = -k2
        rect3.centerx += 3


    if rect3.left < 10:
        s2+=1
        speed = 5
        rect3.center = (500,random.randint(50,h-50))
    if rect3.right > w - 10:
        s1+=1
        speed = 5
        rect3.center = (500,random.randint(50,h-50))
    if fps<60:
        fps = 60
    if fps>100:
        fps = 100
    #ВЫвод скорости
    follow3 = font2.render(f"Скорость = {speed * 2}", 1, black)
    sch1 = font3.render(str(s1), 1, black)
    sch2 = font3.render(str(s2), 1, black)
    sc.fill(white)
    sc.blit(surf1,(0,rect1.y))
    sc.blit(surf2, (rect2.x, rect2.y))
    sc.blit(surf3,(rect3))
    #Отображение счёта
    sc.blit(sch1, (sc_rect.topleft))
    sc.blit(sch2, (sc_rect.right-35,sc_rect.top))
    #отображение скорости
    sc.blit(follow3, (sc_rect.centerx - 60, sc_rect.top))
    if startgame == False :
        sc.blit(follow1, (sc_rect.centery - 50, sc_rect.centerx - 86))
        sc.blit(follow2, (sc_rect.centery - 50, sc_rect.centerx - 50))

    pygame.display.update()
    clock.tick(fps)