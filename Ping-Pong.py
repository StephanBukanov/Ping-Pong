from pygame import *
widht = 700
hight = 600
FPS = 120
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed, player_speed2 = 0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.speed2 = player_speed2
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit( self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if self.rect.y < 0:
            self.speed2 *= -1
        if self.rect.y > 550:
            self.speed2 *= -1
        
font.init()
font1 = font.Font(None, 40)
fin1 = font1.render("Player 2 win!", 1, (0, 255, 0)) 
fin2 = font1.render("Player 1 win!", 1, (0, 255, 0)) 
rok1 = Player("raketka.png", 10, 50, 50, 150, 7)
rok2 = Player("raketka.png", 645, 400, 50, 150, 7)
ball = Ball("algoball.png", 80 , 50, 50, 50, 8, 8) 
pl1 = font1.render("Player 1", 1, (0, 255, 0))
pl2 = font1.render("Player 2", 1, (0, 255, 0))

window = display.set_mode((widht, hight))
display.set_caption("Ping-Pong")
window.fill((200, 200, 255))
finish = False
run = True
while run:
    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            run = False
    ball.reset()
    ball.update()
    rok1.reset()
    rok1.update1()
    window.blit(pl1, (15, 15))
    window.blit(pl2, (575, 15))
    rok2.reset()
    rok2.update2()
    if ball.rect.x < 0:
        finish = True
        window.blit(fin1, (260, 300))
    if ball.rect.x > 650:
        finish = True
        window.blit(fin2, (260, 300))
    if sprite.collide_rect(ball, rok1) or sprite.collide_rect(ball, rok2):
        ball.speed *= -1
    display.update()
    time.delay(50)
