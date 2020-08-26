import pygame 
pygame.init()
slide_mas = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Slide master")
#################   Variables  ###################
x_axis = 45
y_axis = 55
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_axis+=10
            if event.key==pygame.K_LEFT:
                x_axis-=10
            if event.key==pygame.K_DOWN:
                y_axis+=10
            if event.key==pygame.K_UP:
                y_axis-=10
    slide_mas.fill((255,255,255))
    img = pygame.image.load(r'C:\Users\Codemaster\Desktop\Untitled.png')
    slide_mas.blit(img,(x_axis+425,y_axis-15))
    # neck = pygame.draw.rect(slide_mas,(255,40,90),[x_axis+240,y_axis+50,20,50])
    # head = pygame.draw.circle(slide_mas,(255,0,0),[x_axis+250,y_axis+30],50)
    # cheat =pygame.draw.rect(slide_mas,(0,250,0),[x_axis+190,y_axis+100,120,200])
    # hand1_line1 =  pygame.draw.line(slide_mas,(255,40,20),[x_axis+190,y_axis+100],(x_axis+55,y_axis+205))
    # hand1_line2 = pygame.draw.line(slide_mas,(255,40,20),[x_axis+190,y_axis+150],(x_axis+75,y_axis+240))
    # hand2_line1  = pygame.draw.line(slide_mas,(255,40,20),[x_axis+310,y_axis+100],(x_axis+415,y_axis+200))
    # hand2_line2 =  pygame.draw.line(slide_mas,(255,40,20),[x_axis+310,y_axis+150],(x_axis+415,y_axis+250))
    # leg1 =  pygame.draw.rect(slide_mas,(0,0,95),[x_axis+220,y_axis+300,25,80])
    # leg2 =  pygame.draw.rect(slide_mas,(100,25,0),[x_axis+270,y_axis+300,25,80])
    pygame.display.update()
    clock.tick(30)