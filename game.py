import sys
import pygame as pg
import random
from pygame.locals import *
from button import Button
import time
def load_sprite(endereço, sprites):
    sprites += 1
    endereços = []
    for frame in range(1, sprites):
        newlocal = endereço + '/' + str(frame) + '.png'
        endereços.append(newlocal)
        if frame + 1 == sprites:
            return endereços        

def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)      
class game:
    def __init__(self):
        self.janela = pg.display.set_mode((1080,2640),pg.FULLSCREEN)
        # vars controle pygame
        pos_y = random.randint(- 6000, -630)
        pos_y2 = random.randint(- 5000, -630)
        pos_x = 70
        pos_x2 = 600
        speed = 90
        clock = pg.time.Clock()
        surfrect = self.janela.get_rect()
        rect = pg.Rect((0, 0), (357, 630))
        rect.center = (surfrect.w / 2, surfrect.h / 2)
        touched = False
        # sprites loading
        local = "/storage/emulated/0/Trafic Car Game/assets"
        sprites = load_sprite(local, 5)
        t1 = time.time()
        player = pg.image.load(sprites[0])
        pista = pg.image.load(local + "/pista.png")
        game_loop = True
        car_esq = pg.image.load(sprites[random.randint(0, 4)])
        car_dir = pg.image.load(sprites[random.randint(0, 4)])       
        while game_loop:
            t2 = time.time()
            delta = t2 - t1
            for ev in pg.event.get():
                if ev.type == QUIT:
                    pg.quit()
                elif ev.type == pg.MOUSEBUTTONDOWN:
                    if rect.collidepoint(ev.pos):
                        touched = True
                        # This is the starting point
                        pg.mouse.get_rel()
                    elif ev.type == pg.MOUSEBUTTONUP:
                        touched = False
                clock.tick(60)
                #self.janela.blit(pista, (0,0))
                if touched:
                    rect.move_ip(pg.mouse.get_rel())
                    rect.clamp_ip(surfrect)
                self.janela.blit(pista, (0,0))
                self.janela.blit(player, (rect))
                self.janela.blit(car_esq, (pos_x, pos_y))
                self.janela.blit(car_dir,(pos_x2 , pos_y2))
                # animacao de game over
                bateu = False
                
                	
                pos_y += speed 
                pos_y2 += speed
                
                
                # colisao
                if (pos_x + 357 >= rect.x + 357) and (pos_y + 630  >= rect.y + 630):
                	print("bateu esq")
                	bateu = True 
                	
                elif (pos_x2 + 357 <= rect.x + 357 ) and (pos_y2+ 630 >= rect.y + 630):
                	print("bateu dir")
                	bateu = True
                	
                if bateu:
                	GAME_OVER = pg.image.load("/storage/emulated/0/Trafic Car Game/assets/over.png")
                	speed = 0
                	print('STOP')
                	self.janela.blit(GAME_OVER, (0,0))
                	if touched:
                		bateu = False
                
                # posicionando carro aleatoriamente	
                if pos_y2 >= 2900:
                	pos_y2 = random.randint(- 3000, -630)
                	car_dir = pg.image.load(random.choice(sprites))
       
                if pos_y >= 2780:
                	pos_y = - 2000
                	car_esq = pg.image.load(random.choice(sprites))
                	pos_y = random.randint(- 2000, -630)
               # pg.display.flip()
                pg.display.update()
                print(f"speed {speed}, pos_y {pos_y} pos_y2 {pos_y2}, rect {rect}")
