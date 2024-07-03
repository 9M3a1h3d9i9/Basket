import pygame
import random

class BG:
    def __init__ (self,source='BackG.PNG',max_x=500,max_y=500):
        self.bg = pygame.image.load(source)
        self.bg
    

class Ball:
    def __init__(self,source='fiba.PNG',scale=(50,50),vx=99,vy=0,x=0,y=0):
        self.ball=pygame.image.load(source)
        self.ball=pygame.transform.scale(self.ball,scale)
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
    
    def move(self, surface):
        self.x += self.vx
        self.y += self.vy
        if self.x >= surface.get_width() or self.x <=0:
            self.vx = -self.vx
        if self.y >= surface.get_height() or self.y <=0:
            self.vy = -self.vy
    
        surface.blit(self.ball,(self.x,400))

    def Control(move):
        def __init__(self,surface, ev = pygame.event.poll()):
            super(move , self).__init__ (surface)
            self.ev = ev

        def cont (self):
            while 1:
                if self.ev.type == pygame.QUIT:
                    break
                if self.ev.type == pygame.KEYDOWN:
                    if self.ev.key == pygame.K_RIGHT:
                        self.vx+=0.5
                    if self.ev.key == pygame.K_LEFT:
                        self.vx-=0.5
                    if self.ev.key == pygame.K_UP:
                        self.vy-=0.5
                    if self.ev.key == pygame.K_DOWN:
                        self.vy+=0.5
                if self.ev.type == pygame.KEYUP:
                    if self.ev.key == pygame.K_LEFT or self.ev.key == pygame.K_RIGHT or self.ev.key == pygame.K_UP or self.ev.key == pygame.K_DOWN:
                        self.vx,self.vy=0,0



pygame.init()
max_x,max_y = 500,500

Main_surface = pygame.display.set_mode((max_x,max_y))
p1 = pygame.image.load("BackG.PNG")
p1 = pygame.transform.scale(p1,(500,500))

main_surface = pygame.display.set_mode((max_x,max_y))
b1= Ball()

bg1=BG()

bmc1 = Ball()

while 1:
    
    ev = pygame.event.poll()
    bmc1.Control()

    if ev.type == pygame.QUIT:
        pygame.quit()
    
    Main_surface.blit(p1,(0,0))

    b1.move(main_surface)
    
    if ev.type != pygame.NOEVENT:
        print(ev)

    pygame.display.flip()


