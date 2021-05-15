from pygame import *
widht = 700
hight = 600
FPS = 120
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
        if keys [K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

rok1 = Player("raketka.png", 10, 50, 50, 150, 5)
rok2 = Player("raketka.png", 645, 50, 50, 150, 5)

window = display.set_mode((widht, hight))
display.set_caption("Ping-Pong")
window.fill((200, 200, 255))

run = True
while run:
    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            run = False
    rok1.reset()
    rok1.update1()
    rok2.reset()
    rok2.update2()
    display.update()
    time.delay(50)
