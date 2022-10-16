import pygame 
pygame.init()

class BackgroundManager:
    def __init__(self):
        self.width, self.height = 400, 700
        self.size = (400, 700)

        self.load_screen_background = pygame.image.load("Images/LoadBackground.png")
        self.load_screen_background = pygame.transform.scale(self.load_screen_background, self.size)
        self.game_background = pygame.image.load("Images/Background.png")
        self.game_background = pygame.transform.scale(self.game_background, self.size)
        self.orange_background = pygame.image.load('Images/orange background.png')
        self.orange_background = pygame.transform.scale(self.orange_background, self.size)

        #daily reward
        self.reward1 = pygame.image.load('Images/reward1.png')
        self.reward2 = pygame.image.load('Images/reward2.png')
        self.reward3 = pygame.image.load('Images/reward3.png')

        #store
        self.store_background = pygame.image.load('Images/pink background.png')
        self.store_background = pygame.transform.scale(self.store_background, self.size)
        self.store_board = pygame.image.load('Images\store board.png')
        self.pi_board = pygame.image.load('Images\pi store.png')


    def render_background(self, screen, level):
        if level == 1:
            screen.blit(self.load_screen_background, [0,0])
        elif level == 0:
            screen.blit(self.orange_background, [0,0])
            screen.blit(self.reward1, [60, 60])
            screen.blit(self.reward2, [220, 60])
            screen.blit(self.reward3, [90, 300])
        elif level == 5:
            screen.blit(self.store_background, [0,0])
            screen.blit(self.store_board, [65, 40])
            screen.blit(self.pi_board, [65, 300])
        else:
            screen.blit(self.game_background, [0,0])


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
# background(1)

    