import pygame 
pygame.init()
def background(level):
    height=700
    width=400
    size=(400, 700)
    screen=pygame.display.set_mode(size)
    
    clock=pygame.time.Clock()
    background_image=pygame.image.load("Images/Background.png")
    background_image=pygame.transform.scale(background_image, (width, height))
    background_image1=pygame.image.load("Images/Background1.png")
    background_image1=pygame.transform.scale(background_image1, (width, height))
    background_image2=pygame.image.load("Images/Background2.png")
    background_image2=pygame.transform.scale(background_image2, (width, height))
    background_image3=pygame.image.load("Images/Background3.png")
    background_image3=pygame.transform.scale(background_image3, (width, height))
    
    if level==1:
        running=True
        pressed=False
        while running:
            click=pygame.mouse.get_pressed()
            if click[0]==1:
                pressed=True
            if pressed==True:
                screen.blit(background_image1, [0,0])
            else:
                screen.blit(background_image, [0,0])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            
            #pygame.display.update()
            pygame.display.flip()
            #Clock.tick(clock_tick_rate)
    elif level==2:
        """#pressed=False
        #while running:
        #Subject to change. Need modification for graphics extra
         click=pygame.mouse.get_pressed()
        if click[0]==1:
            pressed=True
        if pressed==True:
            screen.blit(background_image1, [0,0])
        else:
            screen.blit(background_image, [0,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False """
        running=True
        screen.blit(background_image2, [0,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    running=False
            
                
         #pygame.display.update()
        pygame.display.flip()
        #Clock.tick(clock_tick_rate)
        
    elif level==3:
         #pressed=False
        #while running:
            #Subject to change. Need modification for graphics extra
        """ click=pygame.mouse.get_pressed()
        if click[0]==1:
            pressed=True
        if pressed==True:
            screen.blit(background_image1, [0,0])
        else:
            screen.blit(background_image, [0,0])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False """
        running=True
        screen.blit(background_image3, [0,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
                
        #pygame.display.update()
        pygame.display.flip()
            #Clock.tick(clock_tick_rate)
background(3)