import pygame

pygame.init()

M_S = pygame.display.set_mode((500,500))
S_r = [400,470,100,30]
S_c = [55,55,255]

my_font = pygame.font.SysFont("courier",18)
the_text = my_font.render("Score:",True,(255,255,255))
the_text2 = my_font.render("0",True,(255,255,255))
the_text3 = my_font.render("1",True,(255,255,255))

BG = pygame.image.load("BackG.PNG")
BG = pygame.transform.scale(BG,(500,500))

WinBG = pygame.image.load("Win.PNG")
WinBG = pygame.transform.scale(WinBG,(500,500))


ball3 = pygame.image.load('fiba.PNG')
ball3 = pygame.transform.scale(ball3,(50,50))

ball2 = pygame.image.load('fiba.PNG')
ball2 = pygame.transform.scale(ball2,(30,30))

ball1 = pygame.image.load('fiba.PNG')
ball1 = pygame.transform.scale(ball1,(35,35))

ball0 = pygame.image.load('fiba.PNG')
ball0 = pygame.transform.scale(ball0,(45,45))


ball = pygame.image.load('fiba.PNG')
ball = pygame.transform.scale(ball,(25,25))



x,y = 250,400
x0,y0 = 239,65




while True:
    ev = pygame.event.poll()

    if ev.type == pygame.QUIT:
        pygame.quit()
    
    #if ev.type != pygame.NOEVENT:
    #    print(ev)
    
    if ev.type == pygame.MOUSEMOTION:
        x,y = ev.pos

    
    
    if M_S.blit(ball,(x,y)) !=  M_S.blit(ball,(x0,y0)) or M_S.blit(ball,(x0-1,y0)) or M_S.blit(ball,(x0+1,y0)) or M_S.blit(ball,(x0,y0-1)) or M_S.blit(ball,(x0,y0+1)) :
        M_S.blit(BG,(0,0))
        M_S.fill(S_c,S_r)
        M_S.blit(the_text,(415,480))
        M_S.blit(the_text2,(485,480))
    
        

    if M_S.blit(ball,(x,y)) == M_S.blit(ball,(x0,y0))  :
        
        M_S.blit(WinBG,(0,0))
        M_S.fill(S_c,S_r)
        M_S.blit(the_text,(415,480))
        M_S.blit(the_text3,(485,480))

    
    M_S.blit(ball,(x,y))



    pygame.display.flip()

    