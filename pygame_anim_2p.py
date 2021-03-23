''' pygame Animation '''

#importing only required things
from pygame.display import set_mode, set_caption, update
from pygame.image import load
from pygame.time import Clock
from pygame.draw import circle
from pygame import init, quit, event, key, QUIT
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
from pygame import K_a, K_d, K_w, K_f


init ()


class window :
    def __init__ (self, size = (600, 400), title = 'pygame surface') :
        self.surface = set_mode ()
        self.size = size
        self.title = title
        self.bg_img = load (r'images\bg.jpg')

        #displaying the changes
        set_mode (self.size)
        set_caption (self.title)
        return




class player :
    def __init__ (self, x, y, height, width) :
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 3
        self.isjump = False
        self.jumpCount = 10
        self.jump_factor = .25
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.neg = 1
        self.bulletlist = []
        self.health = 10
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
                self.y -= round (self.jumpCount ** 2 * self.jump_factor * self.neg)
                self.jumpCount -= 1
            else :
                self.isjump = False
                self.jumpCount = 10
                self.neg = 1
        else :
            self.standing = True
        return

    def fire (self) :
        if len (self.bulletlist) < 3 :
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
                win.surface.blit (image_list_left [self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right :
                win.surface.blit (image_list_right [self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else :
            if self.left :
                win.surface.blit (image_list_left [0], (self.x, self.y))
            elif self.right :
                win.surface.blit (image_list_right [0], (self.x, self.y))
            else :
                win.surface.blit (image_list_stand [0], (self.x, self.y))
        return




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
            self.x = self.player.x + self.player.width // 2
            self.y = self.player.y + self.player.height // 2
            return 1
        else :
            pass
        return

    def show (self, enemy = None) :
        if self.x <= win.size [0] and self.x >= 0 :
            self.x += self.vel
            if enemy :
                gap_x = enemy.x + enemy.width // 2 - self.x
                gap_y = enemy.y + enemy.height //2 - self.y
                dir = abs (self.vel) // self.vel
                
                if abs (gap_y) <= enemy.width // 2 :
                    if dir == -1 and gap_x >= -1 * enemy.width // 2 and gap_x < 0:
                        enemy.health -= 2
                        return
                    elif dir == 1 and gap_x <= enemy.width // 2 and gap_x > 0 :
                        enemy.health -= 2
                        return
                
            circle (win.surface, self.color, (self.x, self.y), 5)
            return 1
        else :
            return



def refresh_display () :
    win.surface.blit (win.bg_img, (0, 0))
    if p_list :
        index = 0
        while True:
            #terminating condition
            if index >= len (p_list) :
                break
            
            #set the player 
            player = p_list [index]

            #checking if bulletlist is not empty
            if player.bulletlist :
                
                #accessing every bullet in the players bulletlist
                for my_bullet in player.bulletlist :

                    idx = 0
                    #accessing the enemies of the player
                    while True :
                        if idx >= len (p_list) :
                            break
                        if idx != index :
                            enemy = p_list [idx]
                            if not (my_bullet.show (enemy)) :
                                player.bulletlist.remove (my_bullet)
                                if enemy.health == 0 :
                                    p_list.remove (enemy)
                                    continue
                                idx += 1
                            else :
                                idx += 1
                        else:
                            idx += 1

                    #when the enemy list is empty
                    if len (p_list) == 1 :
                        if not (my_bullet.show ()) :
                            player.bulletlist.remove (my_bullet)
                        else :
                            pass
            player.show ()
            index += 1
            
    update ()
    return




#main loop and global variables
win = window ((850, 480), 'Character Animation')
win.surface.blit (win.bg_img, (0, 0))

#absolute path
abs_path = r'D:/python_versions/python 3.7.6 64/Visual_game/pvse/images/'
#list of images to be used in the game
image_list_left = [ load (abs_path + 'L1.png'), load (abs_path + 'L2.png'), load (abs_path + 'L3.png'),
                    load (abs_path + 'L4.png'), load (abs_path + 'L5.png'), load (abs_path + 'L6.png'),
                    load (abs_path + 'L7.png'), load (abs_path + 'L8.png'), load (abs_path + 'L9.png'),
                   ]

image_list_stand = [ load (abs_path + 'standing.png') ]

image_list_right = [ load (abs_path + 'R1.png'), load (abs_path + 'R2.png'), load (abs_path + 'R3.png'),
                     load (abs_path + 'R4.png'), load (abs_path + 'R5.png'), load (abs_path + 'R6.png'),
                     load (abs_path + 'R7.png'), load (abs_path + 'R8.png'), load (abs_path + 'R9.png'),
                    ]


#first instance of the player class            
my_p1 = player (225, 396, 64, 64)
my_p1.id (my_p1)

my_p2 = player (625, 396, 64, 64)
my_p2.id (my_p2)


#players' list
p_list = [my_p1, my_p2]


#creating the clock variable
clock = Clock ()


#setting the main loop variable True
run = True



#The Main LOOP
while run :
    clock.tick (27)

    #getting the list of all events 
    for EVENT in event.get () :
        if EVENT.type == QUIT :
            run = False

    keys = key.get_pressed ()
    
    #checking for the events for the first player with the arrow buttons
    if keys [K_LEFT] and my_p1.x > 0 :
        my_p1.update ('left')
    elif keys [K_RIGHT] and my_p1.x < (win.size [0] - my_p1.width) :
        my_p1.update ('right')
    elif keys [K_SPACE] :
        my_p1.fire ()
        pass
    else :
        my_p1.update ()

    if not my_p1.isjump :
        #setting the jump variable True
        if keys [K_UP] :
            my_p1.update ('up')
    else :
        #the jump
        my_p1.update ('jump')


    #checking for the events for the second player with the asdw buttons
    if keys [K_a] and my_p2.x > 0 :
        my_p2.update ('left')
    elif keys [K_d] and my_p2.x < (win.size [0] - my_p2.width) :
        my_p2.update ('right')
    elif keys [K_f] :
        my_p2.fire ()
        pass
    else :
        my_p2.update ()

    if not my_p2.isjump :
        #setting the jump variable True
        if keys [K_w] :
            my_p2.update ('up')
    else :
        #the jump
        my_p2.update ('jump')
        
    #updating the surface of the window
    refresh_display ()



#python pygame program quit statement
quit ()
