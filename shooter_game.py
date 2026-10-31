from pygame import *
from random import *
win = display.set_mode((700,500))
display.set_caption("Shooter Game🔫")
bg = transform.scale(image.load("galaxy.jpg"), (700,500))
clock = time.Clock()


#mixer.init()
#mixer.music.load("jungles.ogg")
#mixer.music.play()
                        #bawaan pygamenya
class gamesprite(sprite.Sprite):
    def __init__(self, img, x, y,w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def plot(self):
        win.blit(self.image, (self.rect.x,self.rect.y))


class Player(gamesprite):
    def control(self):
        tombol = key.get_pressed()
        if tombol[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if tombol[K_RIGHT] and self.rect.x < 625:
            self.rect.x += self.speed
    def fire(self):
        peluru = Bullet("bullet.png", self.rect.centerx, self.rect.top,15,20, 10)
        bullets.add(peluru)


class Ufo(gamesprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 490:
            self.rect.y = 10
            self.rect.x = randint(10, 625)

class Bullet(gamesprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
player = Player("rocket.png", 10, 425,80,100, 5)
monster = sprite.Group()
for i in range(1,6):
    enemy = Ufo("ufo.png", randint(10, 625), 10, 80,50,randint(1,5))
    monster.add(enemy)
bullets = sprite.Group()

font.init()
font1 = font.SysFont("Consolas", 70)
font2 = font.SysFont("Consolas", 36)
kalah = font2.render("YAHHH KAMU KALAH :( ToT", True, (255, 255, 255))
menang = font1.render("HOORAYY!🤯", True, (225, 255, 255))
finish = False
score = 0
lost = 0

        

run = True
while run:
    for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    player.fire()
                
    if finish == False:
        win.blit(bg, (0,0))
        player.plot()
        player.control()
        bullets.draw(win)
        bullets.update()
        monster.draw(win)
        monster.update()
        skor = font2.render("Score:" + str(score), True, (255, 255, 255))
        missed = font2.render("Missed:" + str(lost), True, (225, 255, 255))
        win.blit(skor, (10,20))
        win.blit(missed, (10, 50))

        collides = sprite.groupcollide(monster, bullets, True, True)
        for c in collides:
            score += 1
            enemy = Ufo("ufo.png", randint(10, 625), 10, 80,50,randint(1,5))
            monster.add(enemy)
        if sprite.spritecollide(player, monster, False) or lost > 3:
            win.blit(kalah, (200,200))
            finish = True
        if score >= 10:
            win.blit(menang, (200,200))
            finish = True
        #if sprite.collide_rect(enemy, enemy):
            #win.blit(menang, (200,200))
            #finish = True
        
        display.update()
    #bonus: automatic restart of the game
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monster:
            m.kill()


        time.delay(3000)
        for i in range(1, 6):
            enemy= Ufo('ufo.png', randint(10, 625), 10, 80, 50, randint(1, 5))
            monster.add(enemy)
    clock.tick(60)





