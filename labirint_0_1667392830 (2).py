from pygame import *
 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed, orien):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.orien = orien
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.orien=orien
    def update(self): 
        if player1.rect.x <= win_width-45 and player1.x_speed > 0 or player1.rect.x >= 0 and player1.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if player1.rect.y <= win_height-45 and player1.y_speed > 0 or player1.rect.y >= 0 and player1.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    
    def fire(self):
        bullet = Bullet('bullet_right.png', self.rect.left, self.rect.centery, 30, 25, 15)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet('bullet_left.png', self.rect.right, self.rect.centery, 30, 25, -15)
        bullets.add(bullet)  


class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_x1, start_x2):

        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2


    def update(self):
        if self.rect.x <= self.start_x1: 
            self.side = "right"
        if self.rect.x >= self.start_x2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()

font.init()
font1=font.SysFont("Times", 36)

coins_amount_1 = 0


win_width = 1370
win_height = 725
window = display.set_mode((win_width, win_height))
display.set_caption("Лабіринт")
back = transform.scale(image.load('background.jpg'), (1370, 725))

barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
coins = sprite.Group()

w1 = GameSprite('platform1.png', 0, 0, 30, 725)
w2 = GameSprite('platform2.png', 30, 550, 250, 30)
w3 = GameSprite('platform1.png', 700, 600, 30, 140)
w4 = GameSprite('platform1.png', 1340, 0, 30, 760)

w5 = GameSprite('platform1.png', 120, 80, 30, 170)
w6 = GameSprite('platform1.png', 240, 0, 30, 90)
w7 = GameSprite('platform2.png', 30, 250, 120, 30)
w8 = GameSprite('platform2.png', 150, 150, 270, 30)
w9 = GameSprite('platform1.png', 390, 60, 30, 90)
w10 = GameSprite('platform1.png', 250, 180, 30, 120)
w11 = GameSprite('platform2.png', 30, 370, 360, 30)
w12 = GameSprite('platform1.png', 360, 250, 30, 120)
w13 = GameSprite('platform1.png', 600, 0, 30, 90)
w14 = GameSprite('platform1.png', 100, 400, 30, 100)
w15 = GameSprite('platform1.png', 250, 450, 30, 190)
w16 = GameSprite('platform1.png', 100, 580, 30, 70)
w17 = GameSprite('platform1.png', 420, 450, 30, 150)
w18 = GameSprite('platform2.png', 390, 250, 300, 30)
w19 = GameSprite('platform2.png', 450, 450, 120, 30)
w20 = GameSprite('platform2.png', 420, 600, 450, 30)
w21 = GameSprite('platform1.png', 570, 390, 30, 150)
w22 = GameSprite('platform1.png', 660, 280, 30, 150)
w23 = GameSprite('platform2.png', 600, 510, 100, 30)
w24 = GameSprite('platform2.png', 690, 400, 150, 30)
w25 = GameSprite('platform2.png', 500, 150, 350, 30)
w26 = GameSprite('platform1.png', 750, 180, 30, 150)
w27 = GameSprite('platform1.png', 850, 50, 30, 250)
w28 = GameSprite('platform2.png', 880, 50, 150, 30)
w29 = GameSprite('platform1.png', 1000, 80, 30, 550)
w30 = GameSprite('platform2.png', 1030, 400, 150, 30)
w31 = GameSprite('platform1.png', 1170, 200, 30, 400)
w32 = GameSprite('platform2.png', 1170, 180, 170, 30)
w33 = GameSprite('platform2.png', 1170, 50, 170, 30)
w34 = GameSprite('platform2.png', 1030, 220, 70, 30)
w35 = GameSprite('platform2.png', 1100, 300, 70, 30)





barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
barriers.add(w23)
barriers.add(w24)
barriers.add(w25)
barriers.add(w26)
barriers.add(w27)
barriers.add(w28)
barriers.add(w29)
barriers.add(w30)
barriers.add(w31)
barriers.add(w32)
barriers.add(w33)
barriers.add(w34)
barriers.add(w35)

coin1 = GameSprite('coin.png', 60, 210, 30, 30)
coin2 = GameSprite('coin.png', 50, 600, 30, 30)
coin3 = GameSprite('coin.png', 190, 195, 30, 30)
coin4 = GameSprite('coin.png', 475, 500, 30, 30)
coin5 = GameSprite('coin.png', 800, 200, 30, 30)
coin6 = GameSprite('coin.png', 750, 650, 30, 30)
coin7 = GameSprite('coin.png', 1270, 15, 30, 30)
coin8 = GameSprite('coin.png', 1260, 240, 30, 30)
coin9 = GameSprite('coin.png', 1140, 350, 30, 30)


coins.add(coin1)
coins.add(coin2)
coins.add(coin3)
coins.add(coin4)
coins.add(coin5)
coins.add(coin6)
coins.add(coin7)
coins.add(coin8)
coins.add(coin9)


player1 = Player('hero.png', 45, 430, 45, 45, 0, 0, "right")
monster1 = Enemy('enemy.png', 50, 305, 60, 60, 2, 40, 305)
monster2 = Enemy('enemy.png', 250, 640, 60, 60, 4, 120, 630)
monster3 = Enemy('enemy.png', 850, 640, 60, 60, 4, 790, 1260)
monster4 = Enemy('enemy.png', 500, 90, 60, 60, 2, 420, 785)
monster5 = Enemy('enemy.png', 200, 90, 60, 60, 4, 150, 330)
final_sprite = GameSprite('finish.png',  1240, 90, 80, 80)


monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)



finish = False
run = True
while run:
 
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                player1.x_speed = -5
            elif e.key == K_d:
                player1.x_speed = 5
            elif e.key == K_w:
                player1.y_speed = -5
            elif e.key == K_s:
                player1.y_speed = 5
            elif e.key == K_LEFT:
                player1.fire2()
            elif e.key == K_RIGHT:
                player1.fire()

        elif e.type == KEYUP:
            if e.key == K_a:
                player1.x_speed = 0
            elif e.key == K_d:
                player1.x_speed = 0
            elif e.key == K_w:
                player1.y_speed = 0
            elif e.key == K_s:
                player1.y_speed = 0
    if not finish:
        window.blit(back,(0,0))
        barriers.draw(window)
        coins.draw(window)
        player1.reset()
        bullets.update()
        bullets.draw(window)
        player1.update()
        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)

        if sprite.spritecollide(player1, coins, True):
            coins_amount_1 += 1
        coin = font1.render(f'Квіточок : {coins_amount_1}', True, (0, 0, 0))
        window.blit(coin, (10, 10))

        if coins_amount_1 >= 9:
            final_sprite.reset()
        
        if sprite.spritecollide(player1, monsters, False):
            finish = True
            img = image.load('losec.jpg')
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

        if sprite.collide_rect(player1, final_sprite):
            finish = True
            img = image.load('win.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))


        time.delay(50)
        display.update()