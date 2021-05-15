#Подключить библиотеки
from random import randint
from pygame import *
#pygame.init()
window = display.set_mode((700, 500))
display.set_caption("TOP SHUTER 228 335")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
#Подключить музыку

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play() 

#Работа с ФПС
clock = time.Clock()
FPS = 40
clock.tick(FPS)

#Создание заготовок спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit( self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        #if keys [K_SPACE]:
            #self.fire()
    def fire(self):
        global num_fire
        global reloading
        global rel_time
        if not reloading:
            
            b = Bullet("bullet.png", self.rect.x + 20, self.rect.top, 10, 20, 5)
            bullets.add(b)
            bam = mixer.Sound("fire.ogg")
            bam.play()
            num_fire += 1
            print(num_fire)
            if num_fire >= 8: 
                reloading = True
                rel_time = time.get_ticks()




class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
            global lost
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()


#Спрайты победы и проигрыша
font.init()
font1 = font.SysFont("Arial", 30)
lost = 0
win = font1.render("YOU WIN!!!", 1, (0, 255, 0)) 
lose = font1.render("YOU LOSE!!!", 1, (255, 0, 0))

#Создание спрайтов
cosmolet = Player('rocket.png', 50, 400, 60, 100, 5)
#Создание группы спрайтов
monsters = sprite.Group()
for i in range(5):
    m = Enemy('ufo.png', randint(50, 650), 0, 80, 40, randint(1, 2))
    monsters.add(m)
#aster = Enemy('asteroid.png', randint(50, 650), 0, 80, 40, randint(1, 2))
#monsters.add(aster)

bullets = sprite.Group()

asteroids = sprite.Group()
for i in range(2):
    asteroid = Enemy('asteroid.png', randint(50, 650), 0, 80, 40, randint(1, 2))
    asteroids.add(asteroid)
def restart():
    global score
    global lost
    score = 0
    lost = 0
    num_fire = 0
    for m in monsters:
            m.rect.y = 0
    for asteroid in asteroids:
        asteroid.rect.y = 0
#Игровой цикл(Финиш, счет, работа со спрайтами, столконовения со спрайтами, рестарт, перезарядка оружия)
score = 0
num_fire = 0
rel_time = time.get_ticks()
reloading = False
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                cosmolet.fire()
    if not finish:
        sprite_list = sprite.groupcollide(monsters, bullets, True, True)
        for i in sprite_list:
            score += 1
            m = Enemy('ufo.png', randint(50, 650), 0, 80, 40, randint(1, 2))
            monsters.add(m)
        window.blit(background, (0, 0))
        text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (30, 40)) 
        text_win = font1.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text_win, (30, 15))
        cosmolet.reset()
        cosmolet.update()
        asteroids.draw(window)
        asteroids.update()
        monsters.draw(window) 
        monsters.update()
        bullets.draw(window)
        bullets.update()
    if score >= 10:
        finish = True
        rel_time = time.get_ticks()
        restart()
        window.blit(win, (280, 250))
    if lost >= 8 or sprite.spritecollide(cosmolet, monsters, False) or sprite.spritecollide(cosmolet, asteroids, False):
        finish = True
        rel_time = time.get_ticks()
        restart()
        window.blit(lose, (280, 250))
    if reloading:
        text_reloading = font1.render("Перезарядка!", 1, (255, 255, 255))
        window.blit(text_reloading, (300, 450))
    if reloading and time.get_ticks() - rel_time > 3000:
        reloading = False
        num_fire = 0 
    if finish == True and time.get_ticks() - rel_time > 5000:
        finish = False
        restart()
        print(finish)
        
    print(time.get_ticks() - rel_time)
    display.update()
    clock.tick(FPS)




