from pygame import *
from random import *


win_width = 900
win_height = 650
color_1 = 127
color_2 = 225
color_3 = 212

speed_x = 3
speed_y = 3



class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.a = player_width
        self.b = player_height
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y


class Rakets(GameSprite):
    def __init__(self, player_x, player_y, player_speed, player_width, player_height, r_left, r_right):
        super().__init__(player_x, player_y, player_speed, player_width, player_height)
        self.left = r_left
        self.right = r_right
    def make_raket(self):
        self.raket = Surface((self.a, self.b))
        self.raket.fill((225, 225, 225))
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.left] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[self.right] and self.rect.y < 550:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.raket, (self.rect.x,self.rect.y))

class Ball (GameSprite):
    def __init__(self, ball_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__(player_x, player_y, player_speed, player_width, player_height)
        self.image = ball_image
    def update(self):
        self.image = transform.scale(image.load(ball_image), (self.a,self.b))
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            self.kill()

window = display.set_mode((win_width,win_height))

window.fill((color_1, color_2, color_3))

display.set_caption('Пин-понг')

'''raket1 = Rakets(50, 50, 3, 20, 100, K_w, K_a)
raket1.make_raket()'''

ball = transform.scale(image.load(), (50, 200))


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    raket1.reset()

    display.update()




        
    
'''class Enemy (GameSprite):
    def __init__(self,player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
    def update(self):
        global win_height
        global win_width
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint (80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1'''



'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
rocket = Player('rocket.png', win_width/2-70/2, win_height-75, 8, 70, 70)
enemies = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, win_width - 100), 0, randint(1,4), 70, 70)
    enemies.add(enemy)
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                rocket.fire()
    rocket.reset()
    rocket.update()
    
    enemies.update()
    enemies.draw(window)
    
    text_life = font2.render ("Жизней осталось: " + str(life), 1, (255, 255, 255))
    window.blit(text_life, (10,80))
    sprites_list = sprite.groupcollide(enemies, bullets, True, True)
    if sprites_list != {}:
        enemies.add(Enemy('ufo.png', randint(0, win_width - 100), 0, randint(1,4), 70, 70))
        win=win+1
    
    
    text_win = font2.render ("Убито: " + str(win), 1, (255, 255, 255))
    text_lose = font2.render ("Пропущено: " + str(lost), 1, (255, 255, 255))
    
    window.blit(text_win, (10,20))
    window.blit(text_lose, (10,50))
    
    bullets.update()
    bullets.draw(window)
    display.update()
    clock.tick(FPS)'''