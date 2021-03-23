''' pygame Animation '''

import pygame

#the initialiser function
pygame.init ()


class window :
    def __init__ (self, size = (600, 400), title = 'pygame surface') :
        self.surface = pygame.display.set_mode ()
        self.size = size
        self.title = title
        self.bg_img = pygame.image.load (r'images\bg.jpg')

        #displaying the changes
        pygame.display.set_mode (self.size)
        pygame.display.set_caption (self.title)
        return




class player (object) :
    #list of images to be used in the game
    image_list_left = [ pygame.image.load (r'images\L1.png'), pygame.image.load (r'images\L2.png'),  pygame.image.load (r'images\L3.png'),
                        pygame.image.load (r'images\L4.png'), pygame.image.load (r'images\L5.png'), pygame.image.load (r'images\L6.png'),
                        pygame.image.load (r'images\L7.png'), pygame.image.load (r'images\L8.png'), pygame.image.load (r'images\L9.png'),
                       ]

    image_list_stand = [ pygame.image.load (r'images\standing.png') ]

    image_list_right = [ pygame.image.load (r'images\R1.png'), pygame.image.load (r'images\R2.png'), pygame.image.load (r'images\R3.png'),
                         pygame.image.load (r'images\R4.png'), pygame.image.load (r'images\R5.png'), pygame.image.load (r'images\R6.png'),
                         pygame.image.load (r'images\R7.png'), pygame.image.load (r'images\R8.png'), pygame.image.load (r'images\R9.png'),
                        ]

    def __init__ (self, x, y, height, width) :
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 4
        self.isjump = False
        self.jumpCount = 10
        self.jump_factor = .4
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.neg = 1
        self.bulletlist = []
        self.bulletloop = 0
        self.hitbox = (self.x + 17, self.y + 15, 28, 48)
        self.score = 0
        return

    def id (self, name) :
        self.name = name
        return
    
    def update (self, dir = None) :
        if dir == 'left' :
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
        elif dir == 'right' :
            self.x += self.vel
            self.left = False
            self.right = True
            self.standing = False
        elif dir == 'up' :
            self.isjump = True
            self.standing = True
        elif dir == 'jump' :
            if self.jumpCount >= -10 :
                if self.jumpCount < 0 :
                    self.neg = -1
                self.y -= self.jumpCount ** 2 * self.jump_factor * self.neg
                self.jumpCount -= 1
            else :
                self.isjump = False
                self.jumpCount = 10
                self.neg = 1
        else :
            self.standing = True
        self.hitbox = (self.x + 17, self.y + 15, 28, 48)
        return

    def fire (self) :
        self.bulletloop += 1
        if len (self.bulletlist) < 5 :
            b = bullet (5, (0, 0, 0), 10, self.name)
            if b.draw () :
                self.bulletlist.append (b)
            else :
                pass
        pass
    
    def show (self) :
        if self.walkCount + 1 > 27 :
            self.walkCount = 0
        else :
            pass
        if not self.standing :
            if self.left :
                win.surface.blit (my_p1.image_list_left [self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right :
                win.surface.blit (my_p1.image_list_right [self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else :
            if self.left :
                win.surface.blit (my_p1.image_list_left [0], (self.x, self.y))
            elif self.right :
                win.surface.blit (my_p1.image_list_right [0], (self.x, self.y))
            else :
                win.surface.blit (my_p1.image_list_stand [0], (self.x, self.y))
        return

    def collision (self) :
        #the info
        dec = FONT_.render ('-50', 1, (255, 0, 0))
        win.surface.blit (dec, (425, 150))
        pygame.display.update ()
        
        #delaying mechanism
        for delay in range (0, 1000) :
            for fur_delay in range (0, 1000) :
                for event in pygame.event.get () :
                    if event.type == pygame.QUIT :
                        pygame.quit ()

        #the resetting
        self.x = 225
        self.y = 396
        self.left = False
        self.right = False
        self.standing = True
        self.neg = 1
        self.bulletlist = []
        self.bulletloop = 0
        self.hitbox = (self.x + 17, self.y + 15, 28, 48)
        self.isjump = False
        self.jumpCount = 10
        self.score -= 50
        


    

#enemy
class enemy (object) :
    enemy_left = [ pygame.image.load (r'images\L1E.png'), pygame.image.load (r'images\L2E.png'), pygame.image.load (r'images\L3E.png'),
                   pygame.image.load (r'images\L4E.png'), pygame.image.load (r'images\L5E.png'), pygame.image.load (r'images\L6E.png'),
                   pygame.image.load (r'images\L7E.png'), pygame.image.load (r'images\L8E.png'), pygame.image.load (r'images\L9E.png'),
                   pygame.image.load (r'images\L10E.png'), pygame.image.load (r'images\L11E.png')
                   ]
    enemy_right = [ pygame.image.load (r'images\R1E.png'), pygame.image.load (r'images\R2E.png'), pygame.image.load (r'images\R3E.png'),
                    pygame.image.load (r'images\R4E.png'), pygame.image.load (r'images\R5E.png'), pygame.image.load (r'images\R6E.png'),
                    pygame.image.load (r'images\R7E.png'), pygame.image.load (r'images\R8E.png'), pygame.image.load (r'images\R9E.png'),
                    pygame.image.load (r'images\R10E.png'), pygame.image.load (r'images\R11E.png')
                    ]
    
    def __init__ (self, x, y, width, height) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 20, self.y + 2, 30, 58)
        self.path = (0, win.size [0])
        self.vel = -2
        self.walkCount = 0
        self.health = 50
        self.healthbox = (self.hitbox [0] - 10, self.hitbox [1] - 5, self.hitbox [2] - 30 + self.health, 5)
        self.visible = True
        return

    def update (self) :
        #updating the hitbox and enemies position
        if self.x + self.width + self.vel < self.path [1] and self.x + self.vel > self.path [0] :
            self.x += self.vel
            if self.vel > 0 :
                self.hitbox = (self.x + 15, self.y + 2, 30, 58)
            else :
                self.hitbox = (self.x + 25, self.y + 2, 30, 58)
        else :
            self.vel *= -1

        #updating the health box
        self.healthbox = (self.hitbox [0] - 10, self.hitbox [1] - 5, self.hitbox [2] - 30 + self.health, 5)
        
        #updating the walkCount variable
        if self.walkCount + 1 < 33 :
            self.walkCount += 1
        else :
            self.walkCount = 0
        return

    def hit (self) :
        if self.health - 1 > 0 :
            self.health -= 1
        else :
            self.visible = False
    
    def show (self) :
        #displaying the enemy
        if self.vel < 0 :
            win.surface.blit (goblin.enemy_left [self.walkCount // 3], (self.x, self.y))
        else :
            win.surface.blit (goblin.enemy_right [self.walkCount // 3], (self.x, self.y))

        #displaying the health bar
        pygame.draw.rect (win.surface, (255, 0, 0), (self.hitbox [0] - 10, self.hitbox [1] - 5, self.hitbox [2] + 20, 5))
        pygame.draw.rect (win.surface, (0, 0, 255), self.healthbox)


class bullet :
    def __init__ (self, radius, color, vel, player) :
        self.radius = radius
        self.color = color
        self.vel = vel
        self.player = player
        if player.left :
            self.vel = -1 * abs (self.vel)
        elif player.right :
            self.vel = self.vel
        else :
            self.vel = 0
        return

    def draw (self) :
        if self.vel :
            self.x = round (self.player.x + self.player.width // 2)
            self.y = round (self.player.y + self.player.height // 2)
            return 1
        else :
            pass
        return

    def show (self) :
        if self.x <= win.size [0] and self.x >= 0 :
            if goblin.visible :
                if (self.x > goblin.hitbox [0] and self.x < goblin.hitbox [0] + goblin.hitbox [2]) :
                    if (self.y > goblin.hitbox [1] and self.y < goblin.hitbox [1] + goblin.hitbox [3]) :
                        goblin.hit ()
                        my_p1.score += 1
                        if self.vel * goblin.vel > 0 :
                            goblin.vel *= -1
                        self.player.bulletlist.remove (self)
                        return
            pygame.draw.circle (win.surface, self.color, (self.x, self.y), 5)
            self.x += self.vel 
        else :
            self.player.bulletlist.remove (self)
        return
    


def refresh_display () :
    win.surface.blit (win.bg_img, (0, 0))

    #the scorecard
    text = FONT.render ('Score : ' + str (my_p1.score), 1, (0, 0, 0))
    win.surface.blit (text, (600, 40))

    #for the player
    my_p1.show ()

    #for the enemy
    if goblin.visible :
        goblin.show ()
        goblin.update ()
        #pygame.draw.rect (win.surface, (255, 0, 0), goblin.hitbox, 2)


    #checking whether the enemy is alive or dead
    if goblin.visible :
        #checking the collision condition
        if (my_p1.hitbox [0] + my_p1.hitbox [2] < goblin.hitbox [0]) or (goblin.hitbox [0] + goblin.hitbox [2] < my_p1.hitbox [0]) or (my_p1.hitbox [1] + my_p1.hitbox [3] < goblin.hitbox [1]) :
            pass
        else :
            #reset the player
            my_p1.collision ()

            #reset the goblin
            goblin.x = 625
            goblin.y = 400
            goblin.health = 50
            
    #pygame.draw.rect (win.surface, (255, 0, 0), my_p1.hitbox, 2)

    #for the bullets of the player
    for my_bullet in my_p1.bulletlist :
        my_bullet.show ()


    #screen update
    pygame.display.update ()
    return




#main loop and global variables
win = window ((850, 480), 'Character Animation')
win.surface.blit (win.bg_img, (0, 0))

    
#first instance of the player class and the enemy class
my_p1 = player (225, 396, 64, 64)
my_p1.id (my_p1)

goblin = enemy (625, 400, 64, 64)

FONT = pygame.font.SysFont ('Century', 24, True)
FONT_ = pygame.font.SysFont ('Century', 50, True)


#creating the clock variable
clock = pygame.time.Clock ()

#setting the main loop variable True
run = True


#The Main LOOP
while run :
    clock.tick (27)
    if my_p1.bulletloop :
        if my_p1.bulletloop == 5 :
            my_p1.bulletloop = 0
        else :
            my_p1.bulletloop += 1

    #getting the list of all events 
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed ()
    
    #checking for the events with the arrow buttons
    if keys [pygame.K_LEFT] and my_p1.x > 0 :
        my_p1.update ('left')
    elif keys [pygame.K_RIGHT] and my_p1.x < (win.size [0] - my_p1.width) :
        my_p1.update ('right')
    elif keys [pygame.K_SPACE] and not (my_p1.bulletloop) :
        my_p1.fire ()
    else :
        my_p1.update ()

    if not my_p1.isjump :
        #setting the jump variable True
        if keys [pygame.K_UP] :
            my_p1.update ('up')
    else :
        #the jump
        my_p1.update ('jump')
        
    #updating the surface of the window
    refresh_display ()


#python pygame program quit statement
pygame.quit ()
